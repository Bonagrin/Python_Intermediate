import tkinter as tk


class Alkalmazás(tk.Frame):
    
    def __init__(self, ablak):
        super().__init__(ablak)
        self.ablak = ablak
        self.pack()
        self.komponenseket_létrehoz()
        
    def nyomógomb_kattintás(self):
        név = str(self.név_bevitel.get())
        if név != "":
            self.üdvözlés_felirat["text"] = f'Szia, {név}!'
            
    def komponenseket_létrehoz(self):
        self.név_keret = tk.Frame(self.ablak)
        self.név_felirat = tk.Label(master = self.név_keret, text = 'Név:')
        self.név_felirat.grid(column = 0, row = 0)
        self.név_bevitel = tk.Entry(master = self.név_keret)
        self.név_bevitel.grid(column = 1, row = 0)
        self.név_keret.pack()
        self.nyomógomb = tk.Button(self.ablak, text = 'Kattints', command = self.nyomógomb_kattintás)
        self.nyomógomb.pack()
        self.üdvözlés_felirat = tk.Label(self.ablak, text = 'Szia!')
        self.üdvözlés_felirat.pack()
        
Alkalmazás(tk.Tk()).mainloop()