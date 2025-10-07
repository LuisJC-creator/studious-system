# Homework 2

# file input
f = open("input.txt", "r")
lines = f.readlines()
f.close()

numStations = int(lines[0])   # number of stations
numLines = int(lines[1])      # number of bus lines

# store each bus line as [start, end]
busLines = []
i = 0
pos = 2
while i < numLines:
    parts = lines[pos].split()
    start = int(parts[0])
    end = int(parts[1])
    busLines.append([start, end])
    pos = pos + 1
    i = i + 1

# track coverage from one bus line
def trackLine(stationsCovered, numStations, start, end):
    if start <= end:
        k = start
        while k <= end:
            stationsCovered[k] = True
            k = k + 1
    else:
        k = start
        while k < numStations:
            stationsCovered[k] = True
            k = k + 1
        k = 0
        while k <= end:
            stationsCovered[k] = True
            k = k + 1

# check if all stations are covered
def checkAll(stationsCovered, numStations):
    i = 0
    while i < numStations:
        if stationsCovered[i] == False:
            return False
        i = i + 1
    return True

# make a copy of a list
def copyStations(oldList, numStations):
    newList = []
    i = 0
    while i < numStations:
        newList.append(oldList[i])
        i = i + 1
    return newList

answer = numLines

# try using 1 line
i = 0
while i < numLines:
    stations = [False] * numStations
    trackLine(stations, numStations, busLines[i][0], busLines[i][1])
    if checkAll(stations, numStations):
        answer = 1
    i = i + 1

# try using 2 lines if needed
if answer > 1:
    i = 0
    while i < numLines:
        j = i + 1
        while j < numLines:
            stations = [False] * numStations
            trackLine(stations, numStations, busLines[i][0], busLines[i][1])
            trackLine(stations, numStations, busLines[j][0], busLines[j][1])
            if checkAll(stations, numStations):
                answer = 2
            j = j + 1
        i = i + 1

# try using 3 lines if needed
if answer > 2:
    i = 0
    while i < numLines:
        j = i + 1
        while j < numLines:
            k = j + 1
            while k < numLines:
                stations = [False] * numStations
                trackLine(stations, numStations, busLines[i][0], busLines[i][1])
                trackLine(stations, numStations, busLines[j][0], busLines[j][1])
                trackLine(stations, numStations, busLines[k][0], busLines[k][1])
                if checkAll(stations, numStations):
                    answer = 3
                k = k + 1
            j = j + 1
        i = i + 1


print(answer)
outFile = open("output.txt", "w")
outFile.write(str(answer))
outFile.close()
