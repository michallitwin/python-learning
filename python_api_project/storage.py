from interfaces import DataSaver
import datetime
import os 
import csv


class TxtSaver(DataSaver):
    def __init__(self, file_name):
        self.file_name = file_name


    def save_data(self, data):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        change_text = ", ".join([f"{key}: {value}" for key, value in data.items()])

        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(f" --- {time} --- {change_text} \n")


class CsvSaver(DataSaver):
    def __init__(self, file_name):
        self.file_name = file_name

    def save_data(self, data):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        row_to_save = {"timestamp": time, **data}
        file_exist = os.path.exists(self.file_name)
        fieldnames = list(row_to_save.keys())
        with open(self.file_name, "a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames)
            if not file_exist:
                writer.writeheader()
            writer.writerow(row_to_save)