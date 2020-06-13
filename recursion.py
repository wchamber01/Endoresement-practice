# Print each item from the list on a seperate line using recursion

word_list = ['Bob', 'Slack', ['reddit', '89', 101, [
    'alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


def recursion(words):
    for word in words:
        if isinstance(word, list):
            recursion(word)
        else:
            print(word)


recursion(word_list)
