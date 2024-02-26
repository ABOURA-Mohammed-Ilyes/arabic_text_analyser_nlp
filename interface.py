import tkinter as tk
from tkinter import ttk

class Interface():
    def __init__(self, data):
        self.data = data
        self.root = tk.Tk()
        self.root.title("Generate Arabic Word")
        self.root.geometry("1000x800") 

        self.style = ttk.Style()
        self.style.configure('My.TLabel', font=('Helvetica', 12,'bold'), padding=10, foreground="black")

        self.label = ttk.Label(self.root, text="Enter a word :", style='My.TLabel')
        self.label.pack()

        self.style.configure('My.TEntry', font=('Helvetica', 12), padding=10, borderwidth=1, relief="flat")
        self.entry = ttk.Entry(self.root, style='My.TEntry')
        self.entry.pack(ipadx=100)  

        frame = ttk.Frame(self.root, style='RoundedFrame.TFrame')
        frame.pack(pady=20)

        self.style.configure('My.TButton', font=('Helvetica', 12), padding=10, background='black', foreground='black', borderwidth=5, relief="ridge")
        self.generate_button = ttk.Button(frame, text="Generate", command=self.get_values, style='My.TButton')
        self.generate_button.pack(padx=20, pady=10)

        self.clear_button = ttk.Button(frame, text="Clear", command=self.clear_text, style='My.TButton')
        self.clear_button.pack(padx=20, pady=10)
        
        self.text = tk.Text(self.root, width=50, height=10, wrap=tk.WORD)
        self.text.pack(pady=10)

    def get_values(self):
        word = self.entry.get()
        if word in self.data:
            values = self.data[word]
            self.text.delete("1.0", tk.END)  
            for key, value in values.items():
                self.text.insert(tk.END, f"{key}\t")  
        else:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "Aucune valeur trouvée pour ce mot.\n")  

    def clear_text(self):
        self.entry.delete(0, tk.END)
        self.text.delete("1.0", tk.END)

    def show_interface(self):
        self.root.mainloop()
