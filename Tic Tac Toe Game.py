from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
root=Tk()
root.title("TIC TAC TOE GAME")
root.resizable(False, False)
label_frame = Frame(root)
label_frame.pack()
label = Label(label_frame, text = "Tic Tac Toe", background="red", font=('Arial', 30))
label.pack(pady=20)
button_frame= Frame(root)
button_frame.pack(padx=20, pady=50)
clicked=True
count=0
def disable_button():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
def checkifwon():
       global winner
       winner=False
       #checking X
       if b1["text"]=="X" and b2["text"]=="X" and b3["text"]== "X":
              b1.config(bg="green")
              b2.config(bg="green")
              b3.config(bg="green")
              winner=True
              turno.destroy()
              turnx.destroy()
              messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
              disable_button()
       elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]== "X":
              b4.config(bg="green")
              b5.config(bg="green")
              b6.config(bg="green")
              winner=True
              turno.destroy()
              turnx.destroy()
              messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X WINS")
              disable_button()
       elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]== "X":
                b7.config(bg="green")
                b8.config(bg="green")
                b9.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]== "X":
                b1.config(bg="green")
                b4.config(bg="green")
                b7.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]== "X":
                b2.config(bg="green")
                b5.config(bg="green")
                b8.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]== "X":
                b3.config(bg="green")
                b6.config(bg="green")
                b9.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]== "X":
                b1.config(bg="green")
                b5.config(bg="green")
                b9.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       elif b7["text"]=="X" and b5["text"]=="X" and b3["text"]== "X":
                b7.config(bg="green")
                b5.config(bg="green")
                b3.config(bg="green")
                winner=True
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! X WINS")
                disable_button()
       #checking O
       elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]== "O":
              b1.config(bg="green")
              b2.config(bg="green")
              b3.config(bh="green")
              winner=False
              turno.destroy()
              turnx.destroy()
              messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O WINS")
              disable_button()
       elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]== "O":
              b4.config(bg="green")
              b5.config(bg="green")
              b6.config(bg="green")
              winner=False
              turno.destroy()
              turnx.destroy()
              messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS!  WINS")
              disable_button()
       elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]== "O":
                b7.config(bg="green")
                b8.config(bg="green")
                b9.config(bg="green")
                winner=False
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O WINS")
                disable_button()
       elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]== "O":
                b1.config(bg="green")
                b4.config(bg="green")
                b7.config(bg="green")
                winner=False
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O WINS")
                disable_button()
       elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]== "O":
                b2.config(bg="green")
                b5.config(bg="green")
                b8.config(bg="green")
                winner=False
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O WINS")
                disable_button()
       elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]== "O":
                b3.config(bg="green")
                b6.config(bg="green")
                b9.config(bg="green")
                winner=False
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS! O WINS")
                disable_button()
       elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]== "O":
                b1.config(bg="green")
                b5.config(bg="green")
                b9.config(bg="green")
                winner=False
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O WINS")
                disable_button()
       elif b7["text"]=="O" and b5["text"]=="O" and b3["text"]== "O":
                b7.config(bg="green")
                b5.config(bg="green")
                b3.config(bg="green")
                winner=False
                turno.destroy()
                turnx.destroy()
                messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! O WINS")
                disable_button()
       
def click(b):
       global clicked, count, turnx, turno
       if b["text"]==" " and clicked == True:
              b["text"]="X"
              turnx=Label(label_frame, text="O's Turn", font=('Arial', 20, "bold",), fg='blue')
              turnx.pack()
              checkifwon()
              clicked=False
              turno.destroy()
              count+=1
       elif b["text"]==" " and clicked== False:
              b["text"]="O"
              turno=Label(label_frame, text="X's Turn", font=('Arial', 20, "bold"), fg='blue')
              turno.pack()
              checkifwon()
              clicked=True
              turnx.destroy()
              count+=1

b1=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5, command=lambda:click(b1))
b2=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b2))
b3=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b3))

b4=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b4))
b5=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b5))
b6=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7,borderwidth= 5,command=lambda:click(b6))

b7=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b7))
b8=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b8))
b9=Button(button_frame, text=" ", font=('Arial', 20), height=4, width=7, borderwidth= 5,command=lambda:click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
root.mainloop()                                     
