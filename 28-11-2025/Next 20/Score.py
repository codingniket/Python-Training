class Score:
    def cal(self,*args) -> int:
        return sum(args)

x = Score()
print(x.cal(3,4,7,8,8,9,7,2))