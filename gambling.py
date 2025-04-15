import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], '|', end=' ')
            else:
                print(column[row], end='')
        print()

def deposit():
    while True:
        try:
            amount = int(input('Enter the amount you want to deposit [minimum amount is $50]: '))
            if amount >= 50:
                print('Your amount is deposited.')
                return amount
            else:
                print('Please enter a minimum amount of $50.')    
        except ValueError:
            print('Please enter a valid number.')

def number_of_lines():
    while True:
        try:
            lines = int(input(f'Enter the number of lines you want to bet on (1-{MAX_LINES}): '))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f'Please enter a number between 1 and {MAX_LINES}.')    
        except ValueError:
            print('Please enter a valid number.')

def get_bet():
    while True:
        try:
            amount = int(input('How much would you like to bet on each line? $'))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f'Please enter a bet between ${MIN_BET} and ${MAX_BET}.')    
        except ValueError:
            print('Please enter a valid number.')

def spin(balance):
    lines = number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You don’t have enough balance. Your current balance is: ${balance}.')
        else:
            break

    print(f'Your bet: ${bet} per line on {lines} lines. Total bet: ${total_bet}')
    print(f'Balance: ${balance}, Lines: {lines}')

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)

    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)

    print(f'You won ${winnings}')
    if winning_lines:
        print(f'You won on lines: {winning_lines}')
    else:
        print('No winning lines this time.')

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance: ${balance}')
        ans = input('Press Enter to play or "q" to quit: ')
        if ans.lower() == 'q':
            break
        balance += spin(balance)
        print(f'You have ${balance} remaining.')

main()
