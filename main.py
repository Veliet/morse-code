import tkinter as tk

MORSE = {
        "A": ".-",     "B": "-...",   "C": "-.-.",
        "D": "-..",    "E": ".",      "F": "..-.",
        "G": "--.",    "H": "....",   "I": "..",
        "J": ".---",   "K": "-.-",    "L": ".-..",
        "M": "--",     "N": "-.",     "O": "---",
        "P": ".--.",   "Q": "--.-",   "R": ".-.",
        "S": "...",    "T": "-",      "U": "..-",
        "V": "...-",   "W": ".--",    "X": "-..-",
        "Y": "-.--",   "Z": "--..",

        "0": "-----",  "1": ".----",  "2": "..---",
        "3": "...--",  "4": "....-",  "5": ".....",
        "6": "-....",  "7": "--...",  "8": "---..",
        "9": "----.",
        " ": "/"}

REVERSE = {value:key for key,value in MORSE.items()}


def encode(texto):
    result = []

    for char in texto:
        result.append(MORSE.get(char.upper(), "?"))

    return " ".join(result)


def decode(code):
    words = code.split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = []

        for symbol in letters:
            decoded_letters.append(REVERSE.get(symbol, "?"))

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)

def mk_root():
    root = tk.Tk()
    root.title("Morse")
    root.geometry("350x280")
    root.resizable(False, False)

    label_1 = tk.Label(root, text=">> Entrada <<")
    label_1.pack(padx=5)

    campo_entrada = tk.Text(root, width=40, height=5)
    campo_entrada.pack(pady= 15)

    label_2 = tk.Label(root, text=">> Saída <<")
    label_2.pack(padx=5)

    campo_saida = tk.Text(root, width=40, height=5)
    campo_saida.pack(pady= 15)
    campo_saida.config(state="disabled")

    campo_entrada.bind("<KeyRelease>", lambda event: translate(campo_entrada,campo_saida, event))

    return root, campo_entrada, campo_saida, label_1, label_2

def translate(campo_entrada, campo_saida, event=None):
    entrada = campo_entrada.get("1.0",tk.END).strip()

    if not entrada:
        campo_saida.config(state="normal")
        campo_saida.delete("1.0", tk.END)
        campo_saida.config(state="disabled")
        return

    char_morse = {".", "-", "/", " "}

    if "." in entrada or "-" in entrada:
        result = decode(entrada)

    else:
        result = encode(entrada)

    campo_saida.config(state="normal")
    campo_saida.delete("1.0", tk.END)
    campo_saida.insert(tk.END, result)
    campo_saida.config(state="disabled")

def main():
    root, campo_entrada, campo_saida,label_1, label_2 = mk_root()
    root.mainloop()

if __name__ == "__main__":
    main()