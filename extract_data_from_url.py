import requests
def get_data_from_url(apikey,url):
    params = {
        "apikey":apikey
    }
    response = requests.get(url=url,params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

# print(get_data_from_url("YdH3zeYkA1CxeAUlU8AJWhMIyAEKF2ePJVBCzoJC","https://api.currencyapi.com/v3/currencies?"))