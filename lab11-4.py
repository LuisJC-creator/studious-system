tstCases = int(input("Please enter the number of circles: "))

def getVals():
    orgList = []
    for i in range(tstCases):
        usrVals = []
        x, y, rad = input("Please enter x, y, and radius: ").split()
        usrVals.append(x)
        usrVals.append(y)
        usrVals.append(rad)
        orgList.extend(usrVals)
    return orgList

def getMinMax(itemList):
    xMinList = []
    yMinList = []
    xMaxList = []
    yMaxList = []
    for i in range(0, len(itemList), 3): # itemList[i] = x value, itemList[i+1] = y value, itemList[i+2] = radius
        xSubEle = float(itemList[i]) - float(itemList[i+2])
        xMinList.append(xSubEle)
        ySubEle = float(itemList[i+1]) - float(itemList[i+2])
        yMinList.append(ySubEle)
        xSubEle1 = float(itemList[i]) + float(itemList[i+2])
        xMaxList.append(xSubEle1)
        ySubEle1 = float(itemList[i+1]) + float(itemList[i+2])
        yMaxList.append(ySubEle1)
    
    minX = xMinList[0]
    minY = yMinList[0]
    maxX = xMaxList[0]
    maxY = yMaxList[0]
    for i in range(len(xMinList)):
        if xMinList[i] < minX:
            minX = xMinList[i]
    for i in range(len(yMinList)):
        if yMinList[i] < minY:
            minY = yMinList[i]
    for i in range(len(xMaxList)):
        if xMaxList[i] > maxX:
            maxX = xMaxList[i]
    for i in range(len(yMaxList)):
        if yMaxList[i] > maxY:
            maxY = yMaxList[i]
    return minX, minY, maxX, maxY

def getArea(bounds): # previously I had getArea(minX, minY, maxX. maxY) but that didn't work so I tried with tuple
    minX, minY, maxX, maxY = bounds
    area = (maxX - minX) * (maxY - minY)
    return area
    

print(f"The area is:  {getArea(getMinMax(getVals()))}")