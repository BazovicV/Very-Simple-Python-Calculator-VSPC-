import tkinter as tk

prozor = tk.Tk()
prozor.title("Kalkulator")
prozor.geometry("400x200")

user_input = tk.StringVar(prozor)

def racunanje():
    try:
        izraz = user_input.get()
        rezultat = eval(izraz)
        tekst.config(text="Rezultat: " + str(rezultat))
    except:
        tekst.config(text="Ovo nije izraz koji se može izračunati.")

kalkul = tk.Label(prozor, text="Upišite izraz: ")
kalkul.pack()

napisati = tk.Entry(prozor, textvariable=user_input)
napisati.pack()

dugme = tk.Button(prozor, text="Izračunaj", command=racunanje)
dugme.pack() 

tekst = tk.Label(prozor, text="")
tekst.pack()

prozor.mainloop()
