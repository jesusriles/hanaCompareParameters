# arguments
verbose2 = False

verbose3 = False # function: getParametersFromFile
if verbose3:
    v3Sections = []
    v3Parameters = []
    v3Removed = []

# global
sectionNotInList = []
'''
    This functions returns a list with the follow structure:
        list =
        [
            [section name],
            [ {param_name:value}, {param_name:value}, ... ]
        ]
'''
def getParametersFromFile(fileName):
    if verbose2:
        print("\nFunction: getParametersFromFile")

    file1 = open(fileName, "r")

    linesF1 = file1.readlines()

    parametersBySection = []
    tmpList = []
    parameterValues = {}

    for line in linesF1:

        if verbose3:
            print("+ Checking line ", line)

        if line[0] == "[":
            if tmpList:
                tmpList.append(parameterValues)
                parametersBySection.append(tmpList)

                if verbose3:
                    print("-- Line added as section")
            else:
                if verbose3:
                    print("-- Line skipped because tmpList is blank")

            tmpList = []
            parameterValues = {}
            tmpList.append(line) # add the new section to the new list
            continue

        if line[0] == "#":
            if verbose3:
                print("-- Line removed, start with #")
            continue

        if "=" not in line:
            if verbose3:
                print("-- Line skipped, doesn't have a = sign")
            continue

        partitionLine = line.partition("=")
        keyTmp = partitionLine[0].replace(" ", "")
        valueTmp = partitionLine[2].replace(" ", "")

        # create dictionaries as {key:value} / {parameter:value}
        if keyTmp not in parameterValues:
            if verbose3:
                print("-- Line added as parameter")
            parameterValues[keyTmp] = valueTmp
        else:
            pass
            #print("Duplicate parameter {0}".format(keyTmp))
    if verbose2:
        print("Returning: ", parametersBySection)
    return parametersBySection


def sectionInList(sectionName, sectionList):
    if verbose2:
        print("\nFunction: sectionInList")
        print("Searching section: {0} in list:{1}".format(sectionName, sectionList))

    for section in sectionList:
        if verbose2:
            print("- Comparing {0} with {1}".format(section[0].strip(), sectionName.strip()))

        if section[0].strip() == sectionName.strip():
            if verbose2:
                print("+ FOUND: {0} equals {1}".format(section[0].strip(), sectionName.strip()))
            return section[1:] # return list without the section name
    sectionNotInList.append(sectionName)
    return False


def parameterInList(parameterToFind, list):

    if verbose2:
        print("\nFunction: parameterInList")

    for parametersAndValues in list:
        for parameter in parametersAndValues:

            if verbose2:
                print("- Comparing {0} with {1}".format(parameter, parameterToFind))

            if(parameter == parameterToFind):
                if verbose2:
                    print("+ FOUND: {0} equals {1}".format(parameter, parameterToFind))
                return parametersAndValues[parameter]
        return False


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

for x in list1:
    for i, y in enumerate(x):
        if(i == 0):
            if sectionInList(y, list2):
                print("+ SECTION, ", y.strip(), "IN LIST")
                break
            else:
                pass
                print("x SECTION, ", y.strip(), " NOT IN LIST")

print("Sections not in file", sectionNotInList)
