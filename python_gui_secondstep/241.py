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
        self.button1["text"] = "押したね！"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
