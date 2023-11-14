import tkinter as tk
import time

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.title("ストップウォッチ")
        master.geometry("400x160")

        self.startTime = 0.0
        self.elapsedTime = 0.0
        self.running = False

        self.pack()
        self.create_widget()

    def create_widget(self):
        self.canvas = tk.Canvas(self.master, width=380, height=80, bg="lightgreen")
        self.canvas.place(x=10, y=10)

        self.timeText = self.canvas.create_text(380, 40, text="0.0", font=("MSゴシック", 24, "bold"), anchor="e")

        startButton = tk.Button(self.master, text="スタート", font=("MSゴシック", 18), command=self.startButtonClicked)
        startButton.place(x=10, y=100)

        stopButton = tk.Button(self.master, text="ストップ", font=("MSゴシック", 18), command=self.stopButtonClicked)
        stopButton.place(x=140, y=100)

        resetButton = tk.Button(self.master, text="リセット", font=("MSゴシック", 18), command=self.resetButtonClicked)
        resetButton.place(x=270, y=100)

    def startButtonClicked(self):
        if not self.running:
            self.startTime = time.time() - self.elapsedTime
            self.running = True
            self.update_Time()

    def update_Time(self):
        if self.running:
            self.elapsedTime = time.time() - self.startTime
            self.canvas.itemconfig(self.timeText, text=f"{self.elapsedTime:.1f}")
            self.master.after(100, self.update_Time)

    def stopButtonClicked(self):
        self.running = False

    def resetButtonClicked(self):
        self.running = False
        self.elapsedTime = 0.0
        self.canvas.itemconfig(self.timeText, text="0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
