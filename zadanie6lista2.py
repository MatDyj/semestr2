def generuj_dzialanie(dzialanie: str) -> str:
    """
    Generuje zapis działania w formie słupka.

    Parametry:
    dzialanie (str): Łańcuch znaków reprezentujący działanie (np. "235+72").

    Zwraca:
    str: Sformatowany słupek zawierający działanie i wynik.
    """
    for operator in ['+', '-', '*']:
        if operator in dzialanie:
            liczby = dzialanie.split(operator)
            if len(liczby) == 2 and liczby[0].isdigit() and liczby[1].isdigit():
                liczba1, liczba2 = map(int, liczby)
                wynik = eval(dzialanie)
                szerokosc = max(len(str(liczba1)), len(str(liczba2)))
                return f"""{str(liczba1).rjust(szerokosc)}
{operator} {str(liczba2).rjust(szerokosc-2)}
{'-' * szerokosc}
{str(wynik).rjust(szerokosc)}"""
print(generuj_dzialanie("235+72"))
print("                 ")
print(generuj_dzialanie("500-125"))
print("                 ")
print(generuj_dzialanie("12*8"))
