import board as b
import time



class Game():

    def __init__(self) -> None:
        self.bb = b.Board()
        self.list()




    def list(self):
        s = 0
        for j in self.bb.arr_1:
            time.sleep(1)
            print(f"{j.i} - {j.r}")
            s += j.r

        print(s / len(self.bb.arr_1))
        s = 0
        for j in self.bb.arr_2:
            time.sleep(0.5)
            print(f"{j.i} - {j.r}")
            s += j.r

        print(s / len(self.bb.arr_2))
     
        

g = Game()