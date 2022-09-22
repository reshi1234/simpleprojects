class array():
    def __init__(self):
        self.l=[]
    def insert_at_last(self,lst,val):
        l=lst
        l.appedd(val)
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
        l1=l.index(lst,val)
        return l1
    def to_sort(self,lst):
        l=lst
        l.sort()
        return l
    def to_get_min(self,lst):
        l=lst
        l1=l.min()
        return l1
    def to_get_max(self,lst,val):
        l=lst
        l1=l.max()
        return l1

obj=array()
lst=[1,2,4,5,6]
res=obj.insert_at_mid(lst,3,2)
print(res)

