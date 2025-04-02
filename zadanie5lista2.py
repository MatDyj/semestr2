from PIL import Image

def tworzenie_znak_wodny(wejscie, znak_wodny, wyjscie, pozycja=(200, 200)):
        """
    Nakłada znak wodny na obraz.

    Parametry:
    wejscie: Ścieżka do obrazu wejściowego.
    znak_wodny: Ścieżka do obrazu znaku wodnego.
    wyjscie: Ścieżka do zapisu obrazu z nałożonym znakiem wodnym.
    pozycja: Pozycja (x, y) umieszczenia znaku wodnego na obrazie.

    Zapisuje wynikowy obraz w formacie PNG.
    """
    podstawowe_zdjecie=Image.open(wejscie).convert("RGBA")
    znak=Image.open(znak_wodny).convert("RGBA")
    znak=znak.resize((podstawowe_zdjecie.width // 2, podstawowe_zdjecie.height // 2))
    podstawowe_zdjecie.paste(znak, pozycja, mask=znak)
    podstawowe_zdjecie.save(wyjscie, format="PNG")

tworzenie_znak_wodny("2.jpg", "watermark.jpg", "znak_wodny.jpg" )