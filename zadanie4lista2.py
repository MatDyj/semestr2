import os
import pypdf
from pathlib import Path

def podzielenie_pdf(pdf, ilosc_stron):
    czytnik=pypdf.PdfReader(pdf)
    licznik_stron=czytnik.get_num_pages()
    ilosc_wyjsc=(licznik_stron + ilosc_stron - 1)//ilosc_stron
    sciezka_wyjscia=Path("wyjscie")
    sciezka_wyjscia.mkdir(parents=True, exist_ok=True)
    for i in range(ilosc_wyjsc):
        pisarz=pypdf.PdfWriter()
        pierwsza_strona=i*licznik_stron
        koncowa_strona=min(pierwsza_strona + ilosc_stron, licznik_stron)
        for numer_strony in range(pierwsza_strona, koncowa_strona):
            pisarz.add_page(czytnik.pages[numer_strony])
        plik_wyjscia=sciezka_wyjscia / f"Podzielone {i+1}.pdf"
        with plik_wyjscia.open("wb") as wyjscie_pdf:
            pisarz.write(wyjscie_pdf)
        print(f"Zapisano: {plik_wyjscia}")
podzielenie_pdf("2025_05.pdf", 2)