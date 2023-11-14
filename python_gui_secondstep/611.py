import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.msg = tk.StringVar()
        self.msg.set("")

        self.label1 = tk.Label(self, text="あなたが押したキーは:", font=("MSゴシック", "24", "bold"))
        self.label1.pack()

        self.label2 = tk.Label(self, textvariable=self.msg, font=("MSゴシック", "24", "bold"))
        self.label2.pack()

        self.master.bind("<Any-KeyPress>", self.print_keysym)

    def print_keysym(self, event):
        # イベントから押されたキーの名前を取得して表示
        self.msg.set(event.keysym)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
