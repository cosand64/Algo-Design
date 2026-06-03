def reverse_string_loop(sentence):
    for index in range(len(sentence)-1, -1, -1):
        print(sentence[index], end='')

def recursive_reverse_string(sentence):
    if len(sentence) <= 0:
        return 
    else:
        recursive_reverse_string(sentence[1:])
        print(sentence[0], end='')


def main():
    sentence = 'the quick brown fox jumps over the lazy dog.'

    reverse_string_loop(sentence)
    print()
    recursive_reverse_string(sentence)

main()