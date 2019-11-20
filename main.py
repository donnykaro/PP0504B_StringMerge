def string_merge(s1, s2):
    counter = len(s2)
    if len(s2) > len(s1):
        counter = len(s1)
    merged_string = ''
    for i in range(0, counter):
        merged_string += s1[i] + s2[i]
    return merged_string


merged_strings = []
for i in range(0, int(input())):
    user_input = input().split()
    merged_strings.append(string_merge(user_input[0], user_input[1]))

for s in merged_strings:
    print(s)
