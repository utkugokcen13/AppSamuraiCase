from urllib.request import urlopen
import json

url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json"
url1 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"
url2 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"
response = urlopen(url1)

data_json = json.loads(response.read())

total_price = 0
not_nested = 0
one_nested = 0
two_nested = 0

# print the json response
for i in range (len(data_json['items'])):
    if("item" not in data_json['items'][i] and "items" not in data_json['items'][i]):
        #print(data_json['items'][i]['count'] * data_json['items'][i]['price'])
        total_price = total_price + (data_json['items'][i]['count'] * data_json['items'][i]['price'])
    else:
        for j in range (len(data_json['items'][i]['items'])):
            if ("item" not in data_json['items'][i]['items'][j] and "items" not in data_json['items'][i]['items'][j]):
                #print(data_json['items'][i]['items'][j]['count'] * data_json['items'][i]['items'][j]['price'])
                total_price = total_price + (data_json['items'][i]['items'][j]['count'] * data_json['items'][i]['items'][j]['price'])
            else:
                for k in range (len(data_json['items'][i]['items'][j]['items'])):
                    if ("item" not in data_json['items'][i]['items'][j]['items'][k] and "items" not in
                            data_json['items'][i]['items'][j]['items'][k]):
                        #print(data_json['items'][i]['items'][j]['items'][k]['count'] * data_json['items'][i]['items'][j]['items'][k]['price'])
                        total_price = total_price + (
                                    data_json['items'][i]['items'][j]['items'][k]['count'] * data_json['items'][i]['items'][j]['items'][k][
                                'price'])

                #total_price = total_price * data_json['items'][i]['items'][j]['count']
        #total_price = total_price * data_json['items'][i]['count']


#total_price = total_price * data_json['count']

print(total_price)