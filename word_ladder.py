#!/bin/python3


from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.append(start_word)

    q = deque()
    q.append(stack)

    dictfile = open(dictionary_file)
    dictlist = [word.strip() for word in dictfile.readlines()]

    if start_word == end_word:
        return [start_word]
    while len(q) > 0:
        stackn = q.popleft()
        for word in set(dictlist):
            if _adjacent(word, stackn[-1]):
                if word == end_word:
                    stackn.append(word)
                    return stackn
                stackcopy = copy.deepcopy(stackn)
                stackcopy.append(word)
                q.append(stackcopy)
                dictlist.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if not ladder:
        return False
    for i in range(0, len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]):
            continue
        else:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    if (len(word1) != len(word2)) or (word1 == word2):
        return False
    else:
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                count += 1
            else:
                continue
        if count != 1:
            return False
        else:
            return True
