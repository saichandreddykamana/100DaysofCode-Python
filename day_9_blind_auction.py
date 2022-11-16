from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bids = {}


def add_bids(name, bid, bids):
    bids[name] = bid


def print_bids(bids):
    if len(bids) > 0:
        for bid in bids:
            print(f'Name : {bid} Bid : {bids[bid]} \n')
    else:
        print('Currently, there are no bids to show')


def show_highest_bid(bids):
    highest = 0
    bidder = ''
    for bid in bids:
        if bids[bid] > highest:
            highest = bids[bid]
            bidder = bid
    return {bidder: highest}


while True:
    clear()
    check_new_bid = input(
        " Do you want add new bid to bids dictionary. Type 'yes' or 'no' : \n"
    ).lower()
    if check_new_bid == 'yes' or check_new_bid == 'y':
        name = input('Name of the bidder : \n').capitalize()
        bid_value = int(input('Bid Value : \n'))
        add_bids(name, bid_value, bids)
    else:
        winner = show_highest_bid(bids)
        for win in winner:
            print(
                f'The highest bid of all current bids is \n Name: {win} \n Bid: {winner[win]}'
            )
        break
