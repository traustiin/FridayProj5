import tkinter as tk

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")
        
        self.label = tk.Label(master, text="Translate Here", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.btn_english = tk.Button(master, text="English", command=self.translate_english)
        self.btn_english.pack(side=tk.LEFT, padx=10)
        
        self.btn_spanish = tk.Button(master, text="Spanish", command=self.translate_spanish)
        self.btn_spanish.pack(side=tk.LEFT, padx=10)
        
        self.btn_french = tk.Button(master, text="French", command=self.translate_french)
        self.btn_french.pack(side=tk.LEFT, padx=10)
        
        self.btn_german = tk.Button(master, text="German", command=self.translate_german)
        self.btn_german.pack(side=tk.LEFT, padx=10)
        
    def translate_english(self):
        self.label.config(text="Hello")
        
    def translate_spanish(self):
        self.label.config(text="Hola")
        
    def translate_french(self):
        self.label.config(text="Bonjour")
        
    def translate_german(self):
        self.label.config(text="Hallo")

def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
