import json
import re

def record_json_data(filename):
    data = []
    with open(filename) as data_file:
        for line in data_file:
            data.append(json.loads(line))
    return data

if __name__ == '__main__':
    listings=record_json_data('listings.txt') #currency, price, manufacturer, title
    products=record_json_data('products.txt') #model,family(optional), announced-date, product_name, manufacturer

    matched_list= []

    for line in products:
        value = {"product_name":line['product_name'],
                "listings":[]
                }
        matched_list.append(value)


    for line in listings:
        a=line['title']
        test = 0
        for lines in products:
            if line['manufacturer'] == lines['manufacturer']:
                if a.find(' '+lines['model']+' ') > -1:
                    if 'family' in lines: #double check with family, if possible
                        if a.find(lines['family']+' ') > -1:
                            matched_list[test]['listings'].append(line)
                            test +=1
                            break
                        else:
                            test +=1
                            continue
                    else: # if no family, it still matches so far
                        matched_list[test]['listings'].append(line)
                        test +=1
                        break
                else:
                    test +=1
            else:
                test +=1

    output = open('results.txt','w')
    for item in matched_list:
        print>>output, json.dumps(item)
    output.close()
