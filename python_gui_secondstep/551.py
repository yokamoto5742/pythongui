import tkinter as tk
from tkinter.filedialog import askopenfilename


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")

        self.pack()
        self.create_menu()
        self.create_widget()

    def create_menu(self):
        def NewFile():
            print("New File!")

        def OpenFile():
            file_name = askopenfilename()
            print(file_name)

        def About():
            print("このアプリは hogehoge なアプリです")

        self.menu_bar = tk.Menu(self)
        root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="新規作成", command=NewFile)
        self.file_menu.add_command(label="開く", command=OpenFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="終了", command=self.master.quit)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="ヘルプ", menu=self.help_menu)
        self.help_menu.add_command(label="このアプリについての情報を表示します", command=About)

    def create_widget(self):
        self.label = tk.Label(self, text="メニューバーを使ってみましょう", padx=100, pady=100)
        self.label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
