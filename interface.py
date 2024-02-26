import tkinter as tk

class Interface():
    def __init__(self, data):
        self.data = data
        self.root = tk.Tk()
        self.root.title("Generate Arabic Word")
        self.label = tk.Label(self.root, text="Enter a word:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Generate", command=self.get_values)
        self.button.pack()
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack()

    def get_values(self):
        word = self.entry.get()
        if word in self.data:
            values = self.data[word]
            self.listbox.delete(0, tk.END)
            for key, value in values.items():
                self.listbox.insert(tk.END, f"{key}: {value}")
        else:
            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, "Aucune valeur trouvée pour ce mot.")

    def show_interface(self):
        self.root.mainloop()


