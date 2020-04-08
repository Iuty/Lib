
def MA(index,serial,itemindex,period):
	if period > index:
		return None
	if index >= len(serial):
		return None
	total = 0.0
	for i in range(index-period,index+1):
		total += serial[i][itemindex]
	return total/period

def HHV(index,serial,itemindex,period):
	if period > index:
		return None
	if index > len(serial):
		return None
	hhv = serial[index][itemindex]
	for i in range(index-period,index):
		if serial[i][itemindex] > hhv:
			hhv = serial[i][itemindex]
	return hhv

def LLV(index,serial,itemindex,period):
	if period > index:
		return None
	if index > len(serial):
		return None
	llv = serial[index][itemindex]
	for i in range(index-period,index):
		if serial[i][itemindex] < llv:
			llv = serial[i][itemindex]
	return llv

def SMA(Pre,Cur,N,M):
	if (M>N):
		return None
	
	v = ((N-M)*Pre + M * Cur)/N
	return v

def KDJ(index,dailyserial,kdjserial):
	if index > len(dailyserial):
		return None
	r_kdj = [datetime.date(2000,1,1),0.0,0.0,0.0,0.0]
	if len(kdjserial) > 0:
		r_kdj = kdjserial[-1]
	hhv = HHV(index,dailyserial,2,9)
	llv = LLV(index,dailyserial,3,9)
	rsv == 0.0
	if hhv != llv:
		rsv = 100.0*(dailyserial[index][4]-llv)/(hhv-llv)
	
	k = SMA(r_kdj[1],rsv,3,1)
	d = SMA(r_kdj[2],k,3,1)
	j = 3*k-2*d
	return (dailyserial[index][0],rsv,k,d,j)

def DLT(index,dailyserial):
	d_data = dailyserial
	level = [5,10,30,60]
	value = [d_data[index][0],]
	for li in range(0,len(level)):
		if 2*level[li] <= index:
			v = 0.0
			for ii in range(0,level[li]):
				v +=(d_data[index-ii][4] - d_data[index-ii-level[li]][4])/level[li]
			av = v/level[li]
			value.append(av)
		else:
			value.append(None)
	return tuple(value)