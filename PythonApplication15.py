S="Hello. My friend, my pet."
s=S.lower()
b=s.split()
a=set()
for word in b:
    alphaWord=""
    for i in word:
        if(i.isalpha()):
            alphaWord+=i;
    if(alphaWord != ""):
        a.add(alphaWord)
print("사용된 단어의 개수는 ", len(a), "개이다.")
print(a)