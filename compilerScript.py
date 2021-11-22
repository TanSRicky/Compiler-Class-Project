charArray = ['L', 'D','}', '{', 'newline', '^', ']', '\\', '[',  'ABN', '@', '>', '<', ';', ':', '/', '.', ',', '*/',  ')', '(', "'=", "'-", "'+", "'", '&', '$', '#', '"', '!']
s ="""S0{1,15,33,56,108,113,118,94,130,135,138,145}
r [ {S1}
r # {S2}
r " {S3}
r $ {S4}
r : {S5}
r - {S6}
r / {S98}
r < {S11}
r > {S99}
r L {S12}
r D {S13}
r { S104

S1{104}
r : {S14}

S2{34}
r L {S15}

S3{114}
r ABN
r " S30

S4{16}
r D S16

S5{146}
S7{2,14}
r S8
S8{3,5,14}
r , S9
r d S303
S9{3,5}
r D S305
r , S43
S10{147}
S11{136}
S12{131,132} ACCEPT


S14{105}
r ] {
r .
S15{35}
r L  S100
S16{29,17}
r D
r .
r , S212
S17{29,18}
r D S19
r , S212
r . S18
S18{30}
r D S27
S19{29,19}
r D S211
r , S20

S20{21,20}
r D S21
S21{22,25}
r D S22
S22{23,26}
r D S23
S23{24,27}
r , S20
r . S18
S24{26}
r  D S25
S25{27}
r . S26
S26{30}
r D S27
S27{31}
r D S28
S28{32} ACCEPT
S29{115,116}
r \"
r ABN
r " S30
S30{117} ACCEPT
S31{35,36,38}
r < {S32}
r " {S33}
r L {S100}
r D {S100}
S32{39}
r L {S34}
S33{46}
r L S35
S34{40}
r L {S36}
r D {S37}

S36{40,41,43}
r . {S40}
r > {S41}
r D {S37}
S37{40,42,43}
r . {S40}
r > {S41}
r L {S36}
S38{46}
r L {S39}
S39{47}
r L {S47}
r D {S48}
S40{44}
r L S42
S41{55} ACCEPT
S42{45}
r > S41
S43{6,7}
r d s44
S44{8,11}
r D S45
S45{9,12}     ACCEPT
r D 305
S47{47,48,50,55}
r . S49
S48{47,49,50,55}
r . S49
S49{51,54}
r L S50
S50{52,54}
r L {S51}
S51{53}
r L {S52}
S52{54}
r " {S41}
S13{56,951,14}
r D S53
S53{58,63,71,73,75,952}
r D S54
r + S85
r - S85
r . S82
S54{59,61,64,72,74}
r . S70
r D S55
S55{65,71,73,75}
r D S56
S56{66,74,76,78}
r D
r , {S57}
S57{67,69,75,79}
r D {S58}
S58{68,70,76,80}
r . {S70}
r D S999
S59{89,93,94}
r D
S60{66,74,76,78}
r ,
S61{67,75,69}
r D S450
S450{68,76,70}
r D S451
r . S70
S451{69,77}
r D S452
S452{70,78}
r , S65
r . s70
S62{77,76}
r D S63
S63{78,77}
r , S65
r D S64
S64{78}
r , S65
S65{75,79}
r D S66
S66{76,80}
r D S67
S67{77,81}
r D S68
r . S70
S68{75,79,81}
r D S66
S70{83,86,87}
r D S72
S72{84,86,88}
r D S74
S74{86,89}
r D S75
S75{90,93}
r D 86
r , S77
S76{81}
r . S70
S77{87,91,93}
r D S78
S78{88,92,94}
r D S80
S80{89,93}
r D S81
S81{90,94}
r d S101
r , S77
S82{96}
r + s85
r - s85
S85{99,101}
r D S86
S86{100,102}
r D S87
S87{101}
r D S88
S88{102}	ACCEPT
S89{105}
r L S90
S90{106}
r ] S92
r D S91
S91{107}
r L S90
r ] S92
r . S93
S92{112}	ACCEPT
S93{108,109}
r ] S92
r L S102

S98{119}
r / S108
r *
S99{140}
S100{35,37,38}
r < {S32}
r " {S33}
r L {S31}
r D {S31}
S101{94}			ACCEPT
S102{110}
r ] S92
r D S103
S103{111}
r ] S92
r L S102
S104{126}
r * S105

S105{127}
r * S106
r ABN
S106{128}
r } S107
S107{129} ACCEPT
S108{123}
r ABN S116
S109{120}
S111{68,76,70}
r . S70
r D S112
S112{69,76}
r D S113
S113 {70,77}
r . S70
r D S64
S114{121}
r */ S115
S115{122} accept
S116{124}
r newline S117
S117{125}	accept


S211{29}
r . S18
S212{19}
r , s20


S999{77,81,69}
r . S70
r D S899
S899 {78,80}
r , S65
r D S76
S304{4,5} S305
r , S43
r D S305
S305{5}
r , S43
S303{14}	ACCEPT
"""

