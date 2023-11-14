import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.label1 = tk.Label(self.master, text="プログラミング言語を\n 一つ選択してください", padx=50)
        self.label1.pack()

        self.select_var = tk.IntVar()
        self.select_var.set(1)

        self.languages = [("Python", 1), ("Java", 2), ("Ruby", 3), ("C#", 4), ("JavaScript", 5)]

        def showchoice():
            for lang, num in self.languages:
                if num == self.select_var.get():
                    self.label2_text.set(lang + "が選択されました。")
                    self.answer = lang
                    break

        for lang, num in self.languages:
            self.radio1 = tk.Radiobutton(self.master, text=lang, variable=self.select_var, value=num,
                                         command=showchoice)
            self.radio1.pack(anchor=tk.W)

        self.label2_text = tk.StringVar()
        self.label2_text.set("言語を選択してください")

        self.label2 = tk.Label(self.master, textvariable=self.label2_text)
        self.label2.pack()

        self.answer = "言語が選択されていません"

        self.button1 = tk.Button(self.master, text="OK!", command=self.button1_clicked, padx=20, pady=10)
        self.button1.pack()

    def button1_clicked(self):
        if self.answer == "言語が選択されていません":
            self.label2_text.set(self.answer)
        else:
            print(self.answer)
            app.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
