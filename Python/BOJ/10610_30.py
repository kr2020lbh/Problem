N = list(map(int,list(input())))
SUM = sum(N)
if SUM % 3==0 and 0 in N:
  for i in sorted(N,reverse=True):
    print(i,end='')

else:
  print(-1)
