stack = []
Minstack = []
def push(item):
	stack.append(item)
	print('Item added in stack:', item)
	if len(Minstack) <= 0:
		Minstack.append(item)
	else:
		if int(Minstack [len(Minstack)-1]) <= int(item):
			Minstack.append(Minstack [len(Minstack)-1])
		else:
			Minstack.append(item)
def Min():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Min Item from Stack :',Minstack [len(Minstack)-1])

def pop():
	if (isempty() == False):
		print('Stack is empty !!')
		return
	print('Removed Item :',stack.pop())
	Minstack.pop()

def isempty():
	if len(stack)<= 0:
		return False
	else:
		return True

push(3)
push(4)
push(5)
Min()
pop()
Min()
pop()
Min()