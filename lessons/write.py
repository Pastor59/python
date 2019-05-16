with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there ninjas, python is awesome')
    write_file.write('\nSome random text')

#la a per a que no esborri el que hi havia escrit
with open('files/write.txt', 'a') as write_file:
    write_file.write('\naaaa')

quotes = [
    '\nI can resist everything',
    '\nWe are all in the gutter',
    '\nAlways forgive'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)