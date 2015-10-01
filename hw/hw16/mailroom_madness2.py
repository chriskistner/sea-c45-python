logbook = {
    'Bill Gates': [500, 1000, 1500],
    'George Washington': [700, 750, 7000],
    'Abraham Lincoln': [500, 50]
}


main_menu = '''
Welcome to to the mailroom
Choose a command:
T - Create a Thank You Message
R - Generate a Report
quit - Quit Program
'''
message_prompt = '''
Enter a name, or choose from the following:
list - Print a list of previous donors
quit - Return to main menu.
'''
message_prompt2 = '''
Enter donation amount or 'quit':
'''
t_letter = '''
Dear {name},
Thank you so much for your generous donation of {amount}. Your funds will go
to maintaining the our habitat for toothless ant eaters in Scandinavia. Grinner
, our 50 year old ant eater is smailing at you.
Thanks again,
Chris Kistner
Director, PTA.
'''
enter_cont = '\n\nPress enter to continue.'

cells = [20, 8, 3, 8]


def repl(prompt, validator=None):
    while True:
        user_input = input(prompt)
        user_input = user_input.lower()
        if user_input in ('q', 'quit'):
            print('Quiting Mailroom')
            return
        if validator:
            result = validator(user_input)
            if result:
                if 'Invalid' in str(result):
                    print(result)
                else:
                    return result
        else:
            return


def main_menu():
    user_input = input('Welcome to to the mailroom Choose a command: \
    T - Create a Thank You Message \
    R - Generate a Report \
    quit - Quit Program')
    if user_input in ('t'):
        repl(message_prompt, t_menu)
    elif user_input in ('r'):
        report()
    else:
        return 'Invalid Command.'


def list_donor_names():
    '''
    Returns a list of all donor names in the logbook, one per line.
    # Runs through all donors in the logbook  and exports a text file with
    Thank You Messages for the sum of their donations.
    '''
    for name, amount in logbook.items():
        letter_log = open('ty_logbook.txt', 'a')
        letter = t_letter.format(name=name, amount=sum(amount))
        letter_log.write(letter + '\n')
        letter_log.flush()
        letter_log.close()
    return '\n'.join(logbook.keys())


def t_menu(user_input):
    '''
    Validator for "Send a Thank You Letter" menu
    redirects through to name and amount validators.
    Eventually returns a formatted letter or an invalid message.
    '''
    if user_input == 'list':
        print (list_donor_names())
        return repl(enter_cont)
    else:
        name = user_input
        if valid_name(name):
            amount = repl(message_prompt2, valid_amount)
            if amount:
                add_to_data(name, amount)
                letter = t_letter.format(name=name, amount=format_amount(amount
                ))
                print(letter)
                #Prompts the User for a filename and exports the message there.
                filename = input("Enter file  name to export message too.")
                out = open(filename, "w")
                out.write(letter)
                out.write('\n')
                out.close()
                return repl(enter_cont)
        else:
            return 'Invalid Name'


def valid_name(name):
    # Checks for valid name with at least two characters
    names = name.split(' ')
    if len(names) < 2:
        return False
    return True


def valid_amount(user_input):
    '''
    Validator for donation amount.
    Returns the float of the given number, or an invalid message
    '''
    try:
        return round(float(user_input), 2)
    except ValueError:
        return 'Invalid Amount'


def format_amount(amount):
    '''
    Returns a neatly formatted dollar amount string from a given int
    or float.
    '''
    return '$%.2f' % amount


def report():
    # Gathers the current logbook and formats it into neat rows, then prints.
    global logbook

    donor_list = logbook.keys()
    # donor_list.sort()
    row_list = get_report_header()

    for d in donor_list:
        donations = logbook[d]
        total = sum(donations)
        num = len(donations)
        avg = total / num
        row = [d, format_amount(total), str(num), format_amount(avg)]
        row_list.append(get_report_cells(row))

    print('\n'.join(row_list))
    return repl(enter_cont)


def get_report_header():
    # Returns neatly formatted column headers for the data report.
    header = ['\n']
    header.append(get_report_cells(['Name', 'Total', '#', 'Average']))
    header.append('-' * (sum(cells) + (3 * len(cells))))
    return header


def get_report_cells(row):
    '''
    Formats each row of donor data into  spaced cells.
    returns a single string formatted row
    '''
    formatted_row = []
    for i, c in enumerate(row):
        spaces = ' ' * (cells[i] - len(c))
        formatted_row.append('{}{}'.format(spaces, c))
    return ' | '.join(formatted_row)


def add_to_data(name, amount):
    # Adds a given name and amount to the logbook. Returns None.
    global logbook
    if name not in logbook.keys():
        logbook[name] = []
    logbook[name].append(amount)

if __name__ == '__main__':
    main_menu()
