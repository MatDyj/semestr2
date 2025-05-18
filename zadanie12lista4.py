import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def seir_model(y, t, N, beta, sigma, gamma):
    """
    Funkcja definiująca układ równań różniczkowych modelu SEIR.

    Parametry:
    y     -- lista z aktualnymi wartościami S, E, I, R
    t     -- czas (nie jest używany bezpośrednio, ale wymagany przez odeint)
    N     -- całkowita populacja
    beta  -- wskaźnik infekcji
    sigma -- wskaźnik inkubacji
    gamma -- wskaźnik wyzdrowień

    Zwraca:
    [dSdt, dEdt, dIdt, dRdt] -- pochodne funkcji w czasie t
    """
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

def main():
    """
    Główna funkcja programu. Parsuje argumenty z linii poleceń,
    uruchamia model SEIR i wyświetla wykres.
    """
    parser = argparse.ArgumentParser(description='Symulacja modelu SEIR')

    parser.add_argument('-N', type=int, default=1000, help='Całkowita populacja')
    parser.add_argument('-S0', type=int, default=999, help='Liczba osób podatnych na początku')
    parser.add_argument('-E0', type=int, default=0, help='Liczba osób eksponowanych na początku')
    parser.add_argument('-I0', type=int, default=1, help='Liczba osób zarażonych na początku')
    parser.add_argument('-R0', type=int, default=0, help='Liczba osób wyzdrowiałych na początku')
    parser.add_argument('-beta', type=float, default=1.34, help='Współczynnik transmisji (beta)')
    parser.add_argument('-sigma', type=float, default=0.19, help='Współczynnik inkubacji (sigma)')
    parser.add_argument('-gamma', type=float, default=0.34, help='Współczynnik wyzdrowień (gamma)')
    parser.add_argument('-days', type=int, default=160, help='Liczba dni symulacji')

    args = parser.parse_args()
    N = args.N
    S0, E0, I0, R0 = args.S0, args.E0, args.I0, args.R0
    beta, sigma, gamma = args.beta, args.sigma, args.gamma
    t = np.linspace(0, args.days, args.days)
    y0 = [S0, E0, I0, R0]
    ret = odeint(seir_model, y0, t, args=(N, beta, sigma, gamma))
    S, E, I, R = ret.T
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label='S - Podatni')
    plt.plot(t, E, label='E - Eksponowani')
    plt.plot(t, I, label='I - Zakażeni')
    plt.plot(t, R, label='R - Odzyskani')
    plt.xlabel('Czas (dni)')
    plt.ylabel('Liczba osób')
    plt.title('Model SEIR (argumenty w stylu uniksowym)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Uruchomienie programu, jeśli plik jest wykonywany bezpośrednio
if __name__ == '__main__':
    main()