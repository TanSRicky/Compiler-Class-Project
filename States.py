from Tables import *

reserved = {"return", "\n", "=", ":", ";", "var", "currency", "string", "start", "stop", "program","string"}
lookup = actionTable.copy()
for states in actionTable:
    for ele in actionTable[states]:
        if (states in acceptDict and actionTable[states][ele] == "*"):
            actionTable[states][ele] = "HR"
            lookup[states][ele] = acceptDict[states]
        elif (states not in acceptDict and actionTable[states][ele] != "*"):
            actionTable[states][ele] = "MA"
        else:
            actionTable[states][ele] = "ERROR"

# print(actionTable)
# print(stateDict)
currState = "S0"

# print(actionTable)
# print(lookup)
inputBuffer = []
with open("sample.txt") as fileobj:
    for line in fileobj:
        for ch in line:
            inputBuffer.append(ch)
mchar = ' '
ps = []
ret = ""
looks = []
actions = []
states = []
tokens = []

for ch in inputBuffer:
    unmapped = ch
    # print(ch)
    # print(currState)
    if currState == "S0" and ch == "\n":
        continue
    if ret in reserved:
        currState = "S0"
        states = []
        looks = []
        actions = []
        tokens.append(ret)
        ret = ""
        continue
    if ch in reserved:
        if (ch == '{'): ch = '/'
        if (ch == '}'): ch = '/'
        # print(currState)


        try:
            nextState = stateDict[currState][ch]
            acceptDict[nextState]

            tokens.append((acceptDict[nextState], ret,ch))
            states = []
            looks = []
            actions = []
            currState = "S0"

            ret = ""
            continue
        except:
            # print("Ch failed trying reset")
            try:
                # print("Accepted " + acceptDict[currState])
                # print(ret)
                acceptDict[currState]

                tokens.append((acceptDict[currState], ret,ch))
                states = []
                looks = []
                actions = []
                currState = "S0"
                ret = ""
                continue
            except:
                if (currState == "S14"):
                    ret = ret + ch
                    currState = "S91"
                continue

    if (ch == None or ch == " "):
        continue

    if (ch.isalpha()): ch = "L"
    if (ch.isdigit()): ch = "D"

    if (currState in s and lookup[currState][ch] != "ERROR"):
        # print(actions)
        tokens.append((acceptDict[currState],ret))
        ps.append(ret)
        ret = ""
        states = []
        looks = []
        actions = []
        # print(ch)
        # print(unmapped)
        # print(currState)

        currState = "S0"
        if (actionTable[currState][ch] == "ERROR"):
            continue
        if (actionTable[currState][ch] == "MA"):
            ret = ret + unmapped
            currState = stateDict["S0"][ch]
            continue

        # print("Bottom state " + currState)
        # print("Bottom ch " + ch)

    currState = stateDict[currState][ch]

    try:
        looks.append(lookup[currState][ch])
        actions.append(actionTable[currState][ch])
    except:
        print("")
    ps.append(ret)
    states.append(currState)
    ret = ret + unmapped

