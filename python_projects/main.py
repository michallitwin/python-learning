from api import OpenWeatherMap, NbpCurrency, CryptoAPI
from storage import FileSaver
from app import Daily_assistant


def main():
    api = OpenWeatherMap("x")
    api2 = CryptoAPI("x")
    file_save = FileSaver("notebook.txt")
    currency_worker = NbpCurrency()
    assistant = Daily_assistant(api, currency_worker, api2, file_save)

    assistant.start_aplication(category="crypto", crypto_name="Bitcoin")


if __name__ == "__main__":
    main()
