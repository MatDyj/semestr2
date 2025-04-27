import argparse
from pypdf import PdfReader, PdfWriter

def polacz_pdf(lista_plikow, plik_wyjscia):
    """
    Funkcja do łączenia kilku plików PDF w jeden dokument.

    Parametry:
    lista_plikow (list): Lista ścieżek do plików PDF, które mają być połączone.
    plik_wyjscia (str): Ścieżka do pliku wynikowego, w którym zostanie zapisany połączony PDF.
    """
    lacznik = PdfWriter()

    for plik in lista_plikow:
        czytnik = PdfReader(plik)
        for strona in czytnik.pages:
            lacznik.add_page(strona)

    with open(plik_wyjscia, "wb") as f:
        lacznik.write(f)

    print(f"Pliki PDF zostały połączone i zapisane jako {plik_wyjscia}")

def main():
    """
    Główna funkcja programu do łączenia plików PDF.
    """
    parser = argparse.ArgumentParser(description="Program do łączenia wielu plików PDF w jeden dokument.")
    parser.add_argument('--wejscie', required=True, nargs='+', help="Ścieżki do plików PDF do połączenia (podaj kilka plików oddzielonych spacjami)")
    parser.add_argument('--wyjscie', required=True, help="Ścieżka do pliku wynikowego (np. polaczony.pdf)")

    args = parser.parse_args()

    polacz_pdf(args.wejscie, args.wyjscie)

if __name__ == "__main__":
    main()