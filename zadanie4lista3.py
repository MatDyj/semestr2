import argparse
import qrcode
import cv2

def generowanie_qr(dane, plik_wyjscia):
    """
    Funkcja do generowania kodu QR na podstawie danych i zapisania go w pliku.

    Parameters:
    dane (str): Dane, które mają zostać zakodowane w QR.
    plik_wyjscia (str): Ścieżka do pliku, w którym zostanie zapisany wygenerowany kod QR.
    """
    qr = qrcode.make(dane)
    qr.save(plik_wyjscia)
    print(f"Qr kod zapisany jako {plik_wyjscia}")

def odczyt_qr(plik_wejscia):
    """
    Funkcja do odczytywania kodu QR z pliku.

    Parameters:
    plik_wejscia (str): Ścieżka do pliku zawierającego kod QR.

    Zwraca:
    dane (str): Odczytane dane z kodu QR, jeżeli kod QR zostanie poprawnie odczytany.
    """
    qr = cv2.imread(plik_wejscia)
    wykrywacz_qr = cv2.QRCodeDetector()
    dane, ramka, _ = wykrywacz_qr.detectAndDecode(qr)
    if dane:
        print(f"Odczytano dane z {plik_wejscia}")
        print(dane)
    else:
        print(f"Nie odnaleziono kodu QR")

def main():
    """
    Główna funkcja programu, która umożliwia generowanie i odczytywanie kodów QR 
    w zależności od podanych argumentów w linii poleceń.
    """
    parser = argparse.ArgumentParser(
        description="Program do generowania i odczytywania kodów QR"
    )
    subparsers = parser.add_subparsers(dest="komenda", help="Podkomendy: generuj lub odczytuj")
    
    parser_generuj = subparsers.add_parser('generuj', help="Generuj kod QR")
    parser_generuj.add_argument('--dane', required=True, help="Dane do zakodowania w QR")
    parser_generuj.add_argument('--wyjscie', required=True, help="Ścieżka do pliku wynikowego (np. qr.png)")

    parser_odczytaj = subparsers.add_parser('odczytaj', help="Odczytaj kod QR z pliku")
    parser_odczytaj.add_argument('--wejscie', required=True, help="Ścieżka do pliku wejściowego (np. qr.png)")

    args = parser.parse_args()

    if args.komenda == 'generuj':
        generowanie_qr(args.dane, args.wyjscie)
    elif args.komenda == 'odczytaj':
        odczyt_qr(args.wejscie)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()