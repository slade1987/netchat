import json, os

def  write_order_to_json(item:str,quantity:int, price:int, buyer:str, date:str):
    file_path = os.path.abspath('json.json')
    data = {}
    if os.path.exists(os.path.abspath('json.json')):
        with open(file_path, 'r') as file:
            data = json.loads(file.read())
            print(data)

        data = str(data) + str({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
         })

        with open(file_path, 'w') as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)
    else:
        data = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
         }

        with open(file_path, 'w') as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)