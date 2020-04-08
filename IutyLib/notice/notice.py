import time
import requests
import json,os


class WeChat_SMS:
	def __init__(self,corpsecret = '_4vuUmRxg9V5bnb1dZ2QlhHIBiwIL5O7SMvowRX7_WA',agentid = '1000002',partid='0'):
		self._corpid = 'ww97a5a59259fbb43d'#企业ID， 登陆企业微信，在我的企业-->企业信息里查看
		self._corpsecret = corpsecret#自建应用，每个自建应用里都有单独的secret
		self._agentid = agentid #应用代码
		self._partid = partid


	@property
	def CorpId(self):
		return self._corpid
		
	@CorpId.setter
	def CorpId(self,value):
		self._corpid = value
		
	@property
	def CorpSecret(self):
		return _corpsecret
		
	@CorpSecret.setter
	def CorpSecret(self,value):
		self._corpsecret = value
		
	@property
	def AgentId(self):
		return _agentid
		
	@AgentId.setter
	def AgentId(self,value):
		self._agentid = value
		

	def _get_access_token(self):
		url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
		values = {'corpid': self._corpid,'corpsecret': self._corpsecret,}
		req = requests.post(url, params=values)
		data = json.loads(req.text)
		return data["access_token"]

	def get_access_token(self):
		try:
			with open('access_token_{0}.conf'.format(self._agentid), 'r') as f:
				t, access_token = f.read().split()
		except:
			with open('access_token_{0}.conf'.format(self._agentid), 'w') as f:
				access_token = self._get_access_token()
				cur_time = time.time()
				f.write('\t'.join([str(cur_time), access_token]))
				return access_token
		else:
			cur_time = time.time()
			if 0 < cur_time - float(t) < 7200:#token的有效时间7200s
				return access_token
			else:
				with open('access_token_{0}.conf'.format(self._agentid), 'w') as f:
					access_token = self._get_access_token()
					f.write('\t'.join([str(cur_time), access_token]))
					return access_token

	def send_data(self, msg,user='@all'):
		send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
		send_values = {
			"touser": user,
			"toparty": self._partid, 	#设置给部门发送
			"msgtype": "text",
			"agentid": self._agentid,
			"text": {
			"content": msg
			},
			"safe": "0"
		}
		send_msges=(bytes(json.dumps(send_values), 'utf-8'))
		respone = requests.post(send_url, send_msges)
		respone = respone.json()#当返回的数据是json串的时候直接用.json即可将respone转换成字典
		#print (respone["errmsg"])
		return respone["errmsg"]


if __name__ == '__main__':
    wx = WeChat_SMS()
    wx.send_data(msg="服务崩了，你还在这里吟诗作对？")
    #以下是添加对日志的监控
    # srcfile = u"G:/123.txt"
    # file = open(srcfile)
    # file.seek(0, os.SEEK_END)
    # while 1:
    #     where = file.tell()
    #     line = file.readline()
    #     if not line:
    #         time.sleep(1)
    #         file.seek(where)
    #     else:
    #         print(line)
    #         wx.send_data(msg=line)
