import os
import zipfile
import datetime

def kopia_zapasowa(katalog, wyjscie):

    wyjscie=f"{wyjscie}_kopia_{datetime.date.today()}.zip "
    with zipfile.ZipFile(wyjscie, 'w', zipfile.ZIP_BZIP2) as zipek:
        for root, dirs, files in os.walk(katalog):
            for file in files:
                sciezka_pliku=os.path.join(root, file)
                zipek.write(sciezka_pliku, os.path.relpath(sciezka_pliku, katalog))
    print(f"Stworzono kopie zapasowa dla katalogu: {katalog}")    
kopia_zapasowa("dokopii", "kopia")        
