import re

colors = [
    'black', 'dark_gray', 'light_gray', 'white', 'brown', 
    'pink', 'magenta', 'purple', 'blue', 'light_blue', 
    'cyan', 'green', 'lime', 'yellow', 'orange', 'red'
]
input_model_files = ['input/models/block/chair.json', 'input/models/block/chair_left.json', 'input/models/block/chair_right.json', 'input/models/block/chair_both.json']

for input_file in input_model_files:
    with open(input_file, 'r') as file:
        content = file.read()
        for color in colors:
            updated_json = re.sub(r'\$\{COLOR\}', color, content)
            filename = 'output/models/' + color + '_' + input_file.split('/')[3]
            with open(filename, 'w') as file:
                file.write(updated_json)
            print(f'File "{filename}" written.')
            
with open('input/models/item/chair.json', 'r') as file:
    content = file.read()
    for color in colors:
        updated_json = re.sub(r'\$\{COLOR\}', color, content)
        filename = 'output/models/item/' + color + '_chair.json'
        with open(filename, 'w') as file:
            file.write(updated_json)
        print(f'File "{filename}" written.')
        
with open('input/blockstates/chair.json', 'r') as file:
    content = file.read()
    for color in colors:
        updated_json = re.sub(r'\$\{COLOR\}', color, content)
        filename = 'output/blockstates/' + color + '_chair.json'
        with open(filename, 'w') as file:
            file.write(updated_json)
        print(f'File "{filename}" written.')
        
with open('input/loot_tables/chair.json', 'r') as file:
    content = file.read()
    for color in colors:
        updated_json = re.sub(r'\$\{COLOR\}', color, content)
        filename = 'output/loot_tables/' + color + '_chair.json'
        with open(filename, 'w') as file:
            file.write(updated_json)
        print(f'File "{filename}" written.')
        
with open('input/recipes/chair.json', 'r') as file:
    content = file.read()
    for color in colors:
        updated_json = re.sub(r'\$\{COLOR\}', color, content)
        filename = 'output/recipes/' + color + '_chair.json'
        with open(filename, 'w') as file:
            file.write(updated_json)
        print(f'File "{filename}" written.')

with open('input/recipes/chair_from_seat.json', 'r') as file:
    content = file.read()
    for color in colors:
        updated_json = re.sub(r'\$\{COLOR\}', color, content)
        filename = 'output/recipes/' + color + '_chair_from_seat.json'
        with open(filename, 'w') as file:
            file.write(updated_json)
        print(f'File "{filename}" written.')