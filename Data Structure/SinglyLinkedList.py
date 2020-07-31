import sys

"""
Homework (Please Exeute in the same order ): 

SINGLY LINKED LIST 

-> Functions to write 
1) add_elememt_at_the start 
2) Delete element at the start 
3) is_empty
4) add element at the end 
5) delete element at the end 
6) add element at the kth Location of a linked List 
7) Delete Element at the kth location of a linked List 
8) Traverse the linked List 
9) Reverse the Linked List 
10) Implement stacks using Linked List 
11) Implement Queues using Linked List  
"""

class Node:
	def __init__(self, data):
		self.data = data 
		self.next_node = None 

class LinkedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head == None:
			print ("Linked List Empty")
			return True
		else:
			print ("Linked List Not Empty")
			return False

	def add_element_at_the_start(self, data):
		# Consider Linked List is empty 
		if self.is_empty():
			new_node = Node(data)
			self.head = new_node

		# Consider Linked List is not Empty 
		else:
			new_node = Node(data)
			new_node.next_node = self.head
			self.head = new_node

	def delete_element_from_the_start(self):
		if self.is_empty():
			print ("No elements in the Linked List cannot Delete")
		else:
			self.head = self.head.next_node

	def traverse_linked_list (self):
		if self.is_empty():
			print ("No Elements in the Linked List")
		else:
			temp = self.head 
			while temp != None:
				print (temp.data)
				temp = temp.next_node

	def add_element_at_end_of_ll(self, data):
		if self.is_empty():
			new_node = Node(data)
			self.head = new_node
		else:
			new_node = Node(data)
			temp = self.head 
			while temp.next_node != None:
				temp = temp.next_node
			temp.next_node = new_node

	def delete_element_at_end_of_ll(self):
		if self.is_empty():
			print ("No Elements in the Linked list to delete !!")
		else :
			currentNode = self.head
			while currentNode.next_node !=None:
				previousNode = currentNode
				currentNode = currentNode.next_node
			previousNode.next_node = None

	def add_elememt_at_Specific(self, data, position):
		# Consider Linked List is empty 
		if self.is_empty():
			new_node = Node(data)
			self.head = new_node

		# Consider Linked List is not Empty 
		else:
			new_node = Node(data)
			Curnode = self.head
			CurPosition = 0

			while True:
				if CurPosition == position:
					PrevNode.next_node =new_node
					new_node.next_node =Curnode
					break					
				PrevNode = Curnode
				Curnode = Curnode.next_node
				CurPosition += 1

	def delete_elememt_at_Specific(self, position):
		if self.is_empty():
			print ("No elements in the Linked List cannot Delete")
		else:
			Curnode = self.head
			CurPosition = 0
			while True:
				if CurPosition == position:
					PrevNode.next_node = Curnode.next_node
					Curnode.next_node = None
					break					
				PrevNode = Curnode
				Curnode = Curnode.next_node
				CurPosition += 1

	def reverse_ll(self):
		PrevNode = None
		Curnode = self.head
		NextNode = None
		while Curnode:
			NextNode = Curnode.next_node
			Curnode.next_node = PrevNode
			PrevNode = Curnode
			Curnode = NextNode
		self.head =PrevNode

a = LinkedList()
a.add_element_at_the_start(5)
a.add_element_at_the_start(2)
a.add_element_at_the_start(3)
a.traverse_linked_list()
a.reverse_ll()
a.traverse_linked_list()
#a.traverse_linked_list()
#a.add_elememt_at_Specific(10, 2)
#a.traverse_linked_list()
#a.delete_elememt_at_Specific(2)
#a.traverse_linked_list()
#a.delete_elememt_at_Specific(1)
#a.traverse_linked_list()
#a.delete_element_from_the_start()
#a.traverse_linked_list()
#a.delete_element_at_end_of_ll()
#a.traverse_linked_list()

'''
a = LinkedList()
a.traverse_linked_list()  # No element 
a.add_element_at_the_start(5)
a.add_element_at_the_start(2)
a.traverse_linked_list() # 2, 5
a.delete_element_from_the_start()
a.traverse_linked_list() # 5
a.delete_element_from_the_start()
a.delete_element_from_the_start() # Empty Linked List 
'''