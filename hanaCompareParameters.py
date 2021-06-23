file1 = open("C:\\Users\\jesushgonzalez\\Desktop\\Diff\\FPR (QA) global.ini", "r")

# read the lines
linesF1 = file1.readlines()
parameterValues = {}

for line in linesF1:
    # remove lines that are not parameters
    if line[0] == "#" or line[0] == "[":
        continue

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
    else:
        print("Duplicate parameter {0}".format(keyTmp))

for value in parameterValues:
    print("Parameter: {0} = {1}".format(value, parameterValues[value]))
