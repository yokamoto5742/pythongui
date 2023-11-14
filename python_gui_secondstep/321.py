import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.grid()
        self.create_widget()

    def create_widget(self):
        self.label1 = tk.Label(self.master, text="これはlabel1です", bg="lightskyblue", relief=tk.RIDGE, bd=2)
        self.label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

        self.label2 = tk.Label(self.master, text="label2です", bg="khaki", relief=tk.RIDGE, bd=2)
        self.label2.grid(row=1, column=0, padx=5, pady=5)

        self.label3 = tk.Label(self.master, text="これはlabel3だよーーーーーーーーーーーん", bg="yellowgreen",
                               relief=tk.RIDGE, bd=2)
        self.label3.grid(row=1, column=1, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
