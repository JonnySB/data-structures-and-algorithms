from Modules.linked_list_class import LinkedList

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_as_list() # Output: 3 5 8 10 2 1s

ll.partition_list(5)

print("LL after partition_list:")
ll.print_as_list() # Output: 3 2 1 5 8 10
