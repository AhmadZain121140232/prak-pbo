import tkinter as tk

def Kalkulator():
    angk1 = int(entry_angk1.get())
    angk2 = int(entry_angk2.get())
    operasi = entry_operasi.get()
    
    if operasi == '+':
        hasil = angk1 + angk2
    elif operasi == '-':
        hasil = angk1 - angk2
    elif operasi == '*':
        hasil = angk1 * angk2
    elif operasi == '/':
        hasil = angk1 / angk2
    else:
        hasil = 'Input tidak valid'
    
    label_hasil.config(text='hasil: ' + str(hasil))

window = tk.Tk()
window.title('Calculator')

label_angk1 = tk.Label(window, text='Angka Pertama:')
label_angk1.pack()
entry_angk1 = tk.Entry(window)
entry_angk1.pack()

label_operasi = tk.Label(window, text='Operator:')
label_operasi.pack()
entry_operasi = tk.Entry(window)
entry_operasi.pack()

label_angk2 = tk.Label(window, text='Angka Kedua:')
label_angk2.pack()
entry_angk2 = tk.Entry(window)
entry_angk2.pack()

btn_Kalkulator = tk.Button(window, text='Hitung', command=Kalkulator)
btn_Kalkulator.pack()

label_hasil = tk.Label(window, text='Hasil:')
label_hasil.pack()

window.mainloop()