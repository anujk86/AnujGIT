stack_1 = []
stack_2 = []

def push(item):
	stack_1.append(item)
	print('Item added in Queue:', item)

def pop():
	if len(stack_2) == 0:
		# If stack_1 is empty, raise an error
		if (isempty() == False):
			print("Queue is empty Can't dequeue from empty queue !!!")
			return
	# while stack_1 is not empty,
	while len(stack_1) > 0:
		last_stack_1_item = stack_1.pop()
		stack_2.append(last_stack_1_item)

	print('Removed Item :',stack_2.pop())

def isempty():
	if len(stack_1)<= 0:
		return False
	else:
		return True

push(1)
push(2)
push(3)
push(4)
push(5)
print(stack_1)
pop()
print(stack_2)
pop()
print(stack_2)
pop()
print(stack_2)
pop()
print(stack_2)
push(6)
print(stack_1)
print(stack_2)