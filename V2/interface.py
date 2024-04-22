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
        self.style.configure('My.TEntry', padding=10)

        self.label_word = ttk.Label(self.centered_frame, text="Enter a word :", style='My.TLabel')
        self.label_word.pack()

        self.entry_word = ttk.Entry(self.centered_frame, style='My.TEntry')
        self.entry_word.pack(ipadx=100)

        self.label_num = ttk.Label(self.centered_frame, text="Enter the number of iterations (N):", style='My.TLabel')
        self.label_num.pack()

        self.entry_num = ttk.Entry(self.centered_frame, style='My.TEntry')
        self.entry_num.pack(ipadx=100)

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

        self.label_output = ttk.Label(self.centered_frame, text="", style='My.TLabel', anchor='w', font=('Helvetica', 15))
        self.label_output.pack(padx=20,pady=5)

    def get_values(self):
        word = self.entry_word.get()
        if word in self.data:
            self.label_output.config(text="")
            num_iterations = int(self.entry_num.get())
            generated_text = ""
            for _ in range(num_iterations):
                values = self.data[word]
                next_word = random.choice(list(values.keys()))
                generated_text = generated_text + " " + next_word
                word = next_word
            self.label_output.config(text=generated_text)
        else:
            self.label_output.config(text="Aucune valeur trouvée pour ce mot.")

    def clear_text(self):
        self.entry_word.delete(0, tk.END)
        self.entry_num.delete(0, tk.END)
        self.label_output.config(text="")

    def show_interface(self):
        self.root.mainloop()
