import requests
from bs4 import BeautifulSoup
import webbrowser

def pobierz_losowy_artykul():
    """
    Pobiera losowy artykuł z Wikipedii.
    Zwraca tytuł artykułu oraz jego prawdziwy URL.
    """
    url = "https://en.wikipedia.org/wiki/Special:Random"
    odpowiedz = requests.get(url)
    prawdziwy_url = odpowiedz.url
    soup = BeautifulSoup(odpowiedz.text, "html.parser")
    tytul_element = soup.find('h1', id="firstHeading")
    tytul = tytul_element.text if tytul_element else "Nieznany tytuł"
    
    return tytul, prawdziwy_url

def zapytaj_uzytkownika(tytul):
    """
    Pyta użytkownika, czy chce otworzyć artykuł o podanym tytule.
    """
    print(f"Tytuł artykułu: {tytul}")
    decyzja = input("Czy chcesz go otworzyć? (tak/nie): ").strip().lower()
    return decyzja == "tak"

def otworz_w_przegladarce(url):
    """
    Otwiera podany URL w domyślnej przeglądarce internetowej.
    """
    webbrowser.open(url)
    print(f"Artykuł został otwarty: {url}")

def main():
    """
    Główna funkcja programu.
    """
    tytul, url = pobierz_losowy_artykul()
    if zapytaj_uzytkownika(tytul):
        otworz_w_przegladarce(url)
    else:
        print("Nie otworzono artykułu.")

if __name__ == "__main__":
    main()
