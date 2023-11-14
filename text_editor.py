import tkinter as tk
from tkinter import ttk
import configparser
from tkinter import filedialog
from tkinter import messagebox
import os


def sub_window():
    if os.path.exists('setting.ini'):
        config = configparser.ConfigParser()
        config.read('setting.ini', encoding='utf-8')

        def writing_func():
            with open('setting.ini', 'w', encoding='utf-8') as f:
                config.write(f)

        def reg_func():
            reg_phrase = reg_box.get()

            if radio_value.get() == 1:
                radio_1['text'] = reg_phrase
                config.set("Fixed Phrase", "phrase1", reg_phrase)
                writing_func()

            elif radio_value.get() == 2:
                radio_2['text'] = reg_phrase
                config.set("Fixed Phrase", "phrase2", reg_phrase)
                writing_func()

            elif radio_value.get() == 3:
                radio_3['text'] = reg_phrase
                config.set("Fixed Phrase", "phrase3", reg_phrase)
                writing_func()

            elif radio_value.get() == 4:
                radio_4['text'] = reg_phrase
                config.set("Fixed Phrase", "phrase4", reg_phrase)
                writing_func()

            elif radio_value.get() == 5:
                radio_5['text'] = reg_phrase
                config.set("Fixed Phrase", "phrase5", reg_phrase)
                writing_func()

        def insert_func():
            if radio_value.get() == 1:
                textbox.insert('insert', radio_1['text'])

            elif radio_value.get() == 2:
                textbox.insert('insert', radio_2['text'])

            elif radio_value.get() == 3:
                textbox.insert('insert', radio_3['text'])

            elif radio_value.get() == 4:
                textbox.insert('insert', radio_4['text'])

            elif radio_value.get() == 5:
                textbox.insert('insert', radio_5['text'])

        fp_window = tk.Toplevel(root)
        frame1 = ttk.LabelFrame(fp_window, text="登録", padding=10)
        frame1.pack(padx=20, pady=10)

        reg_label = tk.Label(frame1, text="定型文の編集:")
        reg_label.pack(side=tk.LEFT, anchor=tk.W)

        reg_box = tk.Entry(frame1, width=50)
        reg_box.pack(side=tk.LEFT)

        save_button = tk.Button(frame1, text="保存", command=reg_func)
        save_button.pack(side=tk.LEFT, padx=10)

        frame2 = ttk.LabelFrame(fp_window, text="定型文一覧", padding=10)
        frame2.pack(padx=20, pady=5, fill=tk.X)

        radio_value = tk.IntVar()
        read_base = config["Fixed Phrase"]
        radio_1 = ttk.Radiobutton(frame2, text=read_base.get("phrase1"), value=1, variable=radio_value)
        radio_1.pack(anchor=tk.W)
        radio_2 = ttk.Radiobutton(frame2, text=read_base.get("phrase2"), value=2, variable=radio_value)
        radio_2.pack(anchor=tk.W)
        radio_3 = ttk.Radiobutton(frame2, text=read_base.get("phrase3"), value=3, variable=radio_value)
        radio_3.pack(anchor=tk.W)
        radio_4 = ttk.Radiobutton(frame2, text=read_base.get("phrase4"), value=4, variable=radio_value)
        radio_4.pack(anchor=tk.W)
        radio_5 = ttk.Radiobutton(frame2, text=read_base.get("phrase5"), value=5, variable=radio_value)
        radio_5.pack(anchor=tk.W)

        set_button = tk.Button(fp_window, text='設定', command=insert_func)
        set_button.pack(padx=10, pady=10, ipady=5, fill=tk.X)

    else:
        messagebox.showerror('エラー', '設定ファイルが存在しません。')


def open_func():
    typ = [('テキストファイル', '*.txt'), ('すべてのファイル', '*')]
    txt_path = tk.filedialog.askopenfilename(filetypes=typ)

    if len(txt_path) != 0:
        textbox.delete('1.0', 'end')
        with open(txt_path, 'r', encoding='utf-8') as f:
            textbox.insert('1.end', f.read())


def save_func():
    typ = [('テキストファイル', '*.txt')]
    txt_path = tk.filedialog.asksaveasfilename(filetypes=typ, defaultextension='*.txt')

    if len(txt_path) != 0:
        with open(txt_path, 'w', encoding='utf-8') as f:
            data = textbox.get('1.0', 'end')
            f.write(data)


root = tk.Tk()

frame = ttk.Frame(root, padding=5)
frame.pack(padx=5, pady=5)
textbox = tk.Text(frame, width=60, height=20)

yscroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=textbox.yview)
textbox['yscrollcommand'] = yscroll.set
yscroll.pack(side=tk.RIGHT, fill=tk.Y)

textbox.pack(side='left', fill='both')

menubar = tk.Menu(root)
root.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(menu=file_menu, label='ファイル')
file_menu.add_command(label='開く', command=open_func)
file_menu.add_command(label='名前を付けて保存', command=save_func)
file_menu.add_separator()
file_menu.add_command(label='終了', command=root.quit)

help_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(menu=help_menu, label='ヘルプ')
help_menu.add_command(label='マニュアル')

fp_button = ttk.Button(root, text='定型文の修正', command=sub_window)
fp_button.pack(padx=10, pady=10, ipady=5, fill=tk.X)

root.mainloop()
