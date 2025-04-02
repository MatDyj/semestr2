import random


def haslo(dlugosc=8):
    """
    Generuje losowe hasło o zadanej długości.
    
    :param dlugosc: Długość hasła (domyślnie 8 znaków)
    :return: Wygenerowane hasło
    """
    znaki = list(range(33, 127)) #Zakres kodow ASCII#
    return ''.join(chr(random.choice(znaki)) for _ in range(dlugosc))
print("Haslo: ", haslo())