# homework 1 python

class Computer:
    def __init__(self, ident):
        self.ident = ident
        self.isInf = False
        self.conList = []   # list of connected computers

    def setInfStat(self, status):
        self.isInf = status

    def getInfStat(self):
        return self.isInf

    def addConnection(self, other_id):
        self.conList.append(other_id)

    def getConnections(self):
        return self.conList

# open the file for reading
f = open("input.txt", "r")
lines = f.readlines()
f.close()

num_computers = int(lines[0])
num_edges = int(lines[1])

# list of computer objects creation loop
computers = [None]
i = 1
while i <= num_computers:
    computers.append(Computer(i))
    i = i + 1

# edges
edge_index = 2
end_edge_index = 2 + num_edges # to end at the right index for edges in input.txt
while edge_index < end_edge_index:
    parts = lines[edge_index].split()
    a = int(parts[0]) # comment this better if you have time.
    b = int(parts[1])
    computers[a].addConnection(b)
    computers[b].addConnection(a)
    edge_index = edge_index + 1

# starting infected
start = int(lines[end_edge_index])
computers[start].setInfStat(True)

# checking the lists and updating infection statuses
infected = [start]   # keeping track of infected
idx = 0
while idx < len(infected):
    current_id = infected[idx]
    neighbors = computers[current_id].getConnections()

    j = 0
    while j < len(neighbors):
        nb = neighbors[j]

        # check if nb already infected
        k = 0
        seen = False
        while k < len(infected):
            if infected[k] == nb:
                seen = True
            k = k + 1

        if (not seen) and (not computers[nb].getInfStat()):
            computers[nb].setInfStat(True)
            infected.append(nb)
        j = j + 1

    idx = idx + 1

# exclude the original infected computer
answer = len(infected) - 1

print(answer)
outf = open("output.txt", "w")
outf.write(str(answer))
outf.close()
