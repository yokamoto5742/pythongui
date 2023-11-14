import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.elapse = 0
        self.after_id = 0

        self.pack()
        self.create_widget()

    def create_widget(self):

        self.label1 = tk.Label(self, text=str(self.elapse) + "秒経過しました", font=("MSゴシック", "24", "bold"))
        self.label1.pack()

    def update_time(self):
        self.elapse += 1
        self.label1["text"] = str(self.elapse) + "秒経過しました"
        self.after_id=app.after(1000, self.update_time)

        if self.elapse == 10:
            self.after_cancel(self.after_id)
            self.label1["text"] = "終了しました"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.update_time()
    app.mainloop()
