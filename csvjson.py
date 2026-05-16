import csv
# encoding utf 8 pozwala na polskie znaki - inaczej by wywalilo kod 
# newline zawsze sie dodaje zeby nie dodawalo pustych enterow 
with open('example.csv', mode='r', encoding='utf-8', newline='') as exampleFile:
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    for i, e in enumerate(exampleData):
        print(f"#{i} {e}")


with open('output.csv', mode='w', encoding='utf-8', newline='') as outputFile:
    outputWriter = csv.writer(outputFile)
    #WRITEROW ZAPISUJE WIERSZ i zwraca liczbe znakow z przecinkami i wcieciami 
    outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
    outputWriter.writerow(['abcd', 12, 'dupaa'])



with open('example.tsv', mode='w', encoding='utf-8', newline='') as csvFile:
    # Ustawiamy tabulator jako separator i wymuszamy podwójny enter jako koniec wiersza
    csvWriter = csv.writer(csvFile, delimiter='#', lineterminator='\n\n dupa')
    # lineterminator wstawiamy tam czym chcemy zakonczyc dany wiersz
    #  a delimiter ustawia czym separujemy dane 
    csvWriter.writerow(['apples', 'oranges', 'grapes'])
    csvWriter.writerow('Dupa')
    csvWriter.writerow(['abcd', 'dupa'])
    csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

#CSV (.csv) używa przecinków (,) jako separatora kolumn, co jest uniwersalnym standardem dla arkuszy kalkulacyjnych.
#  TSV (.tsv) używa tabulatorów (\t), co czyni go bezpieczniejszym formatem, gdy wewnątrz samych danych 
# często pojawiają się przecinki lub cudzysłowy