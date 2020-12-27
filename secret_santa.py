# Program to random pick a secret santa
# get names from a list
# draw names
# a person cannot pick herself
# we need to make sure everybody was picked
# make it in one cycle

import random


def random_picker(list_of_names):
    """Shuffles the given list.
    Creates a dictionary where each element in the given list is a key and
    its value is the next item on the list. The assignment is done in a 
    circle, where the last element's value is the first element in the list.
    Returns a dictionary"""
    pairs = {}
    random.shuffle(list_of_names)
    for i in range(len(list_of_names)):
        pairs[list_of_names[i]] = list_of_names[(i + 1) % len(list_of_names)]

    return pairs


def print_all_pairs(pairs):
    """Takes a dictionary and print all key-value pairs"""
    for key, value in pairs.items():
        print("{}, you will get a gift for {}".format(key, value))


def print_my_secret_santa_recipient(name, pairs):
    """Get a name and a dictionary.
    print the person's name assigned to the input name.
    name is a string
    pairs is a dictionary"""
    try:
        print("{}, you will get a gift for {}".format(name, pairs[name]))
    except KeyError:
        print("{}, your name is not on this list.".format(name))


# List of participants
park = ["Mordecai", "Rigby", "Pops", "Mitch", "Skips", "Benson", "Hi Five Ghost", "Margaret", "Eileen"]



new_draw = random_picker(park)
print()
print("Printing all pairs:")
print()
print_all_pairs(new_draw)
print("---")
print()
print("Printing only the person assigned to Skips:")
print()
print_my_secret_santa_recipient("Skips", new_draw)
print("---")
print()
print("Trying to print someone that is not in the list:")
print()
print_my_secret_santa_recipient("Mr. Maellard", new_draw)
print("---")
