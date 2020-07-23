Queue = []
def push(item):
	Queue.append(item)
	print('Item added in Queue:', item)

def pop():
	if (isempty() == False):
		print('Queue is empty !!')
		return
	print('Removed Item :',Queue.pop(0))

def Max():

	if (isempty() == False):
		print('Queue is empty !!')
		return
	MaxVal = Queue[0]
	while len(Queue) > 0:
		if MaxVal < Queue[0]:
			MaxVal = Queue[0]
		else:
			return
	print('Max Item :',MaxVal)
	
def top():
	if (isempty() == False):
		print('Queue is empty !!')
		return
	print('Top Item from Queue :',Queue[0])

def isempty():
	if len(Queue)<= 0:
		return False
	else:
		return True
push(3)
push(4)
push(5)
Max()