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


count_calls()
# b = 'Capibara'
# a = string_info('Capibara')
print(string_info('Capibara'))
print(calls)
