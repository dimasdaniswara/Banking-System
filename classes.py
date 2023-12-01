class user:
    #initializer
    def __init__(self,username,password) -> None:

        self.username = username
        self.password = password
        

    def getinfo(self):

        return f"{self.username} {self.password}"
    
class Linkedlist:
        
    def __init__(self) -> None:
        self.head = None
        pass

    def insertBeginning(self,username,password):
        new_user = user(username,password)
        new_user.next = self.head
        self.head = new_user

    def insertEnd(self,username,password):
        new_user = user(username,password)
        if self.head == None :
            self.head = new_user
        else:
            current_user = self.head
            current_user.next = new_user
            self.head = new_user

    def deleteBeginning(self):
        temp = self.head
        self.head = temp.next
        del temp

    def deleteEnd(self):
        if self.head is not None:
            if self.head.next is None:
                temp = self.head
                self.head = None
                del temp
            else:
                current_user = self.head
                while current_user.next.next is not None:
                    current_user = current_user.next
                temp = current_user.next
                current_user.next = None
                del temp

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.username,current_node.password)
            current_node = current_node.next
    
    def search_account(self,username,password):
        current_node = self.head
        while current_node is not None:
            if current_node.username == username:
                if current_node.password == password:
                    return True
            else:
                current_node = current_node.next



