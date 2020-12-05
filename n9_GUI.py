import time
from tkinter import *
from tkinter import messagebox
from n9 import N9


class Application:

    def __init__(self, master=None):

        self.master = master
        self.set_window()
        self.create_default_widgets()
        self.create_menu()

    def set_window(self):

        self.master.title('N9')
        self.master.resizable(True, True)

        w = 800
        h = 600
        ws = self.master.winfo_screenwidth()
        wh = self.master.winfo_screenheight()

        x = ws // 2 - w // 2
        y = wh // 2 - h // 2

        self.master.geometry(f'{w}x{h}+{x}+{y}')

    def create_default_widgets(self):

        self.key_label = Label(self.master, text="Ключ ", font="Tahoma 20")
        self.key_label.grid(row=0, column=0)

        self.input_label = Label(self.master, text="Текст", font="Tahoma 14")
        self.input_label.place(relx=0.2, rely=0.07)

        self.output_label = Label(self.master, text="Вывод", font="Tahoma 14")
        self.output_label.place(relx=0.7, rely=0.07)

        self.encode_btn = Button(self.master, text='Кодировать', bd=2, bg="#fcc", command=self.encode)
        self.encode_btn.grid(row=0, column=2)

        self.decode_btn = Button(self.master, text='Раскодировать', bd=2, bg="#fcc", command=self.decode)
        self.decode_btn.grid(row=0, column=3)

        self.clear_btn = Button(self.master, text='Очистить', bd=2, bg='#fcc', command=self.clear)
        self.clear_btn.grid(row=0, column=4)

        self.transform_btn = Button(self.master, bd=2, text='⇄', bg='#fcc', command=self.transform)
        self.transform_btn.grid(row=0, column=5)

        self.paste_btn = Button(self.master, text='📋', fg='#1E90FF', font='10', command=self.paste_input)
        self.paste_btn.place(relx=0.01, rely=0.06)

        self.clear_input = Button(self.master, font='10', text='X', fg='#f00', command=self.clear_input)
        self.clear_input.place(relx=0.05, rely=0.06)

        self.copy_output_btn = Button(self.master, text='📄', fg='#1E90FF', font='10', command=self.copy_output)
        self.copy_output_btn.place(relx=0.5, rely=0.06)

        self.clear_output_btn = Button(self.master, text='X', fg='#f00', font='10', command=self.clear_output)
        self.clear_output_btn.place(relx=0.54, rely=0.06)

        self.key_entry = Entry(self.master, bd=1, font="Tahoma 12", bg='#bcd', width=35)
        self.key_entry.bind('<Button-3>', self.show_text_menu)
        self.key_entry.grid(row=0, column=1)

        self.input_text = Text(self.master, bd=1.2, bg='white', width=42, height=27, font='Tahoma 12')
        self.input_text.bind('<Button-3>', self.show_text_menu)

        self.scrollbar = Scrollbar(self.master, command=self.input_text.yview, orient=VERTICAL)

        self.input_text['yscrollcommand'] = self.scrollbar.set
        self.input_text.place(relx=0.00325, rely=0.125)

        self.output_text = Text(self.master, bd=1.2, bg='white', width=42, height=27, font='Tahoma 12')
        self.output_text.bind('<Button-3>', self.show_text_menu)

        self.scrollbar2 = Scrollbar(root, command=self.output_text.yview, orient=VERTICAL)

        self.output_text['yscrollcommand'] = self.scrollbar2.set
        self.output_text.place(relx=0.5, rely=0.125)

        self.scrollbar.place(in_=self.input_text, relx=1.0, relheight=1.0, bordermode="outside")
        self.scrollbar2.place(in_=self.output_text, relx=1.0, relheight=1.0, bordermode="outside")

    def create_menu(self):

        self.top_menu = Menu(self.master)
        self.master.config(menu=self.top_menu)

        self.deep_menu = Menu(self.master, tearoff=0)
        self.deep_menu.add_command(label="Глубокое кодирование", command=self.deep_encode)
        self.deep_menu.add_command(label="Глубокое раскодирование", command=self.deep_decode)
        self.deep_menu.add_separator()
        self.deep_menu.add_command(label="Файл", command=self.file_encode)
        self.deep_menu.add_command(label="История", command=self.history)

        self.text_menu = Menu(self.master, tearoff=0)
        self.text_menu.add_command(label="Вставить", command=self.text_menu_paste)
        self.text_menu.add_command(label="Копировать", command=self.text_menu_copy)
        self.text_menu.add_command(label="Вырезать", command=self.text_menu_cut)
        self.text_menu.add_command(label="Удалить", command=self.text_menu_delete)

        self.top_menu.add_cascade(label='Прочее', menu=self.deep_menu)

    def encode(self):
        text = self.input_text.get('1.0', END).strip()
        key = self.key_entry.get().strip()
        try:
            encoded_text = N9.encode(text, key)
            self.output_text.delete('1.0', END)
            self.output_text.insert('1.0', encoded_text)

        except:
            error = 'Bad key or bad encoded text. Try again'
            self.output_text.delete('1.0', END)
            self.output_text.insert('1.0', error)

    def decode(self):
        text = self.input_text.get('1.0', END).strip()
        key = self.key_entry.get().strip()
        try:
            decoded_text = N9.decode(text, key)
            self.output_text.delete('1.0', END)
            self.output_text.insert('1.0', decoded_text)

        except:
            error = 'Bad key or bad encoded text. Try again'
            self.output_text.delete('1.0', END)
            self.output_text.insert('1.0', error)

    def clear(self):
        self.input_text.delete('1.0', END)
        self.output_text.delete('1.0', END)

    def transform(self):
        input_text = self.input_text.get('1.0', END)
        output_text = self.output_text.get('1.0', END)

        self.input_text.delete('1.0', END)
        self.output_text.delete('1.0', END)

        self.input_text.insert('1.0', output_text)
        self.output_text.insert('1.0', input_text)

    def paste_input(self):
        try:
            text = self.master.clipboard_get()
            self.input_text.delete('1.0', END)
            self.input_text.insert('1.0', text)

        except:
            pass

    def clear_input(self):
        self.input_text.delete('1.0', END)

    def clear_output(self):
        self.output_text.delete('1.0', END)

    def copy_output(self):
        text = self.output_text.get('1.0', END)
        self.master.clipboard_clear()
        self.master.clipboard_append(text)

    def show_text_menu(self, event):
        self.text_menu.post(event.x_root, event.y_root)

    def text_menu_delete(self):
        try:
            widget = self.master.focus_get()
            widget.delete('sel.first', 'sel.last')
        except:
            pass

    def text_menu_copy(self):
        try:
            widget = self.master.focus_get()
            self.master.clipboard_clear()
            self.master.clipboard_append(widget.selection_get())
        except:
            pass

    def text_menu_cut(self):
        try:
            widget = self.master.focus_get()
            self.master.clipboard_clear()
            self.master.clipboard_append(widget.selection_get())

            widget.delete('1.0', END)
        except:
            pass

    def text_menu_paste(self):
        try:
            widget = self.master.focus_get()
            if 'entry' in str(widget):
                widget.insert(0, self.master.clipboard_get())
            else:
                widget.insert('1.0', self.master.clipboard_get())
        except:
            pass

    def deep_encode(self):
        self.deep_encode = Tk()
        self.create_window(self.deep_encode, '')

        self.label_encode = Label(self.deep_encode, text="Уровень ", font="Tahoma 11")
        self.label_encode.grid(row=0, column=0)

        self.entry_encode = Entry(self.deep_encode, bd=1, font="Tahoma 11", width=10)
        self.entry_encode.grid(row=0, column=1)

        self.button_encode = Button(self.deep_encode, text='Раскодировать', bd=2, command=self.start_deep_encode)
        self.button_encode.place(relx=0.36, rely=0.45)

        self.deep_encode.mainloop()

    def deep_decode(self):
        self.deep_decode = Tk()
        self.create_window(self.deep_decode, '')

        self.label_decode = Label(self.deep_decode, text="Уровень ", font="Tahoma 11")
        self.label_decode.grid(row=0, column=0)

        self.entry_decode = Entry(self.deep_decode, bd=1, font="Tahoma 11", width=10)
        self.entry_decode.grid(row=0, column=1)

        self.button_decode = Button(self.deep_decode, text='Раскодировать', bd=2, command=self.start_deep_decode)
        self.button_decode.place(relx=0.36, rely=0.45)

        self.deep_decode.mainloop()

    def start_deep_encode(self):
        N = self.entry_encode.get()
        if N.isdigit():
            if int(N) > 1_000_000:
                messagebox.showwarning('Ошибка', 'Максимальное число 1 000 000')
                self.deep_encode.deiconify()

            else:
                try:
                    key = self.key_entry.get()
                    text = self.input_text.get('1.0', END).strip()

                    message = N9.encode(text, key, int(N))

                    self.output_text.delete('1.0', END)
                    self.output_text.insert('1.0', message)
                except:
                    messagebox.showwarning('Ошибка', 'Пустой ключ или пустой текст!')
                    self.deep_encode.deiconify()

        else:
            messagebox.showwarning('Ошибка', 'Вы должны ввести число')
            self.deep_encode.deiconify()

    def start_deep_decode(self):
        N = self.entry_decode.get()
        if N.isdigit():
            if int(N) > 1_000_000:
                messagebox.showwarning('Ошибка', 'Максимальное число 1 000 000')
                self.deep_decode.deiconify()

            else:
                #try:
                    key = self.key_entry.get()
                    text = self.input_text.get('1.0', END).strip()

                    message = N9.decode(text, key, int(N))

                    self.output_text.delete('1.0', END)
                    self.output_text.insert('1.0', message)

                #except:
                    #messagebox.showwarning('Ошибка', 'Пустой ключ или пустой текст!')
                    #self.deep_decode.deiconify()

        else:
            messagebox.showwarning('Ошибка', 'Вы должны ввести число')
            self.deep_encode.deiconify()

    def file_encode(self):
        pass

    def history(self):
        pass

    def create_window(self, window, title):
        window.title(title)
        window.resizable(False, False)

        w = 180
        h = 60
        ws = window.winfo_screenwidth()
        wh = window.winfo_screenheight()

        x = ws // 2 - w // 2
        y = wh // 2 - h // 2

        window.geometry(f'{w}x{h}+{x}+{y}')

    def closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try: self.deep_encode.destroy()
            except: pass

            try: self.deep_decode.destroy()
            except: pass

            self.master.destroy()

    def mainloop(self):
        self.master.protocol("WM_DELETE_WINDOW", self.closing)
        self.master.mainloop()


root = Tk()
app = Application(root)

if __name__ == '__main__':
    app.mainloop()
