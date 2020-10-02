#circular_linked_list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class clinkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp.next!=llist.head):
            print(temp.data)
            temp=temp.next
            last=temp      
        while(last):
            print(last.data)
            last=last.prev
            
        
    
llist=clinkedlist()
llist.head=node(20)
second=node(40)
second.prev=llist.head
third=node(60)
third.prev=second
third.next=llist.head
llist.head.next=second
second.next=third
llist.printlist()
