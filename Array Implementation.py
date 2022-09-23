class array():
    def __init__(self):
        self.l=[]
    def insert_at_last(self,lst,val):
        l=lst
        l.append(val)
        return l
    def insert_at_start(self,lst,val):
        l=lst
        l.insert(0,val)
        return l
    def insert_at_mid(self,lst,val,index):
        l=lst
        l.insert(index,val)
        return l
    def to_clear(self,lst):
        l=lst
        l.clear()
        return l
    def to_pop(self,lst):
        l=lst
        l1=l.pop()
        return l1
    def to_remove(self,lst,val):
        l=lst
        l.remove(val)
        return l
    def to_get_index(self,lst,val):
        l=lst
        l1=l.index(val)
        return l1
    def to_sort(self,lst):
        l=lst
        l.sort()
        return l
    def to_get_min(self,lst):
        l=lst
        l1=min(l)
        return l1
    def to_get_max(self,lst):
        l=lst
        l1=max(l)
        return l1
    def to_get_length(self,lst):
        l=lst
        l1=len(l)
        return l1
    def to_reverse(self,lst):
        l=lst
        l.reverse()
        return l
    def to_sum(self,lst):
        l=lst
        l1=sum(l)
        return l1
    def to_display_list(self,lst):
        l=lst
        return l
obj=array()
lst=[]#list is created
length=int(input("Enter A Length Of A List:"))#length of list 
print("Enter The List Elements:")#for user to give values
for i in range(length):
    values=int(input())#values are getten
    lst.append(values)#adding to list
c='y'
while(c=='y'):
    print("Enter '1' for insert a value in a list at start")
    print("Enter '2' for insert a value in a list at end")
    print("Enter '3' for insert a value in a list at Your Position")
    print("Enter '4' for Clear a list")
    print("Enter '5' for pop a list")
    print("Enter '6' for Remove some element from a list")
    print("Enter '7' for get a index for a value in a list")
    print("Enter '8' to sort  a list in asscending")
    print("Enter '9' to get a min in a list")
    print("Enter '10' to get a max in a list")
    print("Enter '11' to get a length of the list")
    print("Enter '12' to reverse a list")
    print("Enter '13' to get the sum of the list")
    print("Enter '14' to display the list")
    print("------------------------------------------------------------------------------------------")
    choice=int(input("Enter The Choice From Above Function:"))
    if choice==1:
        val=int(input("Enter The Value To Add:"))
        res=obj.insert_at_start(lst,val)
        print(res)
    elif choice==2:
        val=int(input("Enter The Value To Add:"))
        res=obj.insert_at_last(lst,val)
        print(res)
    elif choice==3:
        val=int(input("Enter The Value To Add:"))
        pos=int(input("Enter The Position For Adding value:"))
        res=obj.insert_at_mid(lst,val,pos)
        print(res)
    elif choice==4:
        res=obj.to_clear(lst)
        print(res)
    elif choice==5:
        res=obj.to_pop(lst)
        print(res)
    elif choice==6:
        val=int(input("Enter The Element In a List:"))
        res=obj.to_remove(lst,val)
        print(res)
    elif choice==7:
        val=int(input("Enter The Element In a List To Get Index:"))
        res=obj.to_get_index(lst,val)
        print(res)
    elif choice==8:
        res=obj.to_sort(lst)
        print(res)
    elif choice==9:
        res=obj.to_get_min(lst)
        print(res)
    elif choice==10:
        res=obj.to_get_max(lst)
        print(res)
    elif choice==11:
        res=obj.to_get_length(lst)
        print(res)
    elif choice==12:
        res=obj.to_reverse(lst)
        print(res)
    elif choice==13:
        res=obj.to_sum(lst)
        print(res)
    elif choice==14:
        res=obj.to_display_list(lst)
        print(res)
    print("------------------------------------------------------------------------------------------")
    c=input("To Continue The Above Function Press 'y' If not press 'n':")
print("Program Exit")




