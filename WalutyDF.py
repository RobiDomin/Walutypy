import tkinter as tk
from tkinter import messagebox

class Przelicznik_Walut:
    def __init__(self, master):
        self.master = master
        self.master.title("Przelicznik Walut")
        self.master.geometry("400x400")

        # GUI
        self.label_amount = tk.Label(master, text="Wprowadź kwotę w PLN:", width=20, font="Arial 16 bold ")
        self.label_amount.pack(pady=10)

        self.entry_amount = tk.Entry(master)
        self.entry_amount.pack(pady=10)

        self.label_currency = tk.Label(master, text="Wybierz walutę:", width=20, font="Arial 16 bold")
        self.label_currency.pack(pady=10)

        self.currency_var = tk.StringVar(value="USD")
        self.currencies = {"USD": 4.5, "EUR": 4.8, "GBP": 5.4, "HUF": 0.012, "CZK": 0.2}
        self.dropdown = tk.OptionMenu(master, self.currency_var, *self.currencies.keys())
        self.dropdown.pack(pady=10)

        self.convert_button = tk.Button(master, text="Przelicz", command=self.convert, width=10, font="Arial 16 bold")
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 20))
        self.result_label.pack(pady=10)

    def convert(self):
        try:
            amount = float(self.entry_amount.get())
            if amount < 0:
                raise ValueError("Kwota nie może być ujemna.")

            currency = self.currency_var.get()
            rate = self.currencies[currency]
            converted_amount = round(amount / rate, 2)

            self.result_label.config(text=f"Kwota: {converted_amount} {currency}")
        except ValueError as e:
            messagebox.showerror("Błąd", f"Niepoprawna kwota: {e}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany błąd: {e}")

    def  __del__(self):
        print("Program zakończony")


if __name__ == "__main__":
    root = tk.Tk()
    app = Przelicznik_Walut(root)
    root.mainloop()
