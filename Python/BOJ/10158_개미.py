import sys
sys.stdin = open("input.txt","r")
w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())
x+=t;y+=t
x%=(2*w);y%=(2*h)
x = 2*w-x if x > w else x
y = 2*h-y if y > h else y
print(x,y)
#
# w,h = map(int,input().split())
# x,y = map(int,input().split())
# n = int(input())
#
#
# moves = []
# r,c = h-y,x
# d_r,d_c = -1,1
#
# while True:
#     if 0<= r + d_r<=h and 0<= c + d_c <=w:
#         moves.append([r, c])
#         r+=d_r
#         c+=d_c
#
#     else:
#         if r == 0:
#             if c==0 or c==w:
#                 d_r*=-1
#                 d_c*=-1
#             else:
#                 d_r*=-1
#         elif r==h:
#             if c==0 or c==w:
#                 d_r*=-1
#                 d_c*=-1
#             else:
#                 d_r*=-1
#         else:
#             if c==0 or c==w:
#                 d_c*=-1
#
#     if len(moves)>3:
#         if moves[0] == moves[-2] and moves[1] == moves[-1]:
#             break
#
# n%=(len(moves[0:len(moves)//2])-2)
# x,y =  moves[n][1], h-moves[n][0]
# print(x,y)