import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog


prolog = Prolog()
prolog.consult("pakar_ganguantidur_gui.pl")


gejala_dict = {
    "g1": "Sering terbangun tengah malam",
    "g2": "Sulit tidur saat malam",
    "g3": "Bangun terlalu pagi",
    "g4": "Rasa kantuk berlebihan di siang hari",
    "g5": "Sering mimpi buruk",
    "g6": "Kecemasan atau stres",
    "g7": "Mudah lelah saat bangun",
    "g8": "Sakit kepala pagi hari"
}

class DiagnosaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnosa Gangguan Tidur")
        self.check_vars = {}

        tk.Label(root, text="Pilih Gejala yang Dialami:", font=("Helvetica", 14)).pack(pady=10)

        for kode, deskripsi in gejala_dict.items():
            var = tk.IntVar()
            cb = tk.Checkbutton(root, text=f"{kode.upper()} - {deskripsi}", variable=var, anchor='w', justify='left')
            cb.pack(fill='x', padx=20)
            self.check_vars[kode] = var

        tk.Button(root, text="Diagnosa", command=self.diagnosa).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", justify="left")
        self.result_label.pack(pady=10)

    def diagnosa(self):
        selected = [kode for kode, var in self.check_vars.items() if var.get() == 1]

        if not selected:
            messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala.")
            return

        hasil = []
        for sol in prolog.query(f"diagnosa({selected}, G)."):
            gangguan = sol["G"]
            if gangguan not in hasil:
                hasil.append(gangguan)

        if hasil:
            output = "Kemungkinan gangguan tidur:\n" + "\n".join(f"- {g.replace('_', ' ').title()}" for g in hasil)
        else:
            output = "Tidak terdeteksi gangguan tidur berdasarkan gejala tersebut."

        self.result_label.config(text=output)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosaApp(root)
    root.mainloop()
