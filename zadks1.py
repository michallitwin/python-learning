import os
#pdf reader sluzy do czytnia i tlumaczenia pdf, a pdf writer do tworzenia szyfrowania pdf 
from pypdf import PdfReader, PdfWriter


# 1. KONFIGURACJA
haslo = 'abc'  # Tutaj ustaw swoje hasło
pdfy_do_obrobki = []

for folder_obecny, _, pliki in os.walk("."):
    for plik in pliki:
        pelna_sciezka = os.path.join(folder_obecny, plik)
        # Bierzemy tylko PDFy, które NIE SĄ już zaszyfrowane przez nas, bez tego program by chcial blokowac to co zablokowane
        if plik.endswith(".pdf") and not plik.endswith("_encrypted.pdf"):
            pdfy_do_obrobki.append(pelna_sciezka)

print(f"Znaleziono {len(pdfy_do_obrobki)} plików do zabezpieczenia.")

# 3. tutaj przechodzimy przez nieprzerobione pdfy, jesli jakis plik bedzie uszkodzony to program leci dalej 
for pdf_sciezka in pdfy_do_obrobki:
    try:
        # --- ETAP A: SZYFROWANIE ---
        #pdfwriter tworzy pusty nowy pdf 
        writer = PdfWriter()
        #otwieramy oryginal do odczytu
        reader = PdfReader(pdf_sciezka)

#kopiujemy strony do naszego nowego pustego pliku
        for strona in reader.pages:
            writer.add_page(strona)

#tutaj nakladamy na niego haslo i przygotowyjemy nazwe dla nszego pliku 
        writer.encrypt(haslo)
        nowa_nazwa = pdf_sciezka.replace('.pdf', '_encrypted.pdf')

#oznacza to stworz nowy plik jesli go nie ma i przyogtuj sie na pisanie binarne
        with open(nowa_nazwa, 'wb') as f_out:
            #tutaj zapisujemy te dane na dysku z ramu 
            writer.write(f_out)

        # Sprawdzamy, czy nowo powstały plik faktycznie działa
        test_reader = PdfReader(nowa_nazwa)
        
        # decrypt() zwraca status sukcesu (zazwyczaj 1 lub 2 w pypdf)
        if test_reader.decrypt(haslo):
            # --- ETAP C: EGZEKUCJA ---
            # Jeśli test przeszedł, mamy zielone światło na usunięcie oryginału
            os.remove(pdf_sciezka)
            print(f"[OK] Zaszyfrowano i zweryfikowano: {nowa_nazwa}. Oryginał usunięty.")
        else:
            print(f"[BŁĄD] Weryfikacja nieudana dla {nowa_nazwa}! Oryginał zostaje.")

    except Exception as e:
        print(f"[CRITICAL] Problem z plikiem {pdf_sciezka}: {e}")

print("\nRobota skończona!")