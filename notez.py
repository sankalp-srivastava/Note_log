from datetime import datetime
import sys


def write_note():
    print("Write Your Multiline entry")
    print("Enter '/End/' in new line to end note")
    note = ""
    line = ""
    while True:
        line = input()
        if line == "/End/":
            break
        else:
            note = note + '\n' + line
    return note


def welcome():
    """ Welcome Screen Lines"""
    print("Press 1 To Write Entry")
    print("Press 2 To View Entry")
    print("Press 3 To Exit")
    return input()


def write_file(dat, note):
    try:
        with open("Entry.txt", "a+") as _fil:
            _fil.write('[' + str(dat) + ']' + '\n' + note + '\n')
    except:  # except part not working properly
        print("NO Entries found")


def read_file():
    with open("Entry.txt", "r") as _fil:
        line = _fil.read()
        print(line)

def new_user(usrname):
    with open("user.csv","a+") as file:
        name = csv.writer(file,delimiter = "|")
        ''' rest of the code'''


def main():
    option = welcome()
    if option == '1':
        note = write_note()
        dat = datetime.now()  # date and time needs to be formatted
        write_file(dat, note)
        main()
    elif option == '2':
        read_file()
        main()
    elif option == '3':
        sys.exit(0)


if __name__ == "__main__":
    main()
