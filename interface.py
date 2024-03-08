import tkinter as tk
from tkinter import ttk
import random

class Interface():
    def __init__(self, data):
        self.data = data
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.configure_gui()

    def configure_gui(self):
        self.root.configure(background='#222831')
        self.style.configure('Frame1.TFrame', background='#222831')
        self.centered_frame = ttk.Frame(self.root,style='Frame1.TFrame')
        self.centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.root.title("Generate Arabic Word")
        self.root.geometry("1000x800") 

        self.style.configure('My.TLabel', font=('Helvetica', 12,'bold'), padding=20, background='#222831', foreground="white")

        self.label = ttk.Label(self.centered_frame, text="Enter a word :", style='My.TLabel')


        self.label.pack()

        self.style.configure('My.TEntry', padding=(20, 10))

        self.entry = ttk.Entry(self.centered_frame, style='My.TEntry')
        self.entry.pack(ipadx=100)

        self.style.configure('My.TButton', font=('Helvetica', 12),
                             padding=(10, 5), borderwidth=2, relief='groove',
                             cursor='hand2', # Change cursor to hand on hover
                             )

        self.style.map('My.TButton',
            foreground=[('pressed', '#2980b9')],
        )

        self.generate_button = ttk.Button(self.centered_frame, text="Generate", command=self.get_values, style='My.TButton')
        self.generate_button.pack(padx=20, pady=10)

        self.clear_button = ttk.Button(self.centered_frame, text="Clear", command=self.clear_text, style='My.TButton')
        self.clear_button.pack(padx=20, pady=10)

        self.text = tk.Text(self.centered_frame, width=50, height=10, wrap=tk.WORD)
        self.text.pack(pady=10)

    def get_values(self):
        word = self.entry.get()
        if word in self.data:
            values = self.data[word]
            self.text.delete("1.0", tk.END)  
            random_key = random.choice(list(values.keys()))
            self.text.insert(tk.END, f"{random_key}\t")  
        else:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "Aucune valeur trouvée pour ce mot.\n")  

    def clear_text(self):
        self.entry.delete(0, tk.END)
        self.text.delete("1.0", tk.END)

    def show_interface(self):
        self.root.mainloop()
