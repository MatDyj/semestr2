from PIL import Image

def miniatura(wejscie, wyjscie, rozmiar):
    """
    Tworzy miniaturę obrazu o zadanym rozmiarze.

    :param wejscie: Ścieżka do oryginalnego pliku
    :param wyjscie: Ścieżka do zapisanego pliku miniatury
    :param rozmiar: Rozmiar miniatury jako krotka (szerokość, wysokość)
    """
    try:
        with Image.open(wejscie) as obraz:
            obraz.thumbnail(rozmiar)
            obraz.save(wyjscie, "JPEG")
            print(f"Miniatura zapisana jako: {wyjscie}")
            obraz.show()
    except FileNotFoundError:
        print("Błąd: Plik wejściowy nie istnieje.")


miniatura(r"C:\Users\mateu\OneDrive\Pulpit\semestr2\2.jpg", r"C:\Users\mateu\OneDrive\Pulpit\semestr2\miniatura.jpeg", (100, 100))
