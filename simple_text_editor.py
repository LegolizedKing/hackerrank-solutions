s=""
h=[]
n=int(input())
for i in range(n):
  u = input()
  if ' ' in u:
    u, t = u.split(' ')
  if u=='1':
    h.append(t)
    s+=t
  elif u=='2':
    h.append(s)
    t=int(t)
    s=s[:len(s)-t]
  elif u=='3':
    t=int(t)
    print(s[t-1])
  else:
    s=h.pop()

