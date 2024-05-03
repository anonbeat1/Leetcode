import sys

input_string = '''3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry'''

hashmap = {}
def handle_data(data):
    for x in data.split('\n'):
        splitted_data = x.split(' ')
        if len(splitted_data) > 1:
            # print(splitted_data,splitted_data[0],splitted_data[1])
            name = splitted_data[0]
            number = splitted_data[1]
            hashmap[name] = number
        elif len(hashmap) > 0 :
            if x in hashmap.keys():
                print("{}={}".format(x,hashmap.get(x)))
            else:
                print("Not found")
            
            
handle_data(input_string)
