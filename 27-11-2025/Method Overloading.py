class Math0ps:
    def add(self, a, b=0,c=0):
        return a + b + c
m = Math0ps()
print(m.add(5))
print(m.add(5,10))
print(m.add(5,10,20))

class MathArgs:
    def add(self,*args):
        return sum(args)
m = MathArgs()
print(m.add(5))
print(m.add(5,10))
print(m.add(5,10,20))
