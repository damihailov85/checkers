import figure as f


class Board():

    arr_1 = list()
    arr_2 = list()

    def __init__(self):
        self.draw_board()

    def draw_board(self):
        print("draw board")
        self.add_figure()
    
    def add_figure(self):
        for i in range(10):
            self.arr_1.append(f.Figure(i))
            self.arr_2.append(f.Figure(i))
        print(f"добавлено {len(self.arr_1) + len(self.arr_2)} элементов")

