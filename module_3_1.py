calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(sting: str):
    count_calls()
    sting = (len(sting), sting.upper(), sting.lower())
    return sting


def is_contains(sting: str, list_to_search: list):
    count_calls()
    sting = sting.lower()
    for i in list_to_search:
        i = i.lower()
        if i == sting:
            return True
    return False





print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)