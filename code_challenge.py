## Sortable Coding Challenge
# Written by: Josh Borovoy
# Completed on: August 9th, 2016
## Take a list of products with information and compare it to a set of listings potentially related to each product in the list and match them up

import json #needed for the JSON manipulation

def record_json_data(filename):
    data = [] #initialize array that will become the data from each file
    with open(filename) as data_file: # open the file
        for line in data_file: # go through each line of the input file
            data.append(json.loads(line)) #load the JSON file in
    return data

if __name__ == '__main__':
    listings=record_json_data('listings.txt') #currency, price, manufacturer, title
    products=record_json_data('products.txt') #model,family(optional), announced-date, product_name, manufacturer

    matched_list= []

    for line in products:
        value = {"product_name":line['product_name'],
                "listings":[] #create product name with listings dictionary list
                }
        matched_list.append(value) # add the line to the product name


    for line in listings:
        count = 0 # initialize the number to co-incide with the matched_list
        for lines in products:
            if line['manufacturer'] == lines['manufacturer']: #check manufacturer first because the data is in both files. Easiest check
                if line['title'].find(' '+lines['model']+' ') > -1: # check for the name of the model in the title (ensure that the model name won't be part of another model name with spaces)
                    if 'family' in lines: #double check with family, if possible
                        if line['title'].find(lines['family']+' ') > -1: # when checking for the model, to ensure that it's not part of another product's name look for a space before and after
                            matched_list[count]['listings'].append(line) # add the listing value to the appropraite product_name, array set up before
                            count +=1
                            break
                        else:
                            count +=1
                            continue
                    else: # if no family, it still matches so far
                        matched_list[count]['listings'].append(line)
                        count +=1
                        break
                else:
                    count +=1
            else:
                count +=1

    output = open('results.txt','w') # open a file to write the item to
    for item in matched_list: # go through each item in the array containing the matched items
        print>>output, json.dumps(item) # print each dictionary in the array line by line
    output.close() # close the file, end the program
