import requests, json, sentiments

url = "https://hotels4.p.rapidapi.com/reviews/v2/list"

querystring = {"hotelId":"316987","reviewOrder":"date_newest_first","tripTypeFilter":"all"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "df90126f64msh03609b1cbd7cd7fp1923bcjsnaeb213e475ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = dict(json.loads(response.text))
descriptions = []

description = data["data"]["reviews"]["body"]["reviewContent"]["reviews"]["hermes"]["groups"][0]["items"][0]["description"]

print(description)
sentiments.payload["txt"] = description
