class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position=0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index is not present")

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node!=None and position!=index):
                position = position + 1
                current_node = current_node.next
            if current_node!= None:
                current_node.data = val
            else:
                print("Index is not present")
    
    def removeLastNode(self):
        if self.head is None:
            return
        current_node= self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None
    
    def removeFirstNode(self):
        if(self.head == None):
            return
        self.head = self.head.next

    def removeAtIndex(self,index):
        if self.head ==None:
            return
        current_node = self.head
        position=0
        if(position == index):
            self.removeFirstNode()
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node=current_node.next
            if current_node!= None:
                current_node.next= current_node.next.next
            else:
                print("Index is not present")
    
    def removeNode(self,data):
        current_node = self.head
        if current_node.data==data:
            self.head = current_node.next
            return
        try:
            while(current_node!=None and current_node.next.data !=data):
                current_node = current_node.next
            if current_node == None:
                return
            current_node.next = current_node.next.next
        except:
            print("Data not found for deletion")

    def sizeOfLL(self):
        size=0
        if(self.head):
            current_node = self.head
            while(current_node):
                size +=1
                current_node = current_node.next
            return size
        else:
            return 0
    
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

ll = LinkedList()
print()
print("MENU:\n 1 INSERT\n 2 UPDATE\n 3 DELETE\n 4 EXIT")
print()
inp = int(input("Please enter a number from the menu corresponding to the operation to be performed: "))


while(inp!=4):
    if inp==1:
        print("INSERTION SUB-MENU:\n 1 INSERT AT THE BEGINNING\n 2 INSERT AT INDEX\n 3 INSERT AT THE END\n 4 EXIT INSERTION SUB-MENU")
        inpinsert=int(input("Please enter a number from the sub-menu corresponding to the type of insertion: "))
        while(inpinsert!=4):
            if inpinsert==1:
                inpinsbeg = str(input("Enter value to be inserted at the beginning: "))
                ll.insertAtBegin(inpinsbeg)
                ll.printLL()
            elif inpinsert==2:
                inpinsind = str(input("Enter value to be inserted: "))
                indexins = int(input("Enter index: "))
                ll.insertAtIndex(inpinsind, indexins)
                ll.printLL()
            elif inpinsert==3:
                inpinsend = str(input("Enter value to be inserted at the end: "))
                ll.insertAtEnd(inpinsend)
                ll.printLL()
            else:
                print("Please enter a number present in the sub-menu")
            inpinsert=int(input("Please enter a number from the sub-menu corresponding to the type of insertion: "))
        if inpinsert==4:
            print("INSERT sub-menu exited")
            continue

    elif inp==2:
        print("UPDATE:")
        inpupval=str(input("Enter the updated value: "))
        inpupindex=int(input("Enter index where the value is to be updated: "))
        ll.updateNode(inpupval,inpupindex)
    
    elif inp==3:
        print("DELETION SUB-MENU:\n 1 DELETE AT THE BEGINNING\n 2 DELETE AT INDEX\n 3 DELETE AT THE END\n 4 EXIT DELETION SUB-MENU")
        inpdelete=int(input("Please enter a number from the sub-menu corresponding to the type of deletion: "))
        while(inpdelete!=4):
            if inpdelete==1:
                ll.removeFirstNode()
                ll.printLL()
            elif inpinsert==2:
                indexdel = int(input("Enter index of value to be deleted: "))
                ll.removeAtIndex(indexdel)
                ll.printLL()
            elif inpdelete==3:
                ll.removeLastNode()
                ll.printLL()
            else:
                print("Please enter a number present in the sub-menu")
            inpinsert=int(input("Please enter a number from the sub-menu corresponding to the type of insertion: "))
        if inpdelete==4:
            print("DELETE sub-menu exited")
            continue


    else:
        print("Please enter a number present in the menu")
    inp = int(input("Please enter a number from the menu corresponding to the operation to be performed: "))   

if inp==4:
    print("Program exited")