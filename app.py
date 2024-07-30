import customtkinter


def button_callback():
    print("button pressed")


app = customtkinter.CTk()
app.title("My App")
app.geometry("1500x800")

button = customtkinter.CTkButton(app, text="Hello", command=button_callback())
button.grid(row=0, column=0, padx=20, pady=20)


app.mainloop()
