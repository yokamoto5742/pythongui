import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.title("電卓アプリ")
        master.geometry("310x440")

        self.button_number = [
            ["B", "", "C", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]
        ]
        self.symbol = ["+", "-", "*", "/"]
        self.calc_str = ""

        self.pack()
        self.create_widget()
        self.create_button()

    def create_widget(self):

        self.calc_frame = tk.Frame(self.master, width=310, height=60, bg="lightgreen")
        self.calc_frame.propagate(False)
        self.calc_frame.pack(side=tk.TOP, padx=10, pady=20)

        self.calc_var = tk.StringVar()
        self.ans_var = tk.StringVar()

        self.calc_label = tk.Label(self.calc_frame, textvariable=self.calc_var, font=("遊ゴシック体", 15, "bold"))
        self.calc_label.pack(anchor=tk.E)

        self.ans_label = tk.Label(self.calc_frame, textvariable=self.ans_var, font=("遊ゴシック体", 20, "bold"))
        self.ans_label.pack(anchor=tk.E)

        self.button_frame = tk.Frame(self.master, width=300, height=360, bg="gray")
        self.button_frame.propagate(False)
        self.button_frame.pack(side=tk.TOP, padx=10, pady=10)

    def create_button(self):
        for y, row in enumerate(self.button_number):
            for x, num in enumerate(row):
                button = tk.Button(self.button_frame, text=num, font=("遊ゴシック体", 15, "bold"), width=5, height=2)
                button.grid(row=y, column=x)
                button.bind("<Button-1>", self.button_clicked)

    def button_clicked(self, event):
        check = event.widget["text"]

        if check == "C":
            self.calc_str = ""
            self.calc_var.set(self.calc_str)
            self.ans_var.set("")

        elif check == "B":
            self.calc_str = self.calc_str[:-1]
            self.calc_var.set(self.calc_str)

        elif check == "=":
            if self.calc_str != "":
                if self.calc_str[-1] in self.symbol:
                    self.calc_str = self.calc_str[:-1]

            res = "=" + str(eval(self.calc_str))
            self.calc_var.set(self.calc_str)
            self.ans_var.set(res)
            self.calc_str = str(eval(self.calc_str))

        elif check in self.symbol:
            if self.calc_str[-1:] not in self.symbol and self.calc_str != "":
                self.calc_str += check
                self.calc_var.set(self.calc_str)

            elif self.calc_str[-1:] in self.symbol:
                self.calc_str = self.calc_str[:-1] + check
                self.calc_var.set(self.calc_str)

        else:
            self.calc_str += check
            self.calc_var.set(self.calc_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
