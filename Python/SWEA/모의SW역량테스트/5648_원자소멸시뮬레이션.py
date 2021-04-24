import sys
sys.stdin = open("input.txt","r")

T = int(input())
maps = [[0 for _ in range(4001)] for _ in range(4001)]
dx,dy = [1,-1,0,0], [0,0,-1,1]
for t in range(1, T+1):
    atom_nums = int(input())
    atoms = []
    e_sum = 0

    for i in range(atom_nums):
        x,y,d,energy = map(int,input().split())
        x = (x+1000)*2
        y = (y+1000)*2
        atoms.append([y,x,d,energy])
        maps[y][x] += 1

    while atoms:
        out_of_maps = []
        collision_of_maps = set()

        for i in range(len(atoms)):
            y,x,d,energy = atoms[i]
            _dy = y + dx[d]
            _dx = x + dy[d]
            if _dx < 0 or _dx > 4000 or _dy < 0 or _dy > 4000:
                out_of_maps.append(i)
                continue
            maps[y][x] -= 1
            maps[_dy][_dx] += 1
            atoms[i][0],atoms[i][1] = _dy,_dx 

        while out_of_maps:
            i = out_of_maps.pop()
            y,x,d,energy = atoms[i]
            maps[y][x] -= 1
            atoms.pop(i)

        for y,x,d,energy in atoms:
            if maps[y][x] > 1:
                collision_of_maps.add((y,x))

        for y,x in collision_of_maps:
            for i in range(len(atoms)-1,-1,-1):
                _y,_x,d,e = atoms[i]
                if x==_x and y==_y:
                    maps[_y][_x] -= 1
                    e_sum += e
                    atoms.pop(i)
                    
    print("#{} {}".format(t,e_sum))

