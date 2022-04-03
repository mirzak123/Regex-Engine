def question_mark(regex, string):
    if string[0] == regex[0]:
        return match(regex[2:], string[1:])
    return match(regex[2:], string)


def asterisk(regex, string):
    # print("'" + regex + "'" + " '" + string + "'")
    if len(regex) > 2 and len(regex[2:]) == len(string):
        return match(regex[2:], string)
    elif not string:
        return match(regex[2:], string)
    elif string[0] == regex[0] or regex[0] == '.':
        return asterisk(regex, string[1:])
    return match(regex[2:], string)


def plus_sign(regex, string):
    if regex[0] != string[0] and regex[0] != '.':
        return False
    return asterisk(regex, string)


def match(regex, string):
    # print("'" + regex + "'" + " '" + string + "'")
    if len(regex) == len(string) == 1:
        if regex == string or regex == '.':
            return True

    if not regex:
        return True
    elif not string:
        return False
    # elif len(regex) != len(string):
        # return False
    if regex[0] == '\\':
        if regex[1] == string[0]:
            return match(regex[2:], string[1:])
        else:
            return False
    if len(regex) > 1:
        if regex[1] == '?':
            return question_mark(regex, string)
        elif regex[1] == '*':
            return asterisk(regex, string)
        elif regex[1] == '+':
            return plus_sign(regex, string)

    if regex[0] != string[0] and regex[0] != '.':
        return False
    else:
        return match(regex[1:], string[1:])


def string_check(regex, string):
    for i in range(len(string) - len(regex) + (regex.count('?') + regex.count('*') + regex.count('+') + regex.count('\\')) * 2 + 1):
        if match(regex, string[i:i + len(regex)]):
            return True
    return False


def main():
    regex, string = input().split('|')
    if not regex:
        print(True)
    elif regex[0] == '^' and regex[-1] == '$':
        regex = regex.strip('$^')
        if len(regex) != len(string) and '?' not in regex and '*' not in regex and '+' not in regex:
            print(False)
        else:
            print(match(regex, string))
    elif regex[0] == '^':
        print(match(regex[1:], string[:len(regex) - 1]))
    elif regex[-1] == '$':
        print(match(regex[:-1], string[-len(regex) + regex.count('\\') + 1:]))
    else:
        print(string_check(regex, string))


if __name__ == '__main__':
    main()
