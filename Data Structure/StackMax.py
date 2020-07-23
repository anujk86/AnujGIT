stack = []
Mstack = []
def push(item):
	stack.append(item)
	print('Item added in stack:', item)
	if len(Mstack) <= 0:
		Mstack.append(item)
	else:
		if int(Mstack [len(Mstack)-1]) >= int(item):
			Mstack.append(Mstack[len(Mstack)-1])
		else:
			Mstack.append(item)
def Max():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Max Item from Stack :',Mstack [len(Mstack)-1])

def pop():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Removed Item :',stack.pop())
	Mstack.pop()

def isempty():
	if len(stack)<= 0:
		return False
	else:
		return True
push(4)
push(2)
push(3)
push(5)
push(7)
print(Mstack)
print(stack)
Max()
pop()
Max()
pop()
Max()