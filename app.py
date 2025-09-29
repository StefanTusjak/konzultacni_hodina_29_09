import tkinter as tk

# Funkce pro zpracování stisknutí tlačítka
def klik(btn_text):
    current = entry.get()
    
    if btn_text == "=":
        try:
            result = str(eval(current))  # Výpočet výrazu
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Chyba")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# Vytvoření hlavního okna
okno = tk.Tk()
okno.title("Jednoduchá kalkulačka")
okno.resizable(False, False)

# Vstupní pole pro zadání výrazu
entry = tk.Entry(okno, width=20, font=("Arial", 20), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definice tlačítek
tlacitka = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
]

# Dynamické generování tlačítek
radek = 1
sloupec = 0

for znak in tlacitka:
    tl = tk.Button(okno, text=znak, padx=20, pady=20, font=("Arial", 14),
                   width=4, command=lambda z=znak: klik(z))
    tl.grid(row=radek, column=sloupec, padx=5, pady=5)
    
    sloupec += 1
    if sloupec > 3:
        sloupec = 0
        radek += 1

# Spuštění aplikace
okno.mainloop()
