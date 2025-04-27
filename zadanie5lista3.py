def nawias(wyrazenie):
    """
    Sprawdza poprawność nawiasów w podanym wyrażeniu.
    Zwraca True, jeśli nawiasy są poprawne, w przeciwnym razie False.
    """
    stos = []
    nawiasy = {')': '(', ']': '[', '}': '{'}
    
    for znak in wyrazenie:
        if znak in nawiasy.values():  # jeśli to nawias otwierający
            stos.append(znak)
        elif znak in nawiasy.keys():  # jeśli to nawias zamykający
            if not stos or stos[-1] != nawiasy[znak]:
                return False
            stos.pop()
    
    return len(stos) == 0

def main():
    """
    Główna funkcja programu.
    """
    wyrazenie = input("Podaj wyrażenie do sprawdzenia nawiasów: ")
    if nawias(wyrazenie):
        print("Nawiasy są poprawnie użyte.")
    else:
        print("Nawiasy są niepoprawne!")

if __name__ == "__main__":
    main()
