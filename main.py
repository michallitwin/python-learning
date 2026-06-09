import pandas as pd

def get_category(price, low, high):
    if price < low:
        return "tanio"
    elif price <= high:
        return "srednio"
    else:
        return "drogo"
    

def get_quantity(price, alot, few):
    if price < few:
        return "malo"
    elif price <= alot:
        return "srednio"
    else:
        return "duzo"

def add_price_category(df, low=50, high=150, alot=50, few=5):
    df_copy = df.copy()

    df_copy['kategoria'] = df_copy['cena'].apply(lambda x: get_category(x, low, high))
    df_copy['sprawdzanie'] = df_copy['ilosc'].apply(lambda x: get_quantity(x, alot, few))

    return df_copy


dane = {
    'cena': [10, 15, 5, 151],
    'ilosc': [1, 2, 11, 231],
    'przedmioty': ['woda', 'piwo', 'frytki', "kebab"]
    
}
a1 = pd.DataFrame(dane)
print(add_price_category(a1))