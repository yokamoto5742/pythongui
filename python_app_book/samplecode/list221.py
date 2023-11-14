import tkinter as tk
import run_func

# ウィンドウの作成
root = tk.Tk()
# ウィンドウのサイズ指定
root.geometry("250x100")

run_button = tk.Button(root, text="Run", command=run_func.run_func)
run_button.place(x=110, y=30)

root.mainloop()
