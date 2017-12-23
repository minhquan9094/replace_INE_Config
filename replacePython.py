from sys import argv
pathSeft, pathFile= argv

print (pathFile)

def updateSW1(pathFile):

    file = open(pathFile+"\sw1.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/10","Ethernet1/1")
    dataTemp = dataTemp.replace("FastEthernet0/11","Ethernet1/2")
    dataTemp = dataTemp.replace("FastEthernet0/12","Ethernet1/3")

    dataTemp = dataTemp.replace("FastEthernet0/13","Ethernet0/2")
    dataTemp = dataTemp.replace("FastEthernet0/14","Ethernet0/3")
    dataTemp = dataTemp.replace("FastEthernet0/15","Ethernet1/0")

    dataTemp = dataTemp.replace("FastEthernet0/2","Ethernet0/1")
    dataTemp = dataTemp.replace("FastEthernet0/1","Ethernet0/0")

    file.close()

    file = open(pathFile+ "\sw1_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)



def updateSW2(pathFile):

    file = open(pathFile+"\sw2.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/10","Ethernet0/2")
    dataTemp = dataTemp.replace("FastEthernet0/11","Ethernet0/3")
    dataTemp = dataTemp.replace("FastEthernet0/12","Ethernet1/0")

    dataTemp = dataTemp.replace("FastEthernet0/16","Ethernet1/3")
    dataTemp = dataTemp.replace("FastEthernet0/17","Ethernet1/2")
    dataTemp = dataTemp.replace("FastEthernet0/18","Ethernet1/1")

    dataTemp = dataTemp.replace("FastEthernet0/2","Ethernet0/0")
    dataTemp = dataTemp.replace("FastEthernet0/1","Ethernet0/1")

    dataTemp = dataTemp.replace("FastEthernet0/4","Ethernet2/1")
    dataTemp = dataTemp.replace("FastEthernet0/3","Ethernet2/0:")

    file.close()

    file = open(pathFile+ "\sw2_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)


def updateSW3(pathFile):

    file = open(pathFile+"\sw3.txt","r")
    print (pathFile+"\sw3.txt")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/13","Ethernet0/0")
    dataTemp = dataTemp.replace("FastEthernet0/14","Ethernet0/1")
    dataTemp = dataTemp.replace("FastEthernet0/15","Ethernet0/2")

    dataTemp = dataTemp.replace("FastEthernet0/16","Ethernet1/1")
    dataTemp = dataTemp.replace("FastEthernet0/17","Ethernet1/0")
    dataTemp = dataTemp.replace("FastEthernet0/18","Ethernet0/3")

    dataTemp = dataTemp.replace("FastEthernet0/4","Ethernet1/3")
    dataTemp = dataTemp.replace("FastEthernet0/3","Ethernet1/2:")

    file.close()

    file = open(pathFile+ "\sw3_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)


def updateR1(pathFile):

    file = open(pathFile+"\\r1.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/0","Ethernet0/1")
    dataTemp = dataTemp.replace("FastEthernet 0/1","Ethernet0/0:")

    file.close()

    file = open(pathFile+ "\\r1_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)

def updateR2(pathFile):

    file = open(pathFile+"\\r2.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/0","Ethernet0/1")
    dataTemp = dataTemp.replace("FastEthernet 0/1","Ethernet0/0:")

    file.close()

    file = open(pathFile+ "\\r2_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)

def updateR3(pathFile):

    file = open(pathFile+"\\r3.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/0","Ethernet0/0")
    dataTemp = dataTemp.replace("FastEthernet 0/1","Ethernet0/1:")

    file.close()

    file = open(pathFile+ "\\r3_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)

def updateR4(pathFile):

    file = open(pathFile+"\\r4.txt","r")
    data=file.read()
    #print (data)

    #dataTemp = data.replace("FastEthernet","Ethernet")
    dataTemp=data
    dataTemp = dataTemp.replace("FastEthernet0/0","Ethernet0/1")
    dataTemp = dataTemp.replace("FastEthernet 0/1","Ethernet0/0")

    file.close()

    file = open(pathFile+ "\\r4_update.txt","w")
    print (dataTemp)
    file.write(dataTemp)

updateSW1(pathFile)
updateSW2(pathFile)
updateSW3(pathFile)

updateR1(pathFile)
updateR2(pathFile)
updateR3(pathFile)
updateR4(pathFile)