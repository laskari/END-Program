class Student:

    def __int__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None,b=None, c=None):
        if a!=None and b!= None and c!= None:
            return a+b+c
        elif a!=None and b!= None:
            return a+b
        else:
            return c


s1= Student()


print(s1.sum(10,20, 30))

