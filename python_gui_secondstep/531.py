import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widget1()

    def create_widget1(self):

        self.label1 = tk.Label(self.master, text="ユーザー情報を入力してください", padx=50)
        self.label1.pack(padx=5, pady=5)

        items = ["氏名", "生年月日", "電話番号", "メールアドレス"]

        def fetch(entries):
            for entry in entries:
                item = entry[0]
                text = entry[1].get()
                print('{}: {}'.format(item, text))

        def makeform(self, items):
            entries = []
            for item in items:
                row = tk.Frame(self.master)
                label = tk.Label(row, text=item)
                entry = tk.Entry(row)

                row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                label.pack(side=tk.LEFT)
                entry.pack(side=tk.RIGHT, fill=tk.X)
                entries.append((item, entry))

            return entries

        ents = makeform(self, items)

        self.button1 = tk.Button(self.master, text="確認", command=(lambda e=ents: fetch(e)))
        self.button1.pack(side=tk.LEFT, padx=5, pady=5)

        self.button2 = tk.Button(self.master, text="終了", command=self.master.quit)
        self.button2.pack(side=tk.LEFT, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
