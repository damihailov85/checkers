import random

class Pawn(object):
    
    def __init__(self, a, d, l, h):
        self.attack = a
        self.defence = d
        self.luck = l
        self.health = h

    def method1(self, x):
        return 2*x



class Game():
    
    def __init__(self, num):
        self.arr = list()
        max_x = 0
        max_y = 0
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        for i in range(num):
            x = random.randint(0,10)
            y = random.randint(0,10)
            z = random.randint(10,20)
            obj = Pawn(x, y, z, 100)
            self.arr.append(obj)

            
    def round(self):
        #print(len(self.arr), ">>>>>>>>>>>>>>>>>>>")
        next_arr = list()
        random.shuffle(self.arr)
        l = len(self.arr)
        i = 0
        
        while i < l:
            h1 = self.arr[i].health
            h2 = self.arr[i+1].health
            a1 = self.arr[i].attack
            a2 = self.arr[i+1].attack
            d1 = self.arr[i].defence
            d2 = self.arr[i+1].defence
            l1 = self.arr[i].luck
            l2 = self.arr[i+1].luck
            while h1 > 0 and h2 > 0:
                t1 = max(0, a2 + random.randint(0, l2) - d1 - random.randint(0, l1))
                h1 = h1 - t1
                if h1 <= 0:
                    if (a2 == 0 or d2 == 0) and a1 > 4 and d1 > 4 and l2 < l1:
                        print("win ", a2, d2, l2, h2, " lose ", a1, d1, l1)
                    self.arr[i+1].h = min(100, h2 + 20)
                    next_arr.append(self.arr[i+1])
                    continue
                t2 = max(0, a1 + random.randint(0, l1) - d2 - random.randint(0, l2))
                h2 = h2 - t2
                if h2 <= 0:
                    if (a1 == 0 or d1 == 0) and a2 > 4 and d2 > 4 and l1 < l2:
                        print("win ", a1, d1, l1, h1, " lose ", a2, d2, l2)
                    self.arr[i].h = min(100, h1 + 20)
                    next_arr.append(self.arr[i])
                    continue
            i += 2
        self.arr = next_arr
        if len(self.arr) > 1:
            self.round()

n = 1000
a = 0
d = 0
l = 0

for i in range(n):        
    g = Game(128)
    g.round()
    a += g.arr[0].attack
    d += g.arr[0].defence
    l += g.arr[0].luck
    
print(a / n, d / n, l / n)    