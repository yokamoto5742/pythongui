import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_widget()

    def create_widget(self):
        msg = "うへっへへへうへへへへへ\n でへへェェうへへェェうヒィッ\n うひうひうひうはァッ\n でへっでへっどぅひひひひひ\n ふっふふはっひひお\n へおへおへへェェッ"

        self.label1 = tk.Label(self.master, text=msg, font=("MSゴシック", 20, "bold"), bg="pink", fg="black", relief="solid", bd=1, padx=10, pady=10)
        self.label1.pack(side="right")

        self.icon = tk.PhotoImage(file="img/denchan.png")
        self.label2 = tk.Label(self.master, image=self.icon, bg="black", relief="solid", bd=1, padx=10, pady=10)
        self.label2.pack(side="left")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
