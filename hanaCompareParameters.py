'''
    This functions returns a list with the follow structure:
        list =
        [
            [section name],
            [ {param_name:value}, {param_name:value}, ... ]
        ]
'''
def getParametersFromFile(fileName):
    file1 = open(fileName, "r")

    linesF1 = file1.readlines()

    parametersBySection = []
    tmpList = []
    parameterValues = {}

    for line in linesF1:
        if line[0] == "#":
            continue

        if line[0] == "[":
            if tmpList:
                tmpList.append(parameterValues)
                parametersBySection.append(tmpList)
            else:
                pass
                #print("Empty list!!!")

            tmpList = []
            parameterValues = {}

            tmpList.append(line) # add the new section to the new list

        if "=" not in line:
            continue

        partitionLine = line.partition("=")
        keyTmp = partitionLine[0].replace(" ", "")
        valueTmp = partitionLine[2].replace(" ", "")

        # create dictionaries as {key:value} / {parameter:value}
        if keyTmp not in parameterValues:
            parameterValues[keyTmp] = valueTmp
        else:
            pass
            #print("Duplicate parameter {0}".format(keyTmp))

    return parametersBySection


def compareParameters(list1, list2):
    for section in list1:
        for i, x in enumerate(section):
            if i == 0: # section name
                # check if this section exist on list2

                print(x)
            if i == 1: # list with the {parameters:values}
                for parameter in x:
                    print("{0} = {1}".format(parameter, x[parameter]))


def printParametersBySection(list):
    for section in list1:
        for i, x in enumerate(section):
            if i == 0: # section name
                print(x)
            if i == 1: # list with the {parameters:values}
                for parameter in x:
                    print("{0} = {1}".format(parameter, x[parameter]))


list1 = getParametersFromFile("C:\\Users\\jesushgonzalez\\Desktop\\Diff\\FPR (QA) global.ini")
list2 = getParametersFromFile("C:\\Users\\jesushgonzalez\\Desktop\\Diff\\FPR global.ini")

#printParametersBySection(list1)
#printParametersBySection(list2)

compareParameters(list1, list2)
