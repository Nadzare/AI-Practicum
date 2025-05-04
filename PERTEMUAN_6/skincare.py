import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog


prolog = Prolog()
prolog.consult("skincare_gui.pl")

skincare_list = []
gejala_dict = {}
index_skincare = 0
index_gejala = 0
current_skincare = ""
current_gejala = ""

def mulai_diagnosa():
    global skincare_list, gejala_dict, index_skincare, index_gejala
    prolog.retractall("gejala_pos(_)") 
    prolog.retractall("gejala_neg(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    skincare_list = [s["X"].decode() for s in list(prolog.query("skincare(X)"))]
    for s in skincare_list:
        gejala_dict[s] = [g["X"] for g in list(prolog.query(f"gejala(X,\"{s}\")"))]

    index_skincare = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_skincare=False):
    global current_skincare, current_gejala, index_skincare, index_gejala

    if ganti_skincare:
        index_skincare += 1
        index_gejala = -1
    if index_skincare >= len(skincare_list):
        tampilkan_hasil()
        return

    current_skincare = skincare_list[index_skincare]
    index_gejala += 1

    if index_gejala >= len(gejala_dict[current_skincare]):
        tampilkan_hasil(current_skincare)
        return

    current_gejala = gejala_dict[current_skincare][index_gejala]

    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_skincare=True)
        return

    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala}, Y)"))
    if pertanyaan:
        tampilkan_pertanyaan(pertanyaan[0]["Y"].decode())

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_skincare=True)

def tampilkan_hasil(skincare=""):
    if skincare:
        messagebox.showinfo("Rekomendasi Skincare", f"Rekomendasi skincare: {skincare}.")
    else:
        messagebox.showinfo("Rekomendasi Skincare", "Tidak ditemukan rekomendasi skincare yang cocok.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)


root = tk.Tk()
root.title("Aplikasi Rekomendasi Skincare")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Rekomendasi Skincare", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=50, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = tk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3)

yes_btn = tk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3)

start_btn = ttk.Button(mainframe, text="Mulai Diagnosa", command=mulai_diagnosa)
start_btn.grid(column=1, row=4, columnspan=2)

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
