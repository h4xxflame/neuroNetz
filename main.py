#!/usr/bin/python3
import math

def generateData(trainData, testData):
    for i in range(0, 7001, 1):
        trainData.append(math.sin(i/1000))
    for i in range(0, 7001, 1000):
        testData.append(trainData[i])
        print(trainData[i])
        trainData.pop(i)


if __name__ == "__main__":

    trainData = []
    testData = []

    generateData(trainData, testData)
    print("test")
    print(testData)