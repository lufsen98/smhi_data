import requests
def get_data(url):
    response = requests.get(url)

    data = response.json()
    return data

    
