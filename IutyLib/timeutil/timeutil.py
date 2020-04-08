import datetime,time

def getTimeTamp(time = None):
	if time is None:
		return datetime.datetime.now()
	now = datetime.datetime.now()
	if now.time() < time:
		now = now - datetime.timedelta(1)
	return datetime.datetime(now.year,now.month,now.day,time.hour,time.minute,time.second)
	
def showTime():
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))