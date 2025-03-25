import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd

# Funkcja do wczytywania pliku CSV z URL
def load_csv_from_url(url):
    return pd.read_csv(url)

# Interfejs użytkownika w Streamlit
def main():
    st.title("Aplikacja do porównywania raportu z pełną bazą danych")
    
    # Podane URL do plików CSV
    url_prod_price = "https://scommercegroup.sharepoint.com/source/db/data_prod_price.csv"
    url_prod_data = "https://scommercegroup.sharepoint.com/source/db/products_s_data.csv"
    
    # Wczytanie plików CSV z URL
    try:
        full_db_price = load_csv_from_url(url_prod_price)
        full_db_data = load_csv_from_url(url_prod_data)
        
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
