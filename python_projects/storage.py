from interfaces import DataSaver
import datetime

class FileSaver(DataSaver):
    def __init__(self, file_name):
        self.file_name = file_name


    def save_data(self, data):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        with open(self.file_name, "a", encoding="utf-8") as plik:
            plik.write(f" --- {time} --- {data} \n")