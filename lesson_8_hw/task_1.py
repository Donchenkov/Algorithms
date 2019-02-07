

s = 'papa'
res = []
for ln in range(1, len(s)):

    idx_end = ln

    for i in range(0, len(s)):
        if len(s[i:idx_end]) == ln:
            find = hash(s[i:idx_end])
            res.append(find)

        idx_end += 1

print(len(set(res)))
