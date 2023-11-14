import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=200, height=150)

        self.master.title("ウィンドウのタイトル")
        self.pack()
        self.create_widget()

    def create_widget(self):
        frame1 = tk.Frame(self.master, relief=tk.RIDGE, bd=2)
        list1 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")]

        for text, color in list1:
            label = tk.Label(frame1, text=text, bg=color, font="20")
            label.pack(side=tk.LEFT, padx=5, pady=5)
        frame1.place(relx=0.1, rely=0.1)

        frame2 = tk.Frame(self.master, relief=tk.RIDGE, bd=2)
        list2 = [("A", "lightskyblue"), ("B", "khaki"), ("C", "yellowgreen"), ("D", "hotpink")]

        for i, (text, color) in enumerate(list2):
            label = tk.Label(frame2, text=text, bg=color, font="20")
            label.grid(row=i // 2, column=i % 2)
        frame2.place(relx=0.6, rely=0.5)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
