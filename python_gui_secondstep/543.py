import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("ウィンドウのタイトル")
        self.master.geometry("800x600")

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.canvas = tk.Canvas(self, width=800, height=700)
        self.canvas.pack()

        self.bg_img1 = tk.PhotoImage(file="bg_img1.png")
        self.bg_img2 = tk.PhotoImage(file="bg_img2.png")

        self.canvas.create_image(0, 0, image=self.bg_img1, tag="img1", anchor="nw")

        delete_button = tk.Button(self.master, text="画像消去", font=("MSゴシック", "20", "bold"),
                                  command=self.delete_img)
        delete_button.place(x=100, y=620)

        create_button1 = tk.Button(self.master, text="画像1を生成", font=("MSゴシック", "20", "bold"),
                                   command=self.create_img1)
        create_button1.place(x=300, y=620)

        create_button2 = tk.Button(self.master, text="画像2を生成", font=("MSゴシック", "20", "bold"),
                                   command=self.create_img2)
        create_button2.place(x=510, y=620)

    def delete_img(self):
        self.canvas.delete("img1", "img2")

    def create_img1(self):
        self.canvas.create_image(0, 0, image=self.bg_img1, tag="img1", anchor="nw")

    def create_img2(self):
        self.canvas.create_image(0, 0, image=self.bg_img2, tag="img2", anchor="nw")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
