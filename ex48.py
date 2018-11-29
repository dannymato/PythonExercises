verbs = ['go', 'stop', 'kill', 'eat']
direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def __init__():
    print('Init')

def is_verb(string):
    for x in verbs:
        if string == x:
            return True

    return False

def is_direction(string):
    for x in direction:
        if string == x:
            return True

    return False

def is_noun(string):
    for x in nouns:
        if string == x:
            return True

    return False

def is_stop(string):
    for x in stop:
        if string == x:
            return True

    return False

def is_number(string):
    try:
        int(string)
    except ValueError:
        return None


def lexacon():
    string = raw_input("> ")
    
    words = string.split()

    sentence = []

    for i in words:

        if is_verb(i):
            sentence.append(('verb', i))

        elif is_direction(i):
            sentence.append(('direction', i))

        elif is_noun(i):
            sentence.append(('noun', i))

        elif is_stop(i):
            sentence.append(('stop', i))

        elif is_number(i) is not None:
            sentence.append(('number', i))

    return sentence
