class Computer:
    def __init__(self, idefNum, isInf, conList):
        self.idefNum = idefNum 
        self.isInf = isInf 
        self.conList = conList
    
    def setInfStat(status):
        self.isInf = status
    
    def getInfStat():
        return self.isInf
        

f = open("input.txt", "r")
lines = f.readlines()

compList = []
numComputer = lines[0]
numEdges = lines[1]
edgelist = []
tempConctList = []

#loop for filling out list of connections
for x in range(2, numEdges+1):
    tempConctList.append(lines[x])

# loop for creating computer objects
for i in range(numComputer):
    tempC = Computer()


for i in range(2, numEdges):
    edge = lines[i]
    edgelist.append(lines[i])
    print(edgelist)

infComp = input("Please enter whcih computer is infected: ")

# find if computer is "connected" i.e. edge has same
# for x in range(len(edgelist)): # traverse main list
 #   for y in range(x):
        

   #  for y in range(): # this loop looks at the specific lists within our list of lists
