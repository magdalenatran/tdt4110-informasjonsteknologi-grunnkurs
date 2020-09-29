def write_to_file(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename, 'r')
    content = f.read()
    print(content)
    f.close()

def main():
    to_do = ''
    while to_do != 'done':
        to_do = input('Do you want to read or write (r/w)? ')

        if to_do == 'w':
            data = input('What do you want to write to file? ')
            write_to_file(data)
        elif to_do == 'r':
            try:
                read_from_file('my_file.txt')
            except Exception as variabel:
                print(variabel)
    print('You are done')


main()