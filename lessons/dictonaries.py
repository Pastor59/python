def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')
    
    print(f'Imprimir les claus', dictionary.keys())
    print(f'Imprimir en numero de claus', len(dictionary.keys()))
    print(f'Mira si un string es clau', "jordi" in dictionary)
    print(f'Mira tots els valors', dictionary.values())
    print(f'Lista tots els valors', list(dictionary.values()))
    print(f'Mirar quants cops esta repetit un valor', list(dictionary.values()).count('red'))

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name:')
    ninja_belt = input('enter a belt colour:')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

#ninja_intro(ninja_belts)
belt_count(ninja_belts)