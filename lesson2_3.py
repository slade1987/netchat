import os
import yaml

def save_yaml():
    file_path = os.path.abspath('file.yaml')
    data = {
        'items': ['C++', 'Python', 'C#', 'html'],
        'items_quentity': 4,
        'items_price': {
            'C++': '20€-100€',
            'Python': '20€-1000€',
            'C#': '30€-300€',
            'html': '2€-10€'
        }
    }

    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

    with open(file_path) as file:
        print(file.read())