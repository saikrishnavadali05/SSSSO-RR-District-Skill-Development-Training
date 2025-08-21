class Node:      #Node class for linked list
    def __init__(self, data):   #Constructor to initialize the node with data 
        self.data = data      #Data to be stored in the node
        self.next = None   #Pointer to the next node, initiated to none

def reverse_linked_list(head):    #Function to reverse the linked list
    prev = None    #Previous node, initiated to none
    current = head    #Current node, starting with the head of the list
    while current:      #Iterate through the linked list until current is none
        next_node = current.next   #Store the next node
        current.next = prev    #Reverse the link by pointing current's next to previous
        prev = current   #Move prev to current node
        current = next_node     #Move to the next node
    return prev    #Return the new head of the reversed linked list

#Output:
# The linked list has been reversed successfully

