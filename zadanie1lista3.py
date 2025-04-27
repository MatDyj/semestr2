import os
import shutil
import datetime
import argparse

def znajdz_i_skopiuj(katalogi, rozszerzenia):
    """
    Szuka plików o zadanych rozszerzeniach w podanych katalogach i
    kopiuje zmodyfikowane w ciągu ostatnich 3 dni do katalogu Backup/copy-YYYY-MM-DD.

    Args:
        katalogi (list): Lista katalogów do przeszukania.
        rozszerzenia (list): Lista szukanych rozszerzeń (np. ['.txt', '.py']).
    """
    dzisiaj = datetime.date.today()
    backup_folder = os.path.join('Backup', f"copy-{dzisiaj}")
    os.makedirs(backup_folder, exist_ok=True)

    teraz = datetime.datetime.now()
    trzy_dni_temu = teraz - datetime.timedelta(days=3)

    for katalog in katalogi:
        for root, dirs, files in os.walk(katalog):
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in rozszerzenia):
                    sciezka_pliku = os.path.join(root, file)
                    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(sciezka_pliku))

                    if mtime >= trzy_dni_temu:
                        # Tworzymy strukturę katalogów w backupie
                        rel_path = os.path.relpath(root, katalog)
                        backup_path = os.path.join(backup_folder, rel_path)
                        os.makedirs(backup_path, exist_ok=True)

                        shutil.copy2(sciezka_pliku, backup_path)
                        print(f"Skopiowano: {sciezka_pliku} -> {backup_path}")

def main():
    parser = argparse.ArgumentParser(description="Kopiuje zmodyfikowane pliki do katalogu backupu.")
    parser.add_argument('katalogi', nargs='+', help="Lista katalogów do przeszukania.")
    parser.add_argument('--ext', nargs='+', required=True, help="Rozszerzenia plików do znalezienia, np. --ext .txt .py")

    args = parser.parse_args()

    znajdz_i_skopiuj(args.katalogi, args.ext)

if __name__ == "__main__":
    main()
