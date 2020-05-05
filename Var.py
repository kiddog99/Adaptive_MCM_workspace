import random
class Var:
    def __init__(self):
        self.name = None
        self.father = None
        self.typ = None
        self.value = None
        #三角分布
        self.low = None
        self.high = None
        self.mode = None #默认中间点
        #高斯分布、对数正态分布、正态分布
        self.mu = None #平均值
        self.sigma = None #标准差
        #beta分布、伽马分布、帕累托分布、韦伯分布
        self.alpha = None
        self.beta = None
        #指数分布
        self.lambd = None
    def generator(self):
        if self.typ == "三角分布":
            if None in [self.low, self.high]:
                return False
            else:
                try:
                    self.value = random.triangular(self.low, self.high)
                except:
                    self.value = 999
        elif self.typ == "均匀分布":
            if None in [self.low, self.high]:
                return False
            else:
                try:
                    test = random.uniform(self.low, self.high)
                    self.value = test
                except:
                    self.value = 999
        elif self.typ == "正态分布":
            if None in [self.mu, self.sigma]:
                return False
            else:
                try:
                    self.value = random.normalvariate(self.mu, self.sigma)
                except:
                    self.value = 999
        elif self.typ == "高斯分布":
            if None in [self.mu, self.sigma]:
                return False
            else:
                try:
                    self.value = random.gauss(self.mu, self.sigma)
                except:
                    self.value = 999
        elif self.typ == "beta分布":
            if None in [self.alpha, self.beta]:
                return False
            else:
                try:
                    self.value = random.betavariate(self.alpha, self.beta)
                except:
                    self.value = 999
        elif self.typ == "指数分布":
            if None in [self.lambd]:
                return False
            else:
                try:
                    self.value = random.expovariate(self.lambd)
                except:
                    self.value = 999
        elif self.typ == "伽马分布":
            if None in [self.alpha, self.beta]:
                return False
            else:
                try:
                    self.value = random.gammavariate(self.alpha, self.beta)
                except:
                    self.value = 999
        elif self.typ == "对数正态分布":
            if None in [self.mu, self.sigma]:
                return False
            else:
                try:
                    self.value = random.lognormvariate(self.mu, self.sigma)
                except:
                    self.value = 999
        else:
            return False

class MidVar:
    def __init__(self):
        self.name = None
        self.formula = None
        self.tempfor = None
        self.VarLi = []
        self.value = None
    def generator(self, li:dict):
        TempFormula = self.formula
        for var in self.VarLi:
            TempFormula = TempFormula.replace(var, str(li[var].value))
        try:
            print(TempFormula)
            self.value = eval(TempFormula)
        except:
            self.value = 999

'''A = Var()
A.typ = "均匀分布"
A.low = 11
A.high = 22
List = {"A":A}
List["A"].generator()
print(A.value)'''