def read_already_existing():
    global materials
    try:
        with open('materials.txt', 'r') as f:
            mats = f.read().replace("'", "").replace(" ", "").strip('[]')
            materials = mats.split(',')
            print("Materiaux precedents charges")
    except FileNotFoundError:
        print('Fichier non existant')

def save_to_file():
    with open('materials.txt', 'w+') as f:
        f.write(str(materials).replace("'',", ""))
    print("Materiaux sauvegardes")

def check_if_exists(new_material):
    for material in materials:
        if new_material == material:
            print("Ce materiau existe deja")
            return

def main():
    prefix = 'wishtorio:'
    run = True
    read_already_existing()
    while run:
        try:
            new_material = prefix + str(input('Nom >> ')).strip(" ")
            if not check_if_exists(new_material):
                materials.append(new_material)
        except KeyboardInterrupt:
            save_to_file()
            exit()

main()