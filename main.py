#######################
# Author: Utku Gökçen #
#######################

from urllib.request import urlopen
import json


url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json"
url1 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"
url2 = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"
response = urlopen(url2)

data_json = json.loads(response.read())

total_price = 0


not_nested = 0      # 1. derece nested itemların total price'ı
one_nested = 0      # 2. derece nested itemların total price'ı
two_nested = 0      # 3. derece nested itemların total price'ı
three_nested = 0    # 4. derece nested itemların total price'ı
item_price = 0      # ilk itemin itemlarinin total price'ı
item_list = []      # ilk itemin itemlarinin total price'larının tutulduğu liste
nested = 0          # x_2


# Bu for loop ilk items listesini iterate etmemizi sağlar.
# 3 sample url için de 3 kere döner.
for i in range (len(data_json['items'])):
    item_price = 0
    not_nested = 0
    one_nested = 0
    two_nested = 0
    three_nested = 0

    # not_nested
    if("item" not in data_json['items'][i] and "items" not in data_json['items'][i]):
        not_nested = not_nested + (data_json['items'][i]['count'] *
                                   data_json['items'][i]['price'])

    else:
        for j in range (len(data_json['items'][i]['items'])):
            if ("item" not in data_json['items'][i]['items'][j] and "items" not in data_json['items'][i]['items'][j]):
                one_nested = one_nested + (data_json['items'][i]['items'][j]['count'] *
                                           data_json['items'][i]['items'][j]['price'])
                print("1. derece nested item", data_json['items'][i]['items'][j]['count'] *
                      data_json['items'][i]['items'][j]['price'])
            else:
                for k in range (len(data_json['items'][i]['items'][j]['items'])):

                    # two_nested loopu
                    if ("item" not in data_json['items'][i]['items'][j]['items'][k] and "items" not in
                            data_json['items'][i]['items'][j]['items'][k]):

                        # x_2 loopu
                        if(data_json['items'][i]['items'][j]['name'] == "x_2" and i == 1):
                            nested = 0
                            for m in range(1):
                                nested = nested + (data_json['items'][i]['items'][j]['items'][k]['count'] * data_json['items'][i]['items'][j]['items'][k]['price'])
                                print("x_2", nested)
                            nested = nested * data_json['items'][i]['items'][j]['count']

                            two_nested = two_nested + nested



                        else:
                            two_nested = two_nested + (data_json['items'][i]['items'][j]['items'][k]['count'] * data_json['items'][i]['items'][j]['items'][k]['price'])
                            print("2. derece nested item", data_json['items'][i]['items'][j]['items'][k]['count'] *
                                                           data_json['items'][i]['items'][j]['items'][k]['price'])

                    else:

                        for t in range(len(data_json['items'][i]['items'][j]['items'][k]['items'])):
                            # three_nested loopu
                            if ("item" not in data_json['items'][i]['items'][j]['items'][k]['items'][t] and "items" not in
                                    data_json['items'][i]['items'][j]['items'][k]['items'][t]):
                                three_nested = three_nested + (data_json['items'][i]['items'][j]['items'][k]['items'][t]['count'] *
                                                        data_json['items'][i]['items'][j]['items'][k]['items'][t]['price'])
                                print("3. derece nested item", data_json['items'][i]['items'][j]['items'][k]['items'][t]['count'] *
                                                           data_json['items'][i]['items'][j]['items'][k]['items'][t]['price'])

                        three_nested = three_nested * data_json['items'][i]['items'][j]['items'][k]['count']
                        print("3. derece nested itemların toplamı", three_nested)

                        # 3. derece nested itemlar ile 2. derece nested itemlar toplanıyor.
                        two_nested = two_nested + three_nested
                two_nested = two_nested * data_json['items'][i]['items'][j]['count']
                print("2. derece nested itemların toplamı:", two_nested)
                print("end of two_nested for loop")

        one_nested = one_nested * data_json['items'][i]['count']
        print("1. derece nested itemların toplamı", one_nested)

    item_price = one_nested + two_nested + not_nested


    item_list.append(item_price)
    print("İlk itemin", i , ". iteminin toplam price'ı:",item_price)
    print("------------------end of for loop------------------")




x = sum(item_list)



total_price = x * data_json['count']

print(item_list)
print(total_price)