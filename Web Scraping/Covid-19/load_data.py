import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import date


def load_data():
    url = "https://www.worldometers.info/coronavirus/#countries"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('tbody')
    country_data = []
    TotalCases_data = []
    NewCases_data = []
    TotalDeaths_data = []
    NewDeaths_data = []
    TotalRecovered_data = []
    ActiveCases_data = []
    CriticalCases_data = []
    Totcase1M_data = []
    Totdeath1M_data = []
    TotalTests_data = []
    Tottest1M_data = []
    Population_data = []
    rows = table.findAll('tr')
    for row in rows:
        row_data = []
        for cell in row.findAll('td'):
            row_data.append(cell.text)
        if(len(row_data) > 0):
            country_data.append(row_data[1])
            TotalCases_data.append(row_data[2])
            NewCases_data.append(row_data[3])
            TotalDeaths_data.append(row_data[4])
            NewDeaths_data.append(row_data[5])
            TotalRecovered_data.append(row_data[6])
            ActiveCases_data.append(row_data[7])
            CriticalCases_data.append(row_data[8])
            Totcase1M_data.append(row_data[9])
            Totdeath1M_data.append(row_data[10])
            TotalTests_data.append(row_data[11])
            Tottest1M_data.append(row_data[12])
            Population_data.append(row_data[13])
        else:
            print("EHHHHH error occured: row length is 0")
    date_lst = [date.today()]*len(country_data)
    table_dict = {'Date': date_lst, 'Country': country_data, "TotalCases": TotalCases_data, "NewCases": NewCases_data, "TotalDeaths": TotalDeaths_data, "NewDeaths": NewDeaths_data, "TotalRecovered": TotalRecovered_data,
                  "ActiveCases": ActiveCases_data, "CriticalCases": CriticalCases_data, "Totcase1M": Totcase1M_data, "Totdeath1M": Totdeath1M_data, "TotalTests": TotalTests_data, "Tottest1M": Tottest1M_data, "Population": Population_data}
    df = pd.DataFrame(table_dict)
    df = df.loc[8:, :]

    def comma_remover(col_name):
        result = []
        for num in df[col_name]:
            result.append(num.replace(',', ''))
        df[col_name] = result
        df[col_name] = pd.to_numeric(
            df[col_name], errors='coerce', downcast='integer')
    for col in df.columns[2:]:
        comma_remover(col)
        df[col] = df[col].fillna(np.nan)
    return df.reset_index(drop=True)


if __name__ == '__main__':
    df = load_data()
    df.to_csv('data.csv', index=False)
