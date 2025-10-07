# Homework 3

# file input
f = open("input.txt", "r")
lines = f.readlines()
f.close()

first = lines[0].split()
N = int(first[0])     # world size 
K = int(first[1])     # num civs

# birthplaces
birthplaces = []
i = 0
pos = 1
while i < K:
    parts = lines[pos].split()
    x = int(parts[0])
    y = int(parts[1])
    birthplaces.append([x, y])
    pos = pos + 1
    i = i + 1

# square grid
# -1 means empty, otherwise store civ number
world = []
r = 0
while r < N:
    row = []
    c = 0
    while c < N:
        row.append(-1)
        c = c + 1
    world.append(row)
    r = r + 1

# put initial civilizations on their squares
i = 0
while i < K:
    x = birthplaces[i][0]
    y = birthplaces[i][1]
    world[x][y] = i
    i = i + 1

# searching for groups
parent = []
i = 0
while i < K:
    parent.append(i)
    i = i + 1

def getRoot(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def join(a, b):
    ra = getRoot(a)
    rb = getRoot(b)
    if ra != rb:
        parent[rb] = ra
        return 1
    return 0

groupsLeft = K

# neighbors of a square
def neighborSquares(x, y, N):
    out = []
    if x > 0:       out.append([x - 1, y])
    if x + 1 < N:   out.append([x + 1, y])
    if y > 0:       out.append([x, y - 1])
    if y + 1 < N:   out.append([x, y + 1])
    return out

# connect them if birthplaces already touch
i = 0
while i < K:
    x = birthplaces[i][0]
    y = birthplaces[i][1]
    nb = neighborSquares(x, y, N)
    j = 0
    while j < len(nb):
        nx = nb[j][0]
        ny = nb[j][1]
        if world[nx][ny] != -1:
            groupsLeft = groupsLeft - join(world[x][y], world[nx][ny])
        j = j + 1
    i = i + 1

if groupsLeft == 1:
    years = 0
else:
    years = 0

    # list of taken squares for each civ
    takenSquares = []
    i = 0
    while i < K:
        takenSquares.append([])
        i = i + 1

    # starting at the birthplace
    i = 0
    while i < K:
        takenSquares[i].append([birthplaces[i][0], birthplaces[i][1]])
        i = i + 1

    # spreading
    done = False
    while not done:
        years = years + 1

        # making a list of lists for the squares each civ conquers (THIS YEAR)
        newSquares = []
        i = 0
        while i < K:
            newSquares.append([])
            i = i + 1

        # each civ takes adjacent empty squares
        civ = 0
        while civ < K:
            t = 0
            while t < len(takenSquares[civ]):
                x = takenSquares[civ][t][0]
                y = takenSquares[civ][t][1]
                nb = neighborSquares(x, y, N)
                u = 0
                while u < len(nb):
                    nx = nb[u][0]
                    ny = nb[u][1]
                    if world[nx][ny] == -1:
                        world[nx][ny] = civ
                        newSquares[civ].append([nx, ny])
                    u = u + 1
                t = t + 1
            civ = civ + 1

        # connect groups where different civ squares now touch
        r = 0
        while r < N:
            c = 0
            while c < N:
                if world[r][c] != -1:
                    nb = neighborSquares(r, c, N)
                    u = 0
                    while u < len(nb):
                        nx = nb[u][0]
                        ny = nb[u][1]
                        if world[nx][ny] != -1 and world[nx][ny] != world[r][c]:
                            groupsLeft = groupsLeft - join(world[r][c], world[nx][ny])
                        u = u + 1
                c = c + 1
            r = r + 1

        if groupsLeft == 1:
            done = True
        else:
            takenSquares = newSquares

print(years)
outF = open("output.txt", "w")
outF.write(str(years))
outF.close()
