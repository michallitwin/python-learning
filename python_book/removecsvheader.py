#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.
import csv, os

#tworzy zagniezdzone foldery
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    with open(csvFilename, mode='r', encoding='utf-8', newline='') as csvFileObj:
        #csv nie czyta całego pliku na raz tylko seriami, automatycznie tnie tekst w miejscach przecinków i nie tnie tekstu w środku cudzysłowu 
        readerObj = csv.reader(csvFileObj)
        #tutaj omijamy naglowek - to jest takie przesuniecie o jeden, a None jako drugi argument zabezpiecza nas przez wywaleniem programu 
        #przykladowo nic w pliku nie jest napisane to wysweitli sie None a nie wywali program
        next(readerObj, None)

        for row in readerObj:

            csvRows.append(row)

    outputFilePath = os.path.join('headerRemoved', csvFilename)

    with open(outputFilePath, mode='w', encoding='utf-8', newline='') as csvFileObj:
        writerObj = csv.writer(csvFileObj)
        writerObj.writerows(csvRows)



