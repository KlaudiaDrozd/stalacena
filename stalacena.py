import streamlit as st
import pandas as pd
import requests

# Funkcja do pobierania plików z SharePoint
def load_csv_from_sharepoint(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return pd.read_csv(pd.compat.StringIO(response.text))
    else:
        st.error(f"Nie udało się pobrać danych z URL: {response.status_code}")
        return None

# Interfejs użytkownika w Streamlit
def main():
    st.title("Aplikacja do porównywania raportu z pełną bazą danych")

    # URL do plików CSV w chmurze
    url_prod_price = "https://scommercegroup.sharepoint.com/:x:/r/sites/ZAKUPY/Shared%20Documents/Raporty/.data_source/db/data_prod_price_.csv?d=wc7bfcbe9ffeb4d8ebc099f327b34a5ab&csf=1&web=1&e=spfrRB"
    url_prod_data = "https://scommercegroup.sharepoint.com/:x:/r/sites/ZAKUPY/Shared%20Documents/Raporty/.data_source/db/products_s_data.csv?d=w79e4d83752c84acb931ee0a682af12e6&csf=1&web=1&e=nDqKvY"

    # Jeśli pliki są zabezpieczone, dodaj token w nagłówkach
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Zastąp "YOUR_ACCESS_TOKEN" rzeczywistym tokenem
    }

    # Wczytanie plików CSV z SharePoint
    try:
        full_db_price = load_csv_from_sharepoint(url_prod_price, headers)
        full_db_data = load_csv_from_sharepoint(url_prod_data, headers)
        
        if full_db_price is not None and full_db_data is not None:
            st.write("Dane z bazy danych - ceny produktów:")
            st.dataframe(full_db_price.head())  # Pokazujemy tylko kilka pierwszych wierszy
            
            st.write("Dane z bazy danych - szczegóły produktów:")
            st.dataframe(full_db_data.head())  # Pokazujemy tylko kilka pierwszych wierszy
    except Exception as e:
        st.error(f"Nie udało się załadować danych z URL: {e}")
    
    # Wgrywanie pliku raportu
    report_file = st.file_uploader("Wybierz plik z raportem", type=["xlsx", "xls"])
    
    if report_file:
        # Wczytanie pliku raportu
        report = pd.read_excel(report_file)
        st.write("Dane z raportu:")
        st.dataframe(report.head())  # Pokazujemy tylko kilka pierwszych wierszy

if __name__ == "__main__":
    main()
