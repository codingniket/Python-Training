class Score:
    def add(self,*args):
        return sum(args)

x = Score()
print(x.add(3,4))