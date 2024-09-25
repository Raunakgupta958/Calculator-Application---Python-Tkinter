from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input_info = entry.get()
    try:
        if input_info == "":
            popup = Tk()
            popup.resizable(0, 0)
            popup.geometry("150x100")
            popup.title("Alert")
            label = Label(popup, text="Enter valid values")
            label.pack(side="top", fill="x", pady=10)
            B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
            B1.pack()
        else:
            output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    except Exception as e:
        output = "Error"
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("150x100")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def quit_app(root):
    root.quit()


def cal():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    # Set bigger window size
    root.geometry("400x500")

    entry_font = font.Font(size=20)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=10, pady=10, activebackground=button_active_bg, font=entry_font)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=10, pady=10, activebackground=button_active_bg, font=entry_font)

    # Define buttons
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ]

    # Create number buttons dynamically
    for (text, row, col) in buttons:
        num_button(text=text, command=lambda val=text: get_input(entry, val)).grid(row=row, column=col, pady=5)

    # Operators and additional functions
    operators = [
        ('+', 4, 3), ('-', 3, 3), ('*', 2, 3), ('/', 1, 3),
        ('=', 5, 3), ('%', 1, 0), ('^', 5, 2), ('C', 1, 2)
    ]

    for (op, row, col) in operators:
        if op == "=":
            cal_button(text=op, command=lambda: calc(entry)).grid(row=row, column=col, pady=5)
        elif op == "C":
            Button(root, text=op, bg=other_button_bg, padx=20, pady=20,
                   command=lambda: clear(entry), activebackground=button_active_bg, font=entry_font).grid(row=row, column=col, pady=5)
        elif op == "%":
            Button(root, text=op, fg=text_fg, bg=cal_button_bg, padx=20, pady=20,
                   command=lambda: get_input(entry, '/100'), activebackground=button_active_bg, font=entry_font).grid(row=row, column=col, pady=5)
        else:
            cal_button(text=op, command=lambda val=op: get_input(entry, val)).grid(row=row, column=col, pady=5)

    # Backspace button
    Button(root, text='Del', bg=other_button_bg, padx=20, pady=20,
           command=lambda: backspace(entry), activebackground=button_active_bg, font=entry_font).grid(row=1, column=1, pady=5)

    Button(root, text='0', fg=text_fg, bg=num_button_bg, padx=10, pady=10,
           command=lambda: get_input(entry, '0')).grid(row=5, column=0, columnspan=2, sticky=N+S+E+W, pady=5)


    root.mainloop()


if __name__ == '__main__':
    cal()
