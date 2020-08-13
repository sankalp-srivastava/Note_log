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
    return input()


def write_file(dat, note):
    with open("Entry.txt", "a+") as _fil:
        _fil.write('['+ str(dat) + ']' + '\n' + note + '\n')


def main():
    option = welcome()
    if option == '1':
        note = write_note()
        dat = datetime.now()
        write_file(dat,note)
        sys.exit(0)


def read_file():
    with open("Entry.txt","r") as _fil:
        line = _fil.read()
        print(line)

if __name__ == "__main__":
    main()
