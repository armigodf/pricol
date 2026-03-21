import tkinter
import random

number_of_symbol = int(input('на сколько символов вы хотите пароль? '))


def generate(number_of_symbols=6):
    import random
    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)


window = tkinter.Tk()
window.config(background='green')
window.title('ГЕНЕРАТОР')
window.geometry('900x600')

text = tkinter.Text(
    font=('Times New Roman', 20, 'bold'),
    height=10,
    width=number_of_symbol + 1,
    bg='yellow',
    fg='red',
    borderwidth=15
)
text.pack(expand=1)

tkinter.Button(
    text='Сгенерировать пароль',
    font=('Times New Roman', 20, 'bold'),
    bg='yellow',
    fg='red',
    borderwidth=15,
    command=lambda: generate(number_of_symbol)
).pack(expand=1)

window.mainloop()
