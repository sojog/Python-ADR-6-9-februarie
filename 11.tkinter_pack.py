
# tk - alias conventional
import tkinter as tk

window = tk.Tk()

print(window.winfo_geometry())
print(window.winfo_height(), window.winfo_width())

print(window.winfo_screenheight(), window.winfo_screenwidth())


SCREEN_HEIGHT = window.winfo_screenheight()
SCREEN_WIDTH = window.winfo_screenwidth()


width = height = 800
x = SCREEN_WIDTH // 2 - width // 2
y = SCREEN_HEIGHT // 2 - height // 2
print(window.winfo_geometry())

window.geometry(f"{width}x{height}+{x}+{y}")

label1 = tk.Label(window, text = "Acesta este un label")
label1.pack()
label2 = tk.Label(window, text = "Acesta este un alt label")
label2.pack()

def functie_apelata_de_buton():
    print("Functia a fost apelata de catre buton")

button1 = tk.Button(window, text="Acesta este un buton", command=functie_apelata_de_buton)
button1.pack()

button2 = tk.Button(window, text="Acesta este un alt buton")
button2.pack()


def functie_apelata_print_bind(event):
    print("Evenimentul apelat este:", event, type(event))

button2.bind('<Button-1>', functie_apelata_print_bind)

window.mainloop()