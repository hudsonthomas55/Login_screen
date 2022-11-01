from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Login screen")
window.minsize(width=500, height=500)

# Labels
label = Label(text="Please login below")
label.pack()



def button_click():
    user = username.get()
    passw = password.get()
    label.config(text=f"Your username is: {user}, and your password is: {passw}")


# Username box
username = Entry(width=15)
username.focus()
username.insert(END, "Username")
username.pack()
print(username.get())


# Password box
password = Entry(width=15)
password.insert(END, "Password")
password.pack()
print(password.get())


# Login button
button = Button(text="Login", command=button_click)
button.pack()


window.mainloop()
