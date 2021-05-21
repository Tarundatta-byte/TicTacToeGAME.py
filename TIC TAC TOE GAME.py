from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title('TIC TAC TOE')

def disable_all():
    b1.config(state='disable')
    b2.config(state='disable')
    b3.config(state='disable')
    b4.config(state='disable')
    b5.config(state='disable')
    b6.config(state='disable')
    b7.config(state='disable')
    b8.config(state='disable')
    b9.config(state='disable')

def check_win():
    global winner
    winner = False

    if b1['text'] + b2['text'] + b3['text'] == 'XXX':
        b1.config(bg = 'blue')
        b2.config(bg = 'red')
        b3.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b4['text'] + b5['text'] + b6['text'] == 'XXX':
        b4.config(bg = 'green')
        b5.config(bg = 'red')
        b6.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()


    if b7['text'] + b8['text'] + b9['text'] == 'XXX':
        b7.config(bg = 'green')
        b8.config(bg = 'red')
        b9.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b1['text'] + b4['text'] + b7['text'] == 'XXX':
        b1.config(bg = 'green')
        b4.config(bg = 'red')
        b7.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b2['text'] + b5['text'] + b8['text'] == 'XXX':
        b2.config(bg = 'green')
        b5.config(bg = 'red')
        b8.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b3['text'] + b6['text'] + b9['text'] == 'XXX':
            b3.config(bg='green')
            b6.config(bg='red')
            b9.config(bg='green')
            winner = True
            messagebox.showinfo('TIC TAC TOE', 'X wins')
            disable_all()

    if b1['text'] + b5['text'] + b9['text'] == 'XXX':
        b1.config(bg = 'green')
        b5.config(bg = 'red')
        b9.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b3['text'] + b5['text'] + b7['text'] == 'XXX':
        b3.config(bg = 'green')
        b5.config(bg = 'red')
        b7.config(bg = 'green')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()
    if b1['text'] + b2['text'] + b3['text'] == 'OOO':
        b1.config(bg = 'yellow')
        b2.config(bg = 'blue')
        b3.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b4['text'] + b5['text'] + b6['text'] == 'OOO':
        b4.config(bg = 'yellow')
        b5.config(bg = 'blue')
        b6.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b7['text'] + b8['text'] + b9['text'] == 'OOO':
        b7.config(bg = 'yellow')
        b8.config(bg = 'blue')
        b9.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b1['text'] + b4['text'] + b7['text'] == 'OOO':
        b1.config(bg = 'yellow')
        b4.config(bg = 'blue')
        b7.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b2['text'] + b5['text'] + b8['text'] == 'OOO':
        b2.config(bg = 'yellow')
        b5.config(bg = 'blue')
        b8.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b3['text'] + b6['text'] + b9['text'] == 'OOO':
        b3.config(bg = 'yellow')
        b6.config(bg = 'blue')
        b9.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b1['text'] + b5['text'] + b9['text'] == 'OOO':
        b1.config(bg = 'yellow')
        b5.config(bg = 'blue')
        b9.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if b3['text'] + b5['text'] + b7['text'] == 'OOO':
        b3.config(bg = 'yellow')
        b5.config(bg = 'blue')
        b7.config(bg = 'yellow')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    if count == 9 and winner == False:
        messagebox.showinfo('TIC TAC TOE', 'ITS A TIE')
        disable_all()

def b_click(b):
    global count, clicked

    if b['text'] == '' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count = count +1
        check_win()
    elif b['text'] == '' and clicked == False:
          b['text'] = 'O'
          clicked = True
          count = count +1
          check_win()
    else:
     messagebox.showerror('TIC TAC TOE', 'ALREADY FILLED')

def reset():
  global count, clicked
  count = 0
  clicked = True

  global b1,b2,b3,b4,b5,b6,b7,b8,b9
  b1 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b1))
  b2 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b2))
  b3 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b3))

  b4 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b4))
  b5 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b5))
  b6 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b6))

  b7 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b7))
  b8 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b8))
  b9 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 3, width = 6,bg = 'white',command = lambda : b_click(b9))

  b1.grid(row=0,column=0)
  b2.grid(row=0,column=1)
  b3.grid(row=0,column=2)

  b4.grid(row=1,column=0)
  b5.grid(row=1,column=1)
  b6.grid(row=1,column=2)

  b7.grid(row=2,column=0)
  b8.grid(row=2,column=1)
  b9.grid(row=2,column=2)


rese_b = Button(screen, text = 'RESET',font = ('TIMES NEW ROMAN', 12),bg = 'white',command = reset)
rese_b.grid(row = 3,column = 1)
reset()

screen.mainloop()