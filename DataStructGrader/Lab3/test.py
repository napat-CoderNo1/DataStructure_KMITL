s = ['A','B','B','B']
for i in range(0, len(s), 1):
    if s[i] == 'B':
        s.remove(s[i])
print(s)