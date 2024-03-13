class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.data=None

def insertvalue(self,data):
    temp=Node(data)
    temp.next=self.first
    self.first=temp
def display(self):
    if(self.first==None):
        print("list is empty")
        return