import argparse

def konwersja(wejscie, wyjscie, windows):
     """
    Konwertuje znaki końca linii w pliku tekstowym.

    Args:
        wejscie (str): Ścieżka do pliku wejściowego.
        wyjscie (str): Ścieżka do pliku wyjściowego.
        windows(bool): Jeśli True, konwertuje na Windows (CRLF). 
                           Jeśli False, konwertuje na Unix (LF).
    """
    with open(wejscie, 'rb') as plik:
        x=plik.read()

    if windows:
        x=x.replace(b'\r', b'')
        x=x.replace(b'\n', b'\r\n')
    else:
        x=x.replace(b'\r\n', b'\n')
    with open(wyjscie, 'wb') as plik:
        plik.write(x)
def main():
    """
    Parsuje argumenty wiersza poleceń i wykonuje konwersję końców linii
    w pliku wejściowym na podstawie podanych opcji.
    """
    parser = argparse.ArgumentParser(
        description="Konwertuj końce linii w plikach tekstowych między Unix (LF) i Windows (CRLF)."
    )
    parser.add_argument('wejscie', help="Ścieżka do pliku wejściowego")
    parser.add_argument('wyjscie', help="Ścieżka do pliku wyjściowego")
    parser.add_argument('--windows', action='store_true',
                        help="Jeśli podane, konwertuje na Windows (CRLF). Domyślnie konwertuje na Unix (LF).")

    args = parser.parse_args()

    konwersja(args.wejscie, args.wyjscie, args.windows)

if __name__ == "__main__":
    """
    Główne wejście programu: wywołuje funkcję main(), jeśli plik uruchamiany jest bezpośrednio.
    """
    main()