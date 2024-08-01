from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- JSON SEARCH ------------------------------- #

def search():
    website = box1.get().title()
    if website == '':
        messagebox.showinfo(title='Validation system',message=f'No website has been entered')
    else:
        try:
            with open('data.json','r') as file:
                data = json.load(file)
                email = data[website]['Email']
                password = data[website]['Password']
            
        except FileNotFoundError:
            messagebox.showinfo(title='Data search system',message=f'Data file not found')

        except KeyError:
            messagebox.showinfo(title='Data search system',message=f'You have not previously saved the email and password used for {website}')
            
        else:
            messagebox.showinfo(title='Data search system',message=f'Website: {website}\nEmail: {email}\n\nPassword: {password}')
    
# ------------------------- PASSWORD GENERATOR --------------------------- #

def passgen():
    box3.delete(0,END)

    letter = [choice(letters) for _ in range(randint(8, 10))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]

    passwordlst = letter+number+symbol
    shuffle(passwordlst)
    password = ''.join(passwordlst)

    box3.insert(0,password)
    
# -------------------------- SAVE PASSWORD ----------------------------- #
    
def save():
    
    website = box1.get().title()
    email = box2.get()
    password = box3.get()
    
    new = {
        website: {
            'Email': email,
            'Password': password
        }
    }

    if website == '' or password == '' or email == '':
        messagebox.showinfo(title='Validation system',message=f'Ensure all details are provided before submission.')
    else:
        check = messagebox.askokcancel(title='Confirmation system',message=f'Website: {website}\nEmail: {email}\n\nPassword: {password}\n\nAre these details OK to save?')

        if check:

            try:
                with open('data.json','r') as file:
                    data = json.load(file)
                    data.update(new)

            except FileNotFoundError:
                with open('data.json','w') as file:
                    json.dump(new, file, indent=4)

            else:
                with open('data.json','w') as file:
                    json.dump(data, file, indent=4)
            
            finally:
                box1.delete(0,END)
                box3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

s = Tk()
s.title('Password manager')
s.minsize(width=400, height=255)
s.config(padx=20, pady=50)

sub = Label(text="PASSWORD MANAGER\n",font=('Century gothic',18,'bold'))
sub.grid(row=0,column=0,columnspan=3)

c = Canvas(width=200,height=200)
img = PhotoImage('logo.png')
c.create_image(100,100,img)
c.grid(row=0,column=0,columnspan=3)

label1 = Label(text="Website:")
label1.grid(row=1,column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2,column=0)

label3 = Label(text="Password:")
label3.grid(row=3,column=0)

box1 = Entry(width=21)
box1.insert(END,string="")
box1.grid(row=1,column=1)
box1.focus()

buttons = Button(text="Search", command=search,width=14)
buttons.grid(row=1,column=2)

box2 = Entry(width=40)
box2.insert(END,string="contactsohankrishna@gmail.com")
box2.grid(row=2,column=1,columnspan=2)

box3 = Entry(width=21)
box3.insert(END,string="")
box3.grid(row=3,column=1)

button1 = Button(text="Generate Password", command=passgen)
button1.grid(row=3,column=2)

button2 = Button(text="Add", command=save,width=36)
button2.grid(row=4,column=1,columnspan=2)

s.mainloop()