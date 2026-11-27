import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("350x600")
        self.title("Xmas tree clac")

        self.input_frame = CTKFrame(self)
        self.input_frame.grid(row=0, column=0)


class CTKFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Input fields
        self.gamma_input = ctk.CTkEntry(self, placeholder_text="Gamma")
        self.gamma_input.grid(row=0, column=0, padx=10, pady=10)

        self.beta_input = ctk.CTkEntry(self, placeholder_text="Beta")
        self.beta_input.grid(row=1, column=0, padx=10, pady=10)

        self.height_input = ctk.CTkEntry(self, placeholder_text="Height")
        self.height_input.grid(row=2, column=0, padx=10, pady=10)

        self.width_input = ctk.CTkEntry(self, placeholder_text="Width")
        self.width_input.grid(row=3, column=0, padx=10, pady=10)

        self.step_amount_input = ctk.CTkEntry(self, placeholder_text="Step amount")
        self.step_amount_input.grid(row=4, column=0, padx=10, pady=10)

        self.overlap_input = ctk.CTkEntry(self, placeholder_text="Overlap per step")
        self.overlap_input.grid(row=5, column=0, padx=10, pady=10)

        self.thickness_input = ctk.CTkEntry(self, placeholder_text="Thickness of material")
        self.thickness_input.grid(row=6, column=0, padx=10, pady=10)

        self.percent_input = ctk.CTkEntry(self, placeholder_text="Bigger top step")
        self.percent_input.grid(row=7, column=0, padx=10, pady=10)


app = App()
app.mainloop()