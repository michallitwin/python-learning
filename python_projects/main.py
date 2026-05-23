from api import OpenWeatherMap, NbpCurrency
from storage import FileSaver
from app import Daily_assistant



def main():
    first = OpenWeatherMap("x")
    second = FileSaver("notebook.txt")
    currency_worker = NbpCurrency()
    third = Daily_assistant(first,currency_worker,second)

    third.uruchom("currency","EUR")

if __name__ == "__main__":
    main()