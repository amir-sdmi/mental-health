import requests

base_url = "http://127.0.0.1:5000/"
endpoint = "data/Canada/2010/2015"
query_params = "?Schizophrenia=true&Bipolar-disorder=true&Eating-disorders=true&Anxiety-disorders=true&Drug-use-disorders=true&Depression=true&Alcohol-use-disorders=true&Life-Ladder=true&GDP=true&Social-support=true&Healthy-life-expectancy-at-birth=true&Freedom-to-make-life-choices=true&Generosity=true&Perceptions-of-corruption=true&Positive-affect=true&Negative-affect=true&Confidence-in-national-government=true"
full_url = f"{base_url}{endpoint}{query_params}"

try:
    response = requests.get(full_url)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Oops: Something Else", err)
