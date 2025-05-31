import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os

KURSY = "kursy_nbp.json"
NBP_URL = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
ODSWIEZANIE = 300000  # 5 minut w ms

Flagi = {
    "USD": "🇺🇸",
    "EUR": "🇪🇺",
    "CHF": "🇨🇭",
    "GBP": "🇬🇧",
    "JPY": "🇯🇵",
    "NOK": "🇳🇴",
    "SEK": "🇸🇪",
    "DKK": "🇩🇰",
    "CZK": "🇨🇿",
    "CAD": "🇨🇦",
    "AUD": "🇦🇺",
    "CNY": "🇨🇳",
    "PLN": "🇵🇱",
}

Panstwa = {
    "USD": "USA",
    "EUR": "Strefa Euro",
    "CHF": "Szwajcaria",
    "GBP": "Wielka Brytania",
    "JPY": "Japonia",
    "NOK": "Norwegia",
    "SEK": "Szwecja",
    "DKK": "Dania",
    "CZK": "Czechy",
    "CAD": "Kanada",
    "AUD": "Australia",
    "CNY": "Chiny",
    "PLN": "Polska",
}

def kursy():
    """
    Pobiera aktualne kursy walut z API NBP.
    W przypadku braku połączenia, próbuje wczytać kursy z lokalnego pliku.
    Zwraca słownik danych z kursami lub None jeśli nie uda się pobrać ani wczytać danych.
    """
    try:
        odp = requests.get(NBP_URL)
        odp.raise_for_status()
        dane = odp.json()[0]
        with open(KURSY, "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False)
        return dane
    except Exception:
        if os.path.exists(KURSY):
            with open(KURSY, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return None

def przelicz():
    """
    Pobiera kwotę i wybrane waluty, przelicza kwotę z waluty źródłowej na docelową
    i wyświetla wynik w polu wynikowym.
    W przypadku błędu wyświetla komunikat o niepoprawnej kwocie.
    """
    try:
        kwota = float(kwota_wejsciowa.get())
        waluta_z = combo_z.get().split(" ")[0]
        waluta_do = combo_do.get().split(" ")[0]

        if waluta_z == waluta_do:
            wynik = kwota
        elif waluta_z == "PLN":
            kurs_do = kursa[waluta_do]
            wynik = kwota / kurs_do
        elif waluta_do == "PLN":
            kurs_z = kursa[waluta_z]
            wynik = kwota * kurs_z
        else:
            kurs_z = kursa[waluta_z]
            kurs_do = kursa[waluta_do]
            wynik = kwota * kurs_z / kurs_do

        wynik_wejsciowy.config(state="normal")
        wynik_wejsciowy.delete(0, tk.END)
        wynik_wejsciowy.insert(0, f"{wynik:.2f}")
        wynik_wejsciowy.config(state="readonly")

    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną kwotę")

def zakoncz():
    """Zamyka aplikację."""
    root.destroy()

def odswiezanie():
    """
    Odświeża kursy walut co określony czas.
    Aktualizuje dane i wartości w polach wyboru walut.
    """
    global kursa, waluty, flaga
    nowe_dane = kursy()
    if nowe_dane:
        kursa = {item["code"]: item["mid"] for item in nowe_dane["rates"]}
        kursa["PLN"] = 1.0
        waluty = sorted(kursa.keys())
        flaga = [f"{k} {Flagi.get(k, '')} ({Panstwa.get(k, '')})" for k in waluty]
        combo_z["values"] = flaga
        combo_do["values"] = flaga
    root.after(ODSWIEZANIE, odswiezanie)

# Inicjalizacja danych kursów
dane = kursy()
if dane is None:
    messagebox.showerror("Błąd", "Nie udało się pobrać kursów i nie znaleziono pliku lokalnego.")
    exit()

kursa = {item["code"]: item["mid"] for item in dane["rates"]}
kursa["PLN"] = 1.0
waluty = sorted(kursa.keys())
flaga = [f"{k} {Flagi.get(k, '')} ({Panstwa.get(k, '')})" for k in waluty]

root = tk.Tk()
root.title("💱 Przelicznik walut NBP")

# Powiększenie okna i czcionek
root.geometry("450x280")
font_label = ("Segoe UI", 14)
font_entry = ("Segoe UI", 14)
font_button = ("Segoe UI", 14, "bold")

tk.Label(root, text="Waluta źródłowa:", font=font_label).grid(row=0, column=0, padx=10, pady=10, sticky="w")
combo_z = ttk.Combobox(root, values=flaga, state="readonly", font=font_entry, width=25)
combo_z.set("PLN 🇵🇱 (Polska)")
combo_z.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Waluta docelowa:", font=font_label).grid(row=1, column=0, padx=10, pady=10, sticky="w")
combo_do = ttk.Combobox(root, values=flaga, state="readonly", font=font_entry, width=25)
combo_do.set("USD 🇺🇸 (USA)")
combo_do.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Kwota:", font=font_label).grid(row=2, column=0, padx=10, pady=10, sticky="w")
kwota_wejsciowa = tk.Entry(root, font=font_entry)
kwota_wejsciowa.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Wynik:", font=font_label).grid(row=3, column=0, padx=10, pady=10, sticky="w")
wynik_wejsciowy = tk.Entry(root, font=font_entry, state="readonly")
wynik_wejsciowy.grid(row=3, column=1, padx=10, pady=10)

btn_przelicz = tk.Button(root, text="Przelicz", command=przelicz, font=font_button)
btn_przelicz.grid(row=4, column=0, padx=10, pady=15, sticky="ew")

btn_zakoncz = tk.Button(root, text="Zakończ", command=zakoncz, font=font_button)
btn_zakoncz.grid(row=4, column=1, padx=10, pady=15, sticky="ew")

root.after(ODSWIEZANIE, odswiezanie)

root.mainloop()
