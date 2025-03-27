#importing necessary libraries
import requests
import json
import pandas as pd


url0 = "https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&api-key=d0ac108d-74c9-4cab-b358-a2de26b84787"

#calling the endpoint
response_0 = requests.get(url0)
response_0.status_code # checking status code

#converting the response to json
guardian_api = response_0.json()

# checking the keys in the response dictionary
guardian_api.keys()

# extracting the required data from the response
article = guardian_api['response']['results']
article

# converting the data into a pandas dataframe
result = pd.DataFrame(article)
result

# converting to csv
result.to_csv('guardian_articles.csv', index=True)

