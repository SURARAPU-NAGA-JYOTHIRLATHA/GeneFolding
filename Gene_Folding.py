import sys
def goof(string):
    original_string = string
    length = len(string) // 2

    while length != -1:
        if string[:length][::-1] == string[length : length+length]:
            string = string[length:]
            length = -1
        else:
            length -= 1
    string = string[::-1]

    len1 = len(string) // 2
    while len1 != -1:
        if string[:len1][::-1] == string[len1 : len1+len1]:
            string = string[len1:]
            len1 = -1
        else:
            len1 -= 1
    string = string[::-1]

    if string == original_string:
        return len(string)
    return goof(string)

string = sys.argv[1]
print(goof(string))
