import tkinter as tk
from tkinter import ttk, filedialog
import os
import shutil


class App:
    def __init__(self, root):
        self.cb = None
        self.extensions = None
        self.statusbar = None
        self.dir_path = ""  # インスタンス変数として初期化
        self.root = root
        self.create_widgets()

    def browse(self):
        self.dir_path = filedialog.askdirectory()
        self.statusbar["text"] = "フォルダを選択しました！" if self.dir_path else "フォルダ選択がキャンセルされました。"

    def run_func(self):
        try:
            if not self.dir_path:  # dir_pathが設定されていることを確認します。
                raise ValueError("フォルダが選択されていません。")
            save_path = filedialog.askdirectory()
            if not save_path:
                self.statusbar["text"] = "移動先フォルダが選択されていません。"
                return
            for file in os.listdir(self.dir_path):
                if file.endswith(self.cb.get()):
                    path = os.path.join(self.dir_path, file)
                    shutil.move(path, save_path)
            self.statusbar["text"] = "完了しました！"
        except Exception as e:  # 具体的な例外をキャッチして、デバッグを容易にします。
            self.statusbar["text"] = f"エラー: {e}"

    def create_widgets(self):
        self.statusbar = tk.Label(self.root, text="ここからスタート！", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        run_button = tk.Button(self.root, text="移動先フォルダ選択", command=self.run_func)
        run_button.pack(side=tk.BOTTOM, padx=20, pady=10)

        frame = ttk.LabelFrame(self.root, text="拡張子の選択", padding=10)
        frame.pack(padx=20, pady=5, side=tk.BOTTOM)

        self.extensions = [".docx", ".txt", ".py", ".xlsx", ".zip"]
        self.cb = ttk.Combobox(frame, values=self.extensions, state="readonly")
        self.cb.pack(side=tk.LEFT)
        self.cb.current(0)

        browse_button = tk.Button(frame, text="フォルダ選択", command=self.browse)
        browse_button.pack(side=tk.LEFT, padx=10)


root = tk.Tk()
app = App(root)
root.mainloop()
