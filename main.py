import customtkinter as Ctk
from PIL import Image

Ctk.set_appearance_mode("light")

class App(Ctk.CTk):
    
    window_width = 930
    window_height = 500

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Obtém tamanho da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()     
        
        try:
            self.iconbitmap("icon.ico")  # Para Windows (.ico)
        except:
            icon_image = Ctk.CTkImage(Image.open("icon.png"), size=(32, 32))  # Para Linux/macOS (.png)
            self.iconphoto(True, icon_image._photo_image)  # Define o ícone 
    
        # Centraliza a janela
        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)

        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.minsize(900, 400)
        self.resizable(False, False)
        
        # Configuração da grade para dividir a tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.configure(fg_color="#007b83")
        self.showUI()
    
    def showUI(self):
        # Frame da esquerda (Campos e Botão)
        left_frame = Ctk.CTkFrame(self, fg_color="#ffffff")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Frame para título e ícone
        title_frame = Ctk.CTkFrame(left_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, padx=30, pady=(25, 0), sticky="w")

        # Ícone
        icon_image = Ctk.CTkImage(light_image=Image.open("temperatura.png"), size=(30, 30))
        icon_label = Ctk.CTkLabel(title_frame, image=icon_image, text="")
        icon_label.pack(side="left", padx=(0, 10))

        # Título
        lbl_titulo = Ctk.CTkLabel(title_frame, text="Conversor", text_color="#007b83", font=("Arial", 30))
        lbl_titulo.pack(side="left")

        # Configurar para centralizar o conteúdo
        left_frame.grid_rowconfigure(0, weight=1)  # Espaço antes dos campos
        left_frame.grid_rowconfigure(4, weight=1)  # Espaço depois do botão
        left_frame.grid_columnconfigure(0, weight=1)

        # Frame interno para centralizar os elementos
        container = Ctk.CTkFrame(left_frame, fg_color="#ffffff")
        container.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        container.grid_columnconfigure(0, weight=1)
        
        # Campo Temperatura
        lbl_campo1 = Ctk.CTkLabel(container, text="Temperatura", text_color="#007b83")
        lbl_campo1.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")

        self.entry1 = Ctk.CTkEntry(container)
        self.entry1.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Campo 2
        lbl_campo2 = Ctk.CTkLabel(container, text="Converter para", text_color="#007b83")
        lbl_campo2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.combobox = Ctk.CTkComboBox(container, values=["Fahrenheit", "Celsius"])
        self.combobox.set("Fahrenheit")  # Padrão: Converter para Fahrenheit
        self.combobox.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # Botão
        btn_enviar = Ctk.CTkButton(container, text="Converter", command=self.calculate, fg_color="#005f63")
        btn_enviar.grid(row=4, column=0, padx=10, pady=20, sticky="ew")

        # Frame da direita (Resultado)
        right_frame = Ctk.CTkFrame(self, fg_color="transparent")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Variável StringVar
        self.text_var = Ctk.StringVar(value=f"{0.0:.2f}°")
        lbl_text = Ctk.CTkLabel(
            right_frame, 
            textvariable=self.text_var,
            font=("Arial", 80),
            text_color="white"
        )
        lbl_text.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza no frame

    def calculate(self):
        value = 0
        try:
            input_value = float(self.entry1.get())
            choice = self.combobox.get()
            
            if choice == "Fahrenheit":
                value = self.toFahrenheit(input_value)
            else:
                value = self.toCelsius(input_value)
            
            self.text_var.set(f"{value:.2f}°")
        except:
            self.text_var.set(f"{value:.2f}°")
    
    def toFahrenheit(self, value):
        return (value * 1.8) + 32 
    
    def toCelsius(self, value):
        return (value - 32) / 1.8

if __name__ == "__main__":
    app = App()
    app.mainloop()
