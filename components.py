import customtkinter as ctk

# Création d'une frame personnalisée
class Component(ctk.CTkFrame):
    def __init__(self, text, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.pack()

        self.button = ctk.CTkButton(self, text="Button")
        self.button.configure(command=self.on_button_click)
        self.button.pack(side="bottom", pady=20)

    def on_button_click(self):
        print("Button clicked")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("400x300")

        self.content = ctk.CTkFrame(self)
        self.content.configure(fg_color="light blue")
        self.content.pack(fill="both", padx=20, pady=20, expand=True)
        self.content.pack_propagate(0) # Prevent the frame from resizing to fit its contents

        # Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.configure(fg_color="transparent")
        self.buttons_frame.pack(side="bottom", fill="x", expand=True)
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        self.button1 = ctk.CTkButton(self.buttons_frame, text="Button 1")
        self.button1.configure(command=self.on_button1_click)
        self.button1.grid(row=0, column=0)

        self.button2 = ctk.CTkButton(self.buttons_frame, text="Button 2")
        self.button2.configure(command=self.on_button2_click)
        self.button2.grid(row=0, column=1)

    def on_button1_click(self):
        for w in self.content.winfo_children():
            w.destroy()

        component = Component("Component 1", self.content)
        component.pack(fill="both", expand=True)

    def on_button2_click(self):
        for w in self.content.winfo_children():
            w.destroy()

        component = Component("Component 2", self.content)
        component.pack(fill="both", expand=True)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
