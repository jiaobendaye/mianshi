from collections import Counter
s1 ='abcdefa'
s2 = 'acad'

def helper(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)
    for key in count2.keys():
        v2 = count2[key]
        v1 = count1[key]
        if v2 > v1:
            return False
    return True

print(helper(s1, s2))