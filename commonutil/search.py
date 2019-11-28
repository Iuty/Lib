
def getSerialItem(serial,index,key=0):
	start = 0
	end = len(serial)
	while True:
		
		cur = (end-start)//2 + start
		if serial[cur][key] == index:
			return serial[cur]
		if end == start:
			return None
		if serial[cur][key] < index:
			start = cur
		
		else:
			end = cur
	pass