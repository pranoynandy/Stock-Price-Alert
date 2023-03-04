# Storing names of stocks in stocks.txt

us_stocks = []
ind_stocks = []

def input_data(message_received):

    # Read us_stocks and ind_stocks lists
    with open('stocks.txt', 'r') as stk:
        current_list = None
        for line in stk:
            if line.startswith('US:'):
                current_list = us_stocks
            elif line.startswith('INDIA:'):
                current_list = ind_stocks
            else:
                current_list.append(line.strip())

    # Display the lists
    if message_received == 'stocks':
        print(us_stocks)
        print(ind_stocks)
    else:
        # Adding stocks
        if message_received[0].lower() == 'add':
            if message_received[1][-3] == '.':
                ind_stocks.append(message_received[1].upper())
            else:
                us_stocks.append(message_received[1].upper())
        # Removing stocks
        elif message_received[0].lower() == 'remove':
            if message_received[1][-3] == '.':
                ind_stocks.remove(message_received[1].upper())
            else:
                us_stocks.remove(message_received[1].upper())

        with open('stocks.txt', 'w') as stk:
            # Updating us_stocks list
            stk.write('US:\n')
            for stock in us_stocks:
                stk.write(str(stock) + '\n')
            # Updating ind_stocks list
            stk.write('INDIA:\n')
            for stock in ind_stocks:
                stk.write(str(stock) + '\n')

    return 0
