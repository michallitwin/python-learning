from api import OpenWeatherMap, NbpCurrency
from storage import FileSaver
from app import Daily_assistant



def main():
    api = OpenWeatherMap("x")
    file_save = FileSaver("notebook.txt")
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(api,currency_worker,file_save)

    assistant.start_aplication("currency","AUD")

if __name__ == "__main__":
    main()