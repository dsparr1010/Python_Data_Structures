import re

string1 = '  g Od'
string2 = 'd  o g '

ex1 = ' wlaly '
ex2 = 'moo  se'

ex3 = ' clint eastwood '
ex4 = 'old  wesT  action '

def my_anagram(str1, str2):
    """Check if two strings contain same letters"""
    #remove whitespace
    str1, str2 = re.sub('[\s+]', '', str1).lower(), re.sub('[\s+]', '', str2).lower()

    str1_arr = list(str1)
    str2_arr = list(str2)

    count = 0
    for x in str1_arr:
        if x in str2_arr:
            count += 1
    if count == len(str1_arr):
        print(True)
    if count != len(str1_arr):
        print(False)

# anagram(string1, string2)
# anagram(ex1, ex2)

def sorted_anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    print(sorted(s1) == sorted(s2))

# sorted_anagram(string1, string2)
# sorted_anagram(ex1, ex2)
# sorted_anagram(ex3, ex4)

def manual_anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #edge case check
    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    #essentially do the opposite and subtract any instance of letter found in s2 from count
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

print(manual_anagram(string1, string2))
print(manual_anagram(ex1, ex2))
print(manual_anagram(ex3, ex4))