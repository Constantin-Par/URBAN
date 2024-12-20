calls = 0

def count_calls():

    global calls
    calls += 1

    return calls

def string_info(string ):

    count_calls()

    return (len(string ), string .upper(), string .lower())

def is_contains(string, list_to_search):

    count_calls()

    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()

    return string.lower() in list_to_search

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)