stack = []
def push(item):
	stack.append(item)
	print('Item added in stack:', item)

def pop():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Removed Item :',stack.pop())
def top():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Top Item from Stack :',stack [len(stack)-1])

def isempty():
	if len(stack)<= 0:
		return False
	else:
		return True
push(3)
push(4)
push(5)
top()
pop()
top()
pop()
pop()
pop()
pop()