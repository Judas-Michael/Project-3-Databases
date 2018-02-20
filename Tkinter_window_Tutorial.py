
from tkinter import * #imports tkinter tools
 
window = Tk() #opens window
 
window.title("Welcome to LikeGeeks app") #prints something as title

 
lbl = Label(window, text="Hello") #prints within window
 
lbl.grid(column=0, row=0) #tells it where to print

lbl = Label(window, text="Hello", font=("Arial Bold", 50)) #changes font type and size

window.geometry('350x200') #default window size 

btn = Button(window, text="Click Me") #button initializer + text
 
btn.grid(column=1, row=0) #button placement

btn = Button(window, text="Click Me", bg="orange", fg="red") # button colours

txt = Entry(window,width=10) #editable text box

txt.focus() #sets the 'focus' or auto-active thing to the text box

txt = Entry(window,width=10, state='disabled') #disables the piece that's being referred


def clicked(): #behaves when buton is clicked
 
    res = "Welcome to " + txt.get() #gets text from txt entry
 
    lbl.configure(text= res) #assigns label text

def clicked(): #behaves if button has been clicked
 
    lbl.configure(text="Button was clicked !!")
	
combo = Combobox(window) #makes a drop down menu available to choose from 
 
combo['values']= (1, 2, 3, 4, 5, "Text") #establishes options you can choose
 
combo.current(1) #set the selected item
 
combo.grid(column=0, row=0) #sets location

chk = Checkbutton(window, text='Choose'var=chk_state) #sets checkbox ##also can be set to already being checked

chk_state = IntVar() #assigns variable for check state
 
chk_state.set(0) #uncheck
 
chk_state.set(1) #check

rad1 = Radiobutton(window,text='First', value=1) #sets button
 
rad2 = Radiobutton(window,text='Second', value=2) #sets button
 
rad3 = Radiobutton(window,text='Third', value=3) #sets buton
 
rad1.grid(column=0, row=0) #sets button location
 
rad2.grid(column=1, row=0)
 
rad3.grid(column=2, row=0)
 
txt = scrolledtext.ScrolledText(window,width=40,height=10) #sets scrolled text
 
txt.grid(column=0,row=0) #sets location 

txt.insert(INSERT,'You text goes here') #assigns text in scrolled text

txt.delete(1.0,END) #deletes text from 1 to the end

messagebox.showinfo('Message title','Message content') #message box pops up #showwarning and showerror can also be used
#other functions are askaquestion askyesno askyesnocancel askokcancel askretrycancel

spin = Spinbox(window, from_=0, to=100, width=5)#sets spin box can also use from_= and to=

bar = Progressbar(window, length=200) #sets progress bar
bar['value'] = 70 #sets value
style = ttk.Style()
 
style.theme_use('default')
 
style.configure("black.Horizontal.TProgressbar", background='black')
 # styles
 
 file = filedialog.askopenfilename() #opens file
 filetypes = (("Text files","*.txt"),("all files","*.*" #specifies file type
 dir = filedialog.askdirectory() #asks the directory
 from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
 #specifies file path

menu = Menu(window)
 
menu.add_command(label='File')
 
window.config(menu=menu)
#add menu and label
menu.add_cascade(label='File', menu=new_item) #add new items

new_item = Menu(menu, tearoff=0) #disables feature







 
window.mainloop() #keeps window open