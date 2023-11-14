import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")
        self.master.geometry("400x300")

        self.name_var = tk.StringVar(value="山田太郎")
        self.age_var = tk.IntVar(value=20)
        self.agreement_var = tk.BooleanVar(value=False)

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.name = tk.Entry(self, textvariable=self.name_var)
        self.name.pack()

        self.age = tk.Entry(self, textvariable=self.age_var)
        self.age.pack()

        self.agreement = tk.Checkbutton(self, text="同意します", variable=self.agreement_var)
        self.agreement.pack()

        self.buttonframe = tk.Frame(self.master)
        self.buttonframe.pack()

        self.sample = tk.Button(self.buttonframe, text="入力例を表示", command=self.inputSampleValue)
        self.sample.pack(side="left")

        self.verify = tk.Button(self.buttonframe, text="入力内容を確認", command=self.outputValue)
        self.verify.pack(side="left")

    def inputSampleValue(self):
        self.name_var.set("鈴木一郎")
        self.age_var.set(41)
        self.agreement_var.set(False)

    def outputValue(self):
        print("氏名:", self.name_var.get())
        print("年齢:", self.age_var.get())
        print("同意:", self.agreement_var.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
