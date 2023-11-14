import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widget()

    def create_widget(self):

        self.label1 = tk.Label(self.master, text="「スイッチ」を押させるなーーーーッ")
        self.label1.pack()

        self.button1 = tk.Button(self.master, text="いいや！限界だ押すね！", command=self.button1_clicked)
        self.button1.pack()

    def button1_clicked(self):
        self.label1["text"] = "シュゴォーーーーーーーッ"
        self.after(1000, self.button1_after1)

    def button1_after1(self):
        self.label1["text"] = "ゴッ"
        self.after(1000, self.button1_after2)

    def button1_after2(self):
        self.label1["text"] = "オオオオオ"
        self.after(1000, self.button1_after3)

    def button1_after3(self):
        self.label1["text"] ="戻れたぞ……フフフ"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
