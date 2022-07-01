s,t = map(str,input().split())
for i in t:
            if s.count(i) != t.count(i):
                print(i)
                break