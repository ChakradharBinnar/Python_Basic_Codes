class Count_Obj:
    count = 0

    def __init__(self):
        Count_Obj.count = Count_Obj.count+1


obj1 = Count_Obj()
obj2 = Count_Obj()
obj3 = Count_Obj()
obj4 = Count_Obj()

print(obj1.count)
