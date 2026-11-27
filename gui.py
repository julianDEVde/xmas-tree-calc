import customtkinter as ctk
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("Xmas tree clac")

        self.input_frame = CTKFrame(self)
        self.input_frame.grid(row=0, column=0)


class CTKFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.tp_image_path = "assets/td_template_specs.jpg"

        # Input fields
        self.gamma_input = ctk.CTkEntry(self, placeholder_text="Gamma")
        self.gamma_input.grid(row=0, column=0, padx=10)

        self.beta_input = ctk.CTkEntry(self, placeholder_text="Beta")
        self.beta_input.grid(row=1, column=0, padx=10)

        self.height_input = ctk.CTkEntry(self, placeholder_text="Height")
        self.height_input.grid(row=2, column=0, padx=10)

        self.width_input = ctk.CTkEntry(self, placeholder_text="Width")
        self.width_input.grid(row=3, column=0, padx=10)

        self.step_amount_input = ctk.CTkEntry(self, placeholder_text="Step amount")
        self.step_amount_input.grid(row=4, column=0, padx=10)

        self.overlap_input = ctk.CTkEntry(self, placeholder_text="Overlap per step")
        self.overlap_input.grid(row=5, column=0, padx=10)

        self.thickness_input = ctk.CTkEntry(self, placeholder_text="Thickness of material")
        self.thickness_input.grid(row=6, column=0, padx=10)

        self.percent_input = ctk.CTkEntry(self, placeholder_text="Bigger top step")
        self.percent_input.grid(row=7, column=0, padx=10)

        self.generate_button = ctk.CTkButton(self, text="Generate", command=self.get_input)
        self.generate_button.grid(row=8, column=0)

        # Template pictures
        self.tp_image = ctk.CTkImage(Image.open("assets/td_template_specs.jpg"), size=(821 / 2.5, 1094 / 2.5))
        self.tp_label = ctk.CTkLabel(self, text="", image=self.tp_image)
        self.tp_label.grid(row=0, column=1, padx=10, pady=10, rowspan=8)

        self.td_image_button = ctk.CTkButton(self, text="Drawn / Real tree", command=self.change_tp_image)
        self.td_image_button.grid(row=8, column=1)

    def change_tp_image(self):
        if self.tp_image_path == "assets/real_tree_template.jpg":
            self.tp_image_path = "assets/td_template_specs.jpg"
        else:
            self.tp_image_path = "assets/real_tree_template.jpg"
        self.new_td_image = ctk.CTkImage(Image.open(self.tp_image_path), size=(821 / 2.5, 1094 / 2.5))
        self.tp_label.configure(image=self.new_td_image)

    def get_input(self):
        gamma = self.gamma_input.get()
        beta = self.beta_input.get()
        heigth = self.height_input.get()
        width = self.width_input.get()
        step_amount = self.step_amount_input.get()
        overlap = self.overlap_input.get()
        thickness = self.thickness_input.get()
        percent = self.percent_input.get()



app = App()
app.mainloop()