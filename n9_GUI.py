from tkinter import *
from tkinter import messagebox
from n9 import N9


def setwindow(root):
    root.title('N9')
    root.resizable(True, True)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = ws // 2 - w // 2
    y = wh // 2 - h // 2

    root.geometry(f'{w}x{h}+{x}+{y}')


def createwindow(window, title):
    window.title(title)
    window.resizable(False, False)

    w = 180
    h = 60
    ws = window.winfo_screenwidth()
    wh = window.winfo_screenheight()

    x = ws // 2 - w // 2
    y = wh // 2 - h // 2

    window.geometry(f'{w}x{h}+{x}+{y}')

def copy(event):
    try:
        root.clipboard_clear()
        root.clipboard_append(root.selection_get())
    except:
        pass

def insert_text2(message):
    text2.delete('1.0', END)
    text2.insert('1.0', message)


def paste_text():
    text.delete('1.0', END)
    text.insert('1.0', root.clipboard_get())


def clear():
    text.delete('1.0', END)
    text2.delete('1.0', END)


def get_text2():
    return text2.get('1.0', END).strip()


def get_text():
    return text.get('1.0', END).strip()


def get_key():
    return entry.get().strip()


def encode():
    try:
        text = get_text()
        key = get_key()
        encoded_text = N9.encode(text, key)

        text2.delete('1.0', END)
        text2.insert('1.0', encoded_text.strip())


    except:
        text2.delete('1.0', END)
        text2.insert('1.0', 'Bad key or bad encoded text. Try again')


def decode():
    try:
        text = get_text()
        key = get_key()
        decoded_text = N9.decode(text, key)

        text2.delete('1.0', END)
        text2.insert('1.0', decoded_text.strip())
    except:
        text2.delete('1.0', END)
        text2.insert('1.0', 'Bad key or bad encoded text. Try again')


def deep_encode():
    def start_deep_encode():
        n = entry_encode.get()
        if n.isdigit():
            if int(n) > 10:
                messagebox.showwarning('Ошибка', 'Максимальное число 10')
            else:
                n = int(n)
                key = get_key()
                message = get_text()
                while n != 0:
                    message = N9.encode(message, key)
                    n -= 1

                insert_text2(message)

        else:
            messagebox.showwarning('Ошибка', 'Вы должны ввести число')

    deep = Tk()
    createwindow(deep, '')

    label_encode = Label(deep, text="Уровень ", font="Tahoma 11")
    label_encode.grid(row=0, column=0)

    entry_encode = Entry(deep, bd=1, font="Tahoma 11", width=10)
    entry_encode.grid(row=0, column=1)

    button_decode = Button(deep, text='Кодировать', bd=2, command=start_deep_encode)
    button_decode.place(relx=0.4, rely=0.45)

def deep_decode():
    def start_deep_decode():
        n = entry_decode.get()
        if n.isdigit():
            if int(n) > 10:
                messagebox.showwarning('Ошибка', 'Максимальное число 10')
            else:
                n = int(n)
                key = get_key()
                message = get_text()
                while n != 0:
                    message = N9.decode(message, key)
                    n -= 1

                insert_text2(message)

        else:
            messagebox.showwarning('Ошибка', 'Вы должны ввести число')


    deep = Tk()
    createwindow(deep, '')

    label_decode = Label(deep, text="Уровень ", font="Tahoma 11")
    label_decode.grid(row=0, column=0)

    entry_decode = Entry(deep, bd=1, font="Tahoma 11", width=10)
    entry_decode.grid(row=0, column=1)

    button_decode = Button(deep, text='Раскодировать', bd=2, command=start_deep_decode)
    button_decode.place(relx=0.36, rely=0.45)


root = Tk()
setwindow(root)

mainmenu = Menu(root)

root.config(menu=mainmenu)

label1 = Label(root, text="Ключ ", font="Tahoma 20")
label1.grid(row=0, column=0)

label2 = Label(root, text="Текст", font="Tahoma 14")
label2.place(relx=0.2, rely=0.07)

label3 = Label(root, text="Вывод", font="Tahoma 14")
label3.place(relx=0.7, rely=0.07)

button = Button(root, text='Кодировать', bd=2, bg="#fcc", command=encode)
button.grid(row=0, column=2)

button2 = Button(root, text='Раскодировать', bd=2, bg="#fcc", command=decode)
button2.grid(row=0, column=3)

button3 = Button(root, text='Очистить', bd=2, bg='#fcc', command=clear)
button3.grid(row=0, column=4)

button4 = Button(root, text='📋', fg='#1E90FF', font='10', command=paste_text)
button4.place(relx=0.01, rely=0.06)

entry = Entry(root, bd=1, font="Tahoma 12", bg='#bcd', width=30)
entry.grid(row=0, column=1)

text = Text(root, bd=1.2, bg='white', width=42, height=27, font='Tahoma 12')
scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set
text.place(relx=0.00325, rely=0.125)

text2 = Text(root, bd=1.2, bg='white', width=42, height=27, font='Tahoma 12')
scrollbar2 = Scrollbar(root, command=text2.yview, orient=VERTICAL)

text2['yscrollcommand'] = scrollbar2.set
text2.place(relx=0.5, rely=0.125)

scrollbar.place(in_=text, relx=1.0, relheight=1.0, bordermode="outside")
scrollbar2.place(in_=text2, relx=1.0, relheight=1.0, bordermode="outside")

deep = Menu(root, tearoff=0)
deep.add_command(label="Глубокое кодирование", command=deep_encode)
deep.add_command(label="Глубокое раскодирование", command=deep_decode)

mainmenu.add_cascade(label='Прочее', menu=deep)

root.bind('<Control-c>', copy)
root.bind('<Control-C>', copy)

if __name__ == '__main__':
    root.mainloop()