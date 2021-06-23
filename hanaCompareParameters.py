file1 = open("C:\\Users\\jesushgonzalez\\Desktop\\Diff\\FPR (QA) global.ini", "r")

linesF1 = file1.readlines()

parameterValues = {}
parameterSection = []
tmpList = []

for line in linesF1:
    # remove lines that are not parameters
    if line[0] == "#":
        continue

    #TODO: separate parameters by section
    if line[0] == "[":
        if tmpList:
            parameterSection.append(tmpList)
        else:
            print("Empty list!!!")

        tmpList = []
        tmpList.append(line)

    if "=" not in line:
        continue

    # separate the parameter name and the value based on the "=" sign
    partitionLine = line.partition("=")

    # remove spaces to the key and values
    keyTmp = partitionLine[0].replace(" ", "")
    valueTmp = partitionLine[2].replace(" ", "")

    # create dictionaries as {key:value} / {parameter:value}
    if keyTmp not in parameterValues:
        parameterValues[keyTmp] = valueTmp
        tmpList.append(parameterValues)
    else:
        print("Duplicate parameter {0}".format(keyTmp))

for dict1 in parameterSection:
    print(dict1)
