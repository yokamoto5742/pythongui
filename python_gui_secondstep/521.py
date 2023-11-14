import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self, text="興味のある分野を選択してください", padx=50)
        self.label1.pack()

        class Checkbar(tk.Frame):
            def __init__(self, master=None, items=[], side=tk.LEFT, anchor=tk.W):
                super().__init__(master)

                self.vars = []

                for item in items:
                    select_var = tk.IntVar()
                    self.check = tk.Checkbutton(self, text=item, variable=select_var)
                    self.check.pack(anchor=tk.W, side=tk.LEFT)
                    self.vars.append(select_var)

            def state(self):
                return map((lambda var: var.get()), self.vars)

        self.items1 = ["プログラミング", "デザイン", "音楽", "映画", "スポーツ"]
        self.field_bar = Checkbar(self, items=self.items1)
        self.field_bar.pack(side=tk.TOP)
        self.field_bar.config(relief=tk.GROOVE, bd=2)

        self.items2 = ["Webアプリ", "スマホアプリ", "デスクトップアプリ"]
        self.product_bar = Checkbar(self, items=self.items2)
        self.product_bar.pack()

        def button1_clicked():
            answer1 = [item for item, state in zip(self.items1, self.field_bar.state()) if state]
            answer2 = [item for item, state in zip(self.items2, self.product_bar.state()) if state]

            print(answer1, answer2)

        self.button1 = tk.Button(self.master, text="確認", command=button1_clicked, padx=50)
        self.button1.pack()

        self.button2 = tk.Button(self.master, text="終了", command=root.quit, padx=50)
        self.button2.pack()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
