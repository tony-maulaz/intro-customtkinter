import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("400x300")

        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.configure(fg_color="red")
        self.left_frame.pack(side="left", fill="x", expand=True)

        self.right_frame = ctk.CTkFrame(self, width=150, height=100)
        self.right_frame.configure(fg_color="light blue")
        self.right_frame.pack_propagate(0) # Prevent the frame from resizing to fit its contents
        self.right_frame.pack(side="right", fill="x", expand=False)

        self.label = ctk.CTkLabel(self.left_frame, text="Label frame left")
        self.label.pack(pady=20)

        self.label = ctk.CTkLabel(self.right_frame, text="Label frame right")
        self.label.pack()

        self.button = ctk.CTkButton(self, text="Button")
        self.button.configure(command=self.on_button_click)
        self.button.pack(side="bottom", pady=20)

    def on_button_click(self):
        print("Button clicked")

if __name__ == "__main__":
    app = App()
    app.mainloop()
