from tkinter import Tk, Canvas, Frame, BOTH
import pawn

class Board(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Шашки")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)


        size = 80
        for i in range(8):
            for j in range(8):

                x = size + i * size
                y = size + j * size

                color = "#fff" if (i + j) % 2 == 0 else "#999"
                canvas.create_rectangle(
                    x, y, x + size, y + size,
                    outline="#000", fill = color
                )

        canvas.arr = list()
        for i in range(4):
            for j in range(8):
                if j < 3:
                    fill = "#000"
                elif j > 4:
                    fill = "#fff"
                else:
                    continue
                d = 2 if j % 2 == 0 else 1
                x = d * size + i * size * 2
                y = size + j * size
                tag = "p" + str(i * 4 + j)
                tag = "p"
                if tag == "p":
                    fill = "#f00"
                canvas.arr.append(canvas.create_oval(
                    x + 10, y + 10, x + size - 10, y + size - 10, outline="#000", 
                    fill = fill, width=3, tag = tag
                )  ) 

        
        #canvas.move(arr[0], 10, 10)

        canvas.pack(fill=BOTH, expand=1)
    



def main():
    root = Tk()
    ex = Board()
    root.geometry("800x800+1000+0")
    root.mainloop()


if __name__ == '__main__':
    main()