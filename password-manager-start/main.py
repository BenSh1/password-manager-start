
from tkinter import * # imporst all of the class
from tkinter import messagebox # another module of code 
import random
from random import choice, randint, shuffle
import pyperclip 
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
  
  password_entry.delete(0, END)

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  #nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = randint(2, 4)

  password_list = []

  #for char in range(nr_letters):
  #  password_list.append(random.choice(letters))

  # List Comprehension
  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

  #for char in range(nr_symbols):
  #  password_list += random.choice(symbols)

  # List Comprehension
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]


  #for char in range(nr_numbers):
  #  password_list += random.choice(numbers)

  # List Comprehension
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)


  #password = ""
  #for char in password_list:
  #  password += char
  password = "".join(password_list)

  #print(f"Your password is: {password}")
  password_entry.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email ,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
    #if website == "" or password == "":
        #is_empty = messagebox.showerror(title="Oops" , message="Please don't leave any fields empty")
        messagebox.showinfo(title="Oops" , message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details entered: " f"\nEmail: {email} \nPassword: {password}\nIs it ok to save?")

        if is_ok != True:
            print("Zxczxc")
            return 
        
        #if is_ok : 
            #data_file = open("data.txt", "a")
        try:
            with open("data.json", "r") as data_file :
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file : 
                #Saving updated data
                json.dump(new_data , data_file,indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file : 
                #Saving updated data
                json.dump(data , data_file,indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

            #data_file.write(website_entry.get() + " | " + user_entry.get()+" | " + password_entry.get() + "\n")    
            #data_file.write(f"{website} | {email} | {password}\n")    
            #data_file.close()

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file :
            #Reading old data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error" , message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website , message=f"Email:{email}\nPasswrod:{password}")
        else:
            messagebox.showerror(title="Error" , message=f"No Details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)


canvas = Canvas(width=200 , height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image=logo_img)
canvas.grid(column=1 , row=0)

#, font=(FONT_NAME  , 20,"bold")
#label
website_label = Label(text="Website:")
website_label.grid(column=0 , row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0 , row=2)

password_label = Label(text="Password:")
password_label.grid(column=0 , row=3)

#Entry
#website_entry = Entry(width=35 )
website_entry = Entry(width=32 )
website_entry.grid(column=1 , row=1)
website_entry.focus()

#user_entry = Entry(width=35 )
user_entry = Entry(width=50 )
user_entry.grid(column=1 , row=2 , columnspan=2)
user_entry.insert(0,"ben1364@gmail.com")


#password_entry = Entry(width=17)
password_entry = Entry(width=32)
password_entry.grid(column=1 , row=3 )

#Button
generate_button = Button(text="Generate Password"  , command=generate_password)
generate_button.grid(column=2 , row=3)

#Button
search_button = Button(text="Search" ,width=13 , command=find_password)
search_button.grid(column=2 , row=1)

#add_button = Button(text="Add"  , width=30 , command=save)
add_button = Button(text="Add"  , width=43 , command=save)
add_button.grid(column=1 , row=4 , columnspan = 2)



window.mainloop()