class State:
    state = ""
    nodes = []
    reads = []
    charReads = {'L':'*', 'D':'*','}':'*', '{':'*', 'newline':'*', '^':'*', ']':'*', '\\':'*', '[':'*',  'ABN':'*', '@':'*', '>':'*', '<':'*', ';':'*', ':':'*', '/':'*', '.':'*',
                 ':':'*' , ':':'*', '*/':'*',  ')':'*', '(':'*', "'=":'*', "'-":'*', "'+":'*', "'":'*', '&':'*', '$':'*', '#':'*', '"':'*','!':'*'}

    def __init__(self):
        True
    def printState(self):
        print(self.state, end = "\n")
    def printNodes(self):
        for n in self.nodes:
            print(n, end=' ')
        print()
    def setCharRead(self,x,y):
        self.charReads[x] = y
           
                            
                        
                           
                      
    def printData(self):
         self.printState()
         self.printNodes()
         self.printReads()
    def mapReads(self):
        chTmp = ""
        found = False
    
        for l in self.reads:
            index = 0
            found = False
            for i in range(len(l)):
                if found:
                    print(l[i])
                   
                if l[i] in charSet:
                    found = True
                    index = i
                    continue
                 
              
    def getReads(self):
       for a in self.charReads:
        print(a, end = " ")
        print(self.charReads[a], end = " ")
       print()
    def getReadOrder(self):   
      for a in self.charReads:
            print(a + " " + charReads[a], end = "|")
      print()
                    

                    
                    
       
        




accumString = ""
append = False
sets = []
states = []
newState = True
tState = State()
tmpReads = []
prevState = State()
accepts = []
bigReads = []
for l in s.split('\n'):
    l = l.replace("\t","")
    setName = ""
    if ((l.find("S") == 0 or l.find("s") == 0)):
        start =l.find("{")
        end =l.find("}")
       
        setName = l[0:int(start)]
        
        setString = l[int(start):int(end)+1]
        nList = l[int(start)+1:int(end)].split(",")
        
        for n in nList:
            n = int(n)
        tState.nodes = nList
        tState.state = setName
        states.append(tState)
        tState.reads = tmpReads
        #print(tState.reads)
        bigReads.append(tmpReads)
        tmpReads = []    #print(tState.nodes)
        tState = State()
    else:
         tmpReads.append(l.split(" "))

    if(l.lower().find("accept") > 0):
        accepts.append(setName)
                  

        

for i in range(len(states)-1):
   states[i].reads = bigReads[i+1]
def exportCSV():
    for s in states:
        print("{('" + s.state, end = """'):{""" ),
        for c in  charArray:
            currRead = c
            print("('"+c,end = "':")
            corrState = ""
            found = False
            for r in s.reads:#for every read line 
                #go through read elements
                for ele in range(len(r)-1):
                      if r[ele] == 'r':
                          if(ele < len(r)-2):ele = ele + 1
                      if(r[ele] == c):
                          r[ele+1] = r[ele + 1].replace("{","")
                          r[ele+1] = r[ele + 1].replace("}","")
                          r[ele+1] = r[ele + 1].replace("(","")
                          r[ele+1] = r[ele + 1].replace(")","")
                          if(r[ele + 1] == "\\") :print ("\\\\")
                          print("'" + r[ele + 1], end = "'),")
                          corrState = r[ele + 1]
                          found = True
                          break
            if not found:
                print("'*", end = "'),")
                corrState = "*"
      
        print("}}",end = "\n")
def printNonCSV():
    for s in states:
        print(" " + s.state, end = "")
        for c in  charArray:
            currRead = c
            
            corrState = ""
            found = False
            for r in s.reads:#for every read line 
                #go through read elements
                for ele in range(len(r)-1):
                      if r[ele] == 'r':
                          if(ele < len(r)-2):ele = ele + 1
                      if(r[ele] == c):
                          r[ele+1] = r[ele + 1].replace("{","")
                          r[ele+1] = r[ele + 1].replace("}","")
                          r[ele+1] = r[ele + 1].replace("(","")
                          r[ele+1] = r[ele + 1].replace(")","")
                          print(" " + r[ele + 1], end = "  ")
                          s.setCharRead(c,r[ele + 1])
                          found = True
                          break
           
            if not found:
                print("*", end = "\t")
                corrState = "*"
                s.setCharRead(c,corrState)

        print()
exportCSV()

    
                  
        
    
##for i in range(len(states)-1):
##    print('\'',end = "")
##    print(states[i].state, end = "'" )
##    for n in states[i].reads:
##            for el in n:
##                if el == "r":
##                    continue
##                print('\'',end = ",")
##                print (el, end = "'")
##    print(",", end = "}\n")
##    states[i].printState()
##    states[i].printReads()
##    states[i].getReads()
##    print()
   
  #  print()
   # states[i+1].getReads()
























