""" Helper functions """
def num_to_s(n, money = False, per = False):
    if money:
        return '${:,.2f}'.format(n)
    elif per:
        return '{:.2f}%'.format(n)
    else:
        return '{:,}'.format(n)

def pretty_num_to_s(n, money = False, percentage = False):
    """ Convert num to colored, signed string """
    to_string = ""
    if n > 0:
        to_string += '\033[92m+{0}'.format(num_to_s(n, money, percentage))
    elif n < 0:
        to_string += '\033[91m{0}'.format(num_to_s(n, money, percentage))
    else:
        to_string += str(num_to_s(n, money, percentage))
    return to_string + '\033[0m'
