from generate import GeneratePassword
import customtkinter as ctk

app = ctk.CTk()
gp = GeneratePassword()

class main():
    def __init__(self) -> None:
        app.title("Generate Password")
        app.geometry("250x400")
        label = ctk.CTkLabel(master=app, text="Click the button to generate a password")
        button_generate = ctk.CTkButton(master=app, text="Generate", command=lambda: gp.generate(output_text))
        output_text = ctk.CTkTextbox(master=app, width=150, height=300)
        label.pack()
        button_generate.pack(pady=10)
        output_text.pack(pady=10)

init = main()
app.mainloop()