import json
import os

def clear():
    os.system('cls')
    

def load_data():
    try:
        with open('tiles.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    try:
        with open('tiles.json', 'w+') as f:
            f.write(json.dumps(data))
    except Exception as e:
        print(e)
        pass
    
def new_tile():
    generated_resource = None
    generating_time = None
    generator_energy_cost = None
    number_of_generated_resource = None

    number_of_slots = None

    clear()
    print('''
          | Tile creator |
          ''')
    print(f'Name: ? | Type: ? | Size: (?, ?)')
    print(f'Tile name (without "{prefix}")')
    name = prefix + input('>> ')

    clear()
    print('''
          | Tile creator |
          ''')
    print(f'Name: {name} | Type: ? | Size: (?, ?)')
    print('Tile type | [0] default | [1] generator | [2] inventory')
    try: 
        type = int(input('>> '))
    except:
        type = 0
    
    if type == 1:
        clear()
        print('''
          | Tile creator |  
              ''')
        print(f'Name: {name} | Type: {type} (Generates: ? of ? every ?s for ?🔋) | Size: (?, ?)')
        print(f'Generated resource name (without "{prefix}")')
        generated_resource = prefix + str(input('>> '))
    
        clear()
        print('''
          | Tile creator |  
              ''')
        print(f'Name: {name} | Type: {type} (Generates: ? of {generated_resource} every ?s for ?🔋) | Size: (?, ?)')
        print('Generator cooldown (default 3s)')
        try:
            generating_time = float(input('>> '))
        except:
            generating_time = 3.
        
        clear()
        print('''
          | Tile creator |  
              ''')
        print(f'Name: {name} | Type: {type} (Generates: ? of {generated_resource} every ?s for ?🔋) | Size: (?, ?)')
        print('Number of generated resource (default 1)')
        try:
            number_of_generated_resource = int(input('>> '))
        except:
            number_of_generated_resource = 1
            
        clear()
        print('''
          | Tile creator |  
              ''')
        print(f'Name: {name} | Type: {type} (Generates: {number_of_generated_resource} of {generated_resource} every ?s for ?🔋) | Size: (?, ?)')
        print('Energy cost (default 1)')
        try:
            generator_energy_cost = int(input('>> '))
        except:
            generator_energy_cost = 1
    if type == 2:
        clear()
        print('''
          | Tile creator |  
              ''')
        print(f'Name: {name} | Type: {type} (Stores: ?slot) | Size: (?, ?)')
        print(f'Number of slots')
        try:
            number_of_slots = int(input('>> '))
        except:
            number_of_slots = 50
    
    clear()
    print('''
          | Tile creator |
          ''')
    print(f'Name: {name} | Type: {type} (Generates: {number_of_generated_resource} of {generated_resource} every {generating_time}s for {generator_energy_cost}🔋) | Size: (?, ?)')
    print('Tile size | w h | 1x2 | 2x2 | 2x1 ')
    try:
        size_width = int(input('w >> '))
        size_height = int(input('h >> '))
        size = (size_width, size_height)
    except:
        size = (1, 1)
    
    clear()
    print('''
          | Tile creator |
          ''')
    print(f'Name: {name} | Type: {type} (Generates: {number_of_generated_resource} of {generated_resource} every {generating_time}s for {generator_energy_cost}🔋) | Size: {size}')
    
    match type:
        case 0:
            tiles[name] = {
                'type': type,
                'size': size,
            }
        case 1:
            tiles[name] = {
                'type': type,
                'size': size,
                'generated_resource': generated_resource,
                'generating_time': generating_time,
                'number_of_generated_resource': number_of_generated_resource,
                'generator_energy_cost': generator_energy_cost
            }
        case 2:
            tiles[name] = {
                'type': type,
                'size': size,
                'number_of_slots': number_of_slots
            }
            
    if autosave: save_data(tiles)
    
def show_tiles():
    clear()
    names = []
    for tile in tiles:
        names.append(tile)
    print(names)
    
    input()
    
def delete_tile():
    clear()
    print('''
          | Delete tile |
          ''')
    print(f'Enter the name of the tile to delete (without "{prefix}")')
    name = prefix + str(input('>> '))
    if tiles[name] in tiles:
        tiles.pop(name)
        print(f'Tile "{name}" deleted')
    else:
        print('This tile doesn\'t exist')
    
def menu():
    clear()
    print('''
          | (n)ew tile | (s)how tiles | (d)elete tile | (q)uit & save |
          ''')
    choice = str(input(">> "))
    match choice:
        case "n":
            new_tile()
        case "s":
            show_tiles()
        case "d":
            delete_tile()
        case "q":
            save_data(tiles)
            exit()

def main():
    global tiles, prefix, autosave

    print('''
          | Wishtorio tile creator |
          ''')
    run = True
    autosave = True
    prefix = 'wishtorio:'
    tiles = load_data()
    while run:
        try:
            menu()
        except KeyboardInterrupt:
            clear()
            exit()
    pass

if __name__ == '__main__':
    main()