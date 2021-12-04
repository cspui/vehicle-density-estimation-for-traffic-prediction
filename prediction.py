import sys
CONGESTION_RANGES = [15, 30]
VEHICLE_CONGESTION_VALUE = [1, 2, 0.5]

def readInput(txtFileName):
    # Open and read txt file
    txtFile = open(txtFileName, 'r')
    txt = txtFile.read()
    txt = [line for line in txt.splitlines() if line.strip() != ""]
    # Close file
    txtFile.close()

    return txt


def getOutput(txtFileName):
    # Read text from files
    txt = readInput(txtFileName) 

    classes = ['car:', 'truck:', 'motorbike:']
    classesCount = [0, 0, 0]
    totalFrames = 0

    for line in txt:
        word = line.split()[0]
        if word in classes:
            classesCount[classes.index(word)]+=1
        elif word == 'cvWriteFrame':
            totalFrames+=1

    
    # Process output
    # If video input: Get average number of vehicles per frame
    if totalFrames > 0:
        classesCount = [vehicle//totalFrames for vehicle in classesCount]

    # Sum up congestion value of vehicles detected
    congestionVal = 0
    for i in range(len(classesCount)):
        congestionVal += (classesCount[i]) * VEHICLE_CONGESTION_VALUE[i]

    if (congestionVal < CONGESTION_RANGES[0]):
        congestionOutput = "Low Congestion"
    elif (congestionVal < CONGESTION_RANGES[1]):
        congestionOutput = "Medium Congestion"
    else:
        congestionOutput = "High Congestion"

    output = f'Car: {classesCount[0]}, Truck: {classesCount[1]}, Motorbike: {classesCount[2]}\nCongestion Value: {congestionVal}\n{congestionOutput}'


    # Return output
    return output


if __name__ == '__main__':
    print(getOutput('result.txt'))
    print(getOutput('result (1).txt'))
    pass