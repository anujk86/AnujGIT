import ssl

Queue = []
def push(item):
	Queue.append(item)
	print('Item added in Queue:', item)

def pop():
	if (isempty() == False):
		print('Queue is empty !!')
		return
	print('Removed Item :',Queue.pop())
def top():
	if (isempty() == False):
		print('Queue is empty !!')
		return
	print('Top Item from Queue :',Queue[0])

def isempty():
	if len(Queue)> 0:
		return True
	else:
		return False

push(3)
push(4)
push(5)
top()
pop()
top()
pop()
top()
pop()