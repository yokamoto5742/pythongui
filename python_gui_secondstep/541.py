import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")
        self.master.geometry("800x600")

        self.pack()
        self.create_widget()

    def create_widget(self):

        self.canvas = tk.Canvas(self, width=600, height=400, bg="gray")
        # 楕円
        self.canvas.create_oval(10, 10, 100, 100, width=10, fill="white")
        # 円弧
        self.canvas.create_arc(120, 120, 210, 210, width=5, fill="red")
        # 矩形
        self.canvas.create_rectangle(230, 10, 320, 100, width=5, fill="blue")
        # 多角形
        self.canvas.create_polygon(330, 10, 420, 10, 420, 100, 330, 100, width=5, fill="yellow")

        self.canvas.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
