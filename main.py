#importing all the essentials needed like a messagebox and other actions.
from tkinter import *
from tkinter import messagebox

#initialising the screen and title of the screen.
screen = Tk()
screen.title('TIC TAC TOE')

#iniialising the disable function for the keys.
# Once either x or o wins the game all the keys will be disabled by this function
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

#checks the winner throught check_win function.
def check_win():
    global winner
    winner = False

#You need to understand this before going to the logic section.
    # row 0: [1] [2] [3]
    # row 1: [4] [5] [6]
    # row 2: [7] [8] [9]
    #here we need to satisfy the condition  that
    #EITHER the SIDES --> [1][2][3] or [4][5][6] or [7][8][9] or
    # [1][4][7] or [2][5][8] or [3][6][9]
    # or the DIAGONALS [1][5][9] or [3][5][7] must be 'XXX' or 'YYY'
    # if the above condition fails, it must return a message "ITS A TIE" because no one has won the game.

#Here we write the main logic of the program.
    if b1['text'] + b2['text'] + b3['text'] == 'XXX':                                         #if[1][2][3]=='XXX'
        b1.config(bg = 'red')                                                          #change the button color to red.
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')                                         #pop a message "X Wins."
        disable_all()                                  # disable all the keys,because already 'X' won so no more moves.

    if b4['text'] + b5['text'] + b6['text'] == 'XXX':                                          #if[4][5][6]=='XXX'
        b4.config(bg = 'red')                                                           #change the button color to red
        b5.config(bg = 'red')
        b6.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')                                           #pop a message "X Wins."
        disable_all()                                  # disable all the keys,because already 'X' won so no more moves.

                                                                  #the same logic follows the rest.

    if b7['text'] + b8['text'] + b9['text'] == 'XXX':
        b7.config(bg = 'red')
        b8.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b1['text'] + b4['text'] + b7['text'] == 'XXX':
        b1.config(bg = 'red')
        b4.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b2['text'] + b5['text'] + b8['text'] == 'XXX':
        b2.config(bg = 'red')
        b5.config(bg = 'red')
        b8.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b3['text'] + b6['text'] + b9['text'] == 'XXX':
            b3.config(bg='red')
            b6.config(bg='red')
            b9.config(bg='red')
            winner = True
            messagebox.showinfo('TIC TAC TOE', 'X wins')
            disable_all()
    #here is the diagonal part it is also same as the above code.
    if b1['text'] + b5['text'] + b9['text'] == 'XXX':
        b1.config(bg = 'red')
        b5.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

    if b3['text'] + b5['text'] + b7['text'] == 'XXX':
        b3.config(bg = 'red')
        b5.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'X wins')
        disable_all()

  #here the same logic which we wrote for X also applies for O so we do the same process for O which we have done for X
    if b1['text'] + b2['text'] + b3['text'] == 'OOO':                       #checks the condition  if[1][2][3]=='OOO'
        b1.config(bg = 'blue')                                                      #change the button color to blue
        b2.config(bg = 'blue')
        b3.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')                                #pops out a message that 'O Wins'
        disable_all()                                    #since O has won,so we disable all the keys so no more moves.

    if b4['text'] + b5['text'] + b6['text'] == 'OOO':                         #again the same process continues here.
        b4.config(bg = 'blue')
        b5.config(bg = 'blue')
        b6.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b7['text'] + b8['text'] + b9['text'] == 'OOO':
        b7.config(bg = 'blue')
        b8.config(bg = 'blue')
        b9.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b1['text'] + b4['text'] + b7['text'] == 'OOO':
        b1.config(bg = 'blue')
        b4.config(bg = 'blue')
        b7.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b2['text'] + b5['text'] + b8['text'] == 'OOO':
        b2.config(bg = 'blue')
        b5.config(bg = 'blue')
        b8.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b3['text'] + b6['text'] + b9['text'] == 'OOO':
        b3.config(bg = 'blue')
        b6.config(bg = 'blue')
        b9.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
    #here comes the diagonal part for 'O' again the same process has been repeated.
    if b1['text'] + b5['text'] + b9['text'] == 'OOO':
        b1.config(bg = 'blue')
        b5.config(bg = 'blue')
        b9.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()

    if b3['text'] + b5['text'] + b7['text'] == 'OOO':
        b3.config(bg = 'blue')
        b5.config(bg = 'blue')
        b7.config(bg = 'blue')
        winner = True
        messagebox.showinfo('TIC TAC TOE', 'O wins')
        disable_all()
 #here is the logic IF its a tie between both the players.
    if count == 9 and winner == False: #this states that if all the keys are filled with 'X's & 'O's but no one has won.
        #then there is no winner.
        messagebox.showinfo('TIC TAC TOE', 'ITS A TIE') #pops out a message showing "ITS A TIE."
        disable_all() #we are disabling all the keys since its a tie.

#we are defining a function for, if the button is clicked then which text is to be displayed.
def b_click(b):
    global count, clicked

    if b['text'] == '' and clicked == True:#if you click any button and its empty then,
        b['text'] = 'X' # text on button will be X'
        clicked = False #if button is not clicked
        count = count +1 #then increment the count value.
        check_win()                   #calling the function to check whether there is any winner after this move.
    elif b['text'] == '' and clicked == False: #if a button is empty and from above clicke is false
          b['text'] = 'O' #then text on button will be O
          clicked = True
          count = count +1
          check_win()#calling the function to check whether there is any winner after this move.
    else:
     messagebox.showerror('TIC TAC TOE', 'ALREADY FILLED') #this pop up occurs only when you press any button which is already filled.

#here we are initialising a reset function to reset to a fresh screen.
def reset():
  global count, clicked
  count = 0
  clicked = True #if the button is clicked then it clears all the 'X' & 'O' in buttons.

  global b1,b2,b3,b4,b5,b6,b7,b8,b9 #DECLARING variables for buttons.
  #Initialising buttons on screen with font, button height & width, button color, and the command once the button is clicked.
  b1 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b1))
  b2 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b2))
  b3 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b3))

  b4 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b4))
  b5 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b5))
  b6 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b6))

  b7 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b7))
  b8 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b8))
  b9 = Button(screen, text = '',font = ('TIMES NEW ROMAN', 20),height = 4, width = 6,bg = 'light green',command = lambda : b_click(b9))

  #displaying the buttons on a grid view.
  b1.grid(row=0,column=0) # row 0: [1]
  b2.grid(row=0,column=1) # row 0: [2]
  b3.grid(row=0,column=2) # row 0: [3]

  b4.grid(row=1,column=0)# row 1: [4]
  b5.grid(row=1,column=1)# row 1: [5]
  b6.grid(row=1,column=2)# row 1: [6]

  b7.grid(row=2,column=0)# row 2: [7]
  b8.grid(row=2,column=1)# row 2: [8]
  b9.grid(row=2,column=2)# row 2: [9]

#Initialising the RESET button on screen with text as RESET,font,button color,and the command to process when clicked
rese_b = Button(screen, text = 'RESET',font = ('TIMES NEW ROMAN', 12),bg = 'white',command = reset)
rese_b.grid(row = 3,column = 1)
reset()

screen.mainloop()