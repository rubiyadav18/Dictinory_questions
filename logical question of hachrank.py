def fun(words):
    a = {}
    for word in words:
        s = "".join(sorted(word))
        if s in a:
            a[s].append(word)
        else:
            a[s] = [word]
    return list(a.values())
words=["eat","tea","tan","ate","nat","bat"]
print(fun(words))