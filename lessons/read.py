'''
ipsum_file = open('files/ipsum.txt')


for line in ipsum_file:
    print(line.rstrip())

ipsum_file.seek(0) #tornar l'índex al principi

lines = ipsum_file.readlines()
print(lines)


ipsum_file.seek(10)
file_text = ipsum_file.read(5)
print(file_text)

ipsum_file.close()
'''

def sequence_filter(line):
    return '>' not in line

with open('files/ipsum.txt') as ipsum_file:
    lines = ipsum_file.readlines()
    print(list(filter(sequence_filter,lines)))