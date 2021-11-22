from Tables import *
reserved = {"return","\n", "=",":",";","var","currency","string","start","stop","program"}
lookup = actionTable.copy()
for states in actionTable:
    for ele in actionTable[states]:
        if(states in acceptDict and actionTable[states][ele]== "*"):
                actionTable[states][ele] = "HR"
                lookup[states][ele] = acceptDict[states]
        elif(states not in acceptDict and actionTable[states][ele]!= "*"):
                actionTable[states][ele] = "MA"
        else:
              actionTable[states][ele] = "ERROR"
               
#print(actionTable)
#print(stateDict)
currState = "S0"

#print(actionTable)
#print(lookup)
inputBuffer = []
with open("sample.txt") as fileobj:
    for line in fileobj:  
       for ch in line:
             inputBuffer.append(ch)
mchar =  ' ';       
ps = []
ret = ""
looks = []
actions =[]
states = []
for ch in inputBuffer:
         unmapped = ch
         #print(ch)
         #print(currState)
         if currState == "S0" and ch == "\n":
             continue
         if ret in reserved :
             print("Found reserved ret")
             print(ret)
             
             
             currState ="S0"
             
             states = []
             looks = []
             actions = []
     
             ret = ""
             continue
         if ch in reserved :
             if(ch == '{'): ch = '/'
             if(ch == '}') : ch = '/'
             #print("Found reserved ch")
             #print(currState)
             #print(ch)
       
             try:
                 nextState = stateDict[currState][ch]
                 acceptDict[nextState]
                 
                 print("Found token " + str(ret) , end = " ")
                 
                 
                 print("of type " + acceptDict[nextState])
                 states = []
                 looks = []
                 actions = []
                 currState = "S0"
             
                 ret = ""               
                 continue
             except:
                 #print("Ch failed trying reset")
                 try:
                     #print("Accepted " + acceptDict[currState])
                     #print(ret)
                     acceptDict[currState]
                     print("Found token " + str(ret) , end = " ")
                 
                 
                     print("of type " + acceptDict[currState])
                     states = []
                     looks = []
                     actions = []
                     currState = "S0"
                     ret = ""
                     continue
                 except:
                     #print("Failed to be on accept")
                     if(currState == "S14"):
                         ret = ret + ch
                         currState = "S91"
                     continue
                

         if( ch == None or ch == " " ):
            continue
            
         if(ch.isalpha()): ch = "L"
         if(ch.isdigit()): ch = "D"

         if( currState in s and lookup[currState][ch] != "ERROR"):
           #print(actions)
           print("Found token " + str(ret), end = " ")
           print("of type " + acceptDict[currState])
           ps.append(ret)
           ret = ""
           states = []
           looks = []
           actions = []
           #print(ch)
           #print(unmapped)
           #print(currState)
           print(looks)
           currState = "S0"
           if(actionTable[currState][ch] =="ERROR"):
              
               continue
           if(actionTable[currState][ch] =="MA"):
               ret = ret + unmapped
               currState = stateDict["S0"][ch]
               continue
         
           
        
         #print("Bottom state " + currState)
         #print("Bottom ch " + ch)
           print(looks)
           print(actions)
           print(states)
           print(ret)
         currState = stateDict[currState][ch]

         
         try:
             looks.append(lookup[currState][ch])
             actions.append(actionTable[currState][ch])
         except:
             print("")
         ps.append(ret)
         states.append(currState)
         ret = ret + unmapped



        
##        try:
##            currState = stateDict[currState][ch]
##            looks.append(lookup[currState][ch])
##            actions.append(actionTable[currState][ch])
##            states.append(currState)
##            ret.append(unmapped)
##        except:
##            try:
##                if(currState in s and (currState == "116" or currState == "115")):
##                           currState = stateDict["S117"]["newline"]
##                           ret.append(unmapped)
##                           print("Found token " + str(ret))
##                           print("of type " + looks[len(looks)-1])
##                           ps.append(ret)
##                           ret = []
##                           states = []
##                           looks = []
##                           actions = []
##                           currState = "S0"
##                           continue
##            except:
##                ret.append(ch)
##                print("FAILED at " + currState + " with char " + ch)
##                print(looks)
##                print(actions)
##                print(states)
##                print(ret)
##                break
##
##        
##for ch in inputBuffer:
##        if(ch in reserved) :continue
##        # if currState == ',' :
##            # currState = "S0"
##            # continue
##        # if ch == ';' : 
##            # currState = "S0"
##            # continue
##        if(ch.isalpha()): ch = "L"
##        if(ch.isdigit()): ch = "D"
##        #if(ch == "\n"  and currState == "116" or "117"): currState = "S0"
##        
##
##        
##    
##        if(ch == " " or ch == ""):
##                continue
##
##        if((ch == ';' or ch == "\n") and currState in acceptDict and(currState != "S117" or currState != "S116"or currState != "S115")):  
##                continue
##        elif(ch == "\n" ):
##            ch = "newline"
##               
##        try:
##             print(currState)
##             print(ret)
##             print(lookup[currState][ch])
##             print(actionTable[currState][ch])
##             if currState in acceptDict:
##                     ret.append(ch)
##                     currState = stateDict["S0"][ch]
##                     ps.append(ret)
##                     print(ret)
##                     print(lookup[currState][ch])
##                     print(actionTable[currState][ch])
##                     ret = []
##             else:       
##                
##                    currState = stateDict[currState][ch]
##                    ret.append(ch)
##           # print(ch, end = " " + currState)
##            
##        except:
##                    
##                     continue
##            
##            
##        
        

        
        
# msg = input("1.View\n2.Quit")
# while(msg != "2") :
    # print(stateList)
    # msg = input("1.View\n2.Quit")
