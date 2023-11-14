import tkinter as tk


class Frame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.title("ウィンドウのタイトル")
        master.geometry("400x300")

        self.config(bg="whitesmoke")
        self.propagate(False)

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.label1 = tk.Label(self.master, text="これはラベルです")
        self.label1.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.insert(tk.END, "これはエントリーです")
        self.entry1.pack()

        button1 = tk.Button(self.master, text="これはボタンです ")
        button1.pack()


if __name__ == "__main__":
    root = tk.Tk()
    f1 = Frame1(master=root)
    f1.mainloop()
