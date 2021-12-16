from time import sleep

from States import *
s = """program -> libtoken libtoken_tail start | start
libtoken_tail -> libtoken libtoken_tail | LAMBDA
libtoken -> library

start -> code | LAMBDA
code -> program id ; vars main end
vars -> var var_type : p_type ; var_type_tail
var_type_tail -> var_type : ptype ; var_type_tail | LAMBDA
var_type -> var var_tail
var_tail -> , var var_tail | LAMBDA
var -> id
ptype -> int | sci | real | currency | string
main -> begin statemt_list return int ;
statemt_list -> statemt statemt_tail
statemt_tail -> statemt statemt_tail | LAMBDA
statemt -> id := exp ; | device_open file ; | for :=  id to id do statemt_list end do ; | repeat do statemt_list until ( bool ) end do ; | while ( bool ) do statemt_list end do ; | if ( bool ) then begin statemt_list end ; else begin statemt_list end ; | device_close file ; | read_from_device file ; | write_to_device file ; | writeln ( exp ) ; | readln ( var_type ) ;
bool -> exp relational_op exp
relational_op -> < | > | <= | >= | == | !=
exp -> primary primary_tail | string
primary_tail -> + primary primary_tail | - primary primary_tail | LAMBDA
primary -> secondary sec_tail
sec_tail -> * secondary sec_tail | / secondary sec_tail | LAMBDA
secondary -> ( exp ) | id | int | real | sci | currency | abs ( exp ) | fabs ( exp )
end -> stop"""

left = []
lines = []
first = True
grammar = dict()
wordByWord = []
for line in s.split("\n"):
    tmp = []
    for word in line.split(" "):
        wordByWord.append(word)
        if first:
            grammar[word] = ""
            left.append(word)
            first = False
            continue
        else:
            tmp.append(word)
    grammar[left[(len(left) - 1)]] = tmp
    first = True
    lines.append(tmp)
noBrackLeft = []

terminals = set()
for line in s.split("\n"):
    for word in line.split(" "):
        if word not in left:
            terminals.add(word)
for i in range(len(left)):
    noBrackLeft.append(left[i])
    left[i] = "<" + left[i] + ">"



firstfollow = dict()

delimitedText = """<program> \n
<libtoken> <libtoken_tail> <start> 
| <start> 
<libtoken_tail> \n <libtoken> <libtoken_tail> | LAMBDA
<libtoken> \n library <> 
<start> \n <code> | LAMBDA 
<code> \n <program> id ; <vars> <main> <end> 
<vars> \n <var> <var_type> : p_type ; <var_type_tail> 
<var_type_tail> \n <var_type> : <ptype> ; <var_type_tail> | LAMBDA 
<var_type> \n <var> <var_tail>
<var_tail> \n , <var> <var_tail> | LAMBDA
<var> \n id 
<ptype> \n int | sci | real | currency | string 
<main> \n begin <statemt_list> return int ; 
<statemt_list> \n <statemt> <statemt_tail>
<statemt_tail> \n <statemt> <statemt_tail> | LAMBDA 
 <statemt> \n id :=  <exp> ; | device_open file ; | for id :=  id to id do <statemt_list> <end> do ; | repeat do <statemt_list> until ( <bool> ) <end> do ; | while ( <bool> ) do <statemt_list> <end> do ; | if ( <bool> ) then begin <statemt_list> <end> ; else begin <statemt_list> <end> ; | device_close file ; | read_from_device file ; | write_to_device file ; | writeln ( <exp> ) ; | readln ( <var_type> ) ; 
 <bool> \n <exp> <relational_op> <exp>
 <relational_op> \n < | > | <= | >= | == | != 
 <exp> \n <primary> <primary_tail> | string 
 <primary_tail> \n + <primary> <primary_tail> | - <primary> <primary_tail> | LAMBDA 
 <primary> \n <secondary> <sec_tail> 
 <sec_tail> \n * <secondary> <sec_tail> | / <secondary> <sec_tail> | LAMBDA 
 <secondary> \n ( <exp> ) | id | int | real | sci | currency | abs ( <exp> ) | fabs ( <exp> )
 <end> \n stop 
"""
for l in left:
    firstfollow[l] = None

delimitedText = delimitedText.replace("|", "\n")
delimitedText.split("\n")


fstr ="""<program>  library  id lambda									|	$ id
<libtoken_tail>  library, LAMBDA								|	$
<libtoken>  library  											|	library $
<start>    library LAMBDA 									|	$
<code>     library											    |; * / = +  -   ;  )
<vars>  id,LAMBDA											    |  , begin  id
<var_type_tail>  id LAMBDA								    |, begin  id
<var_type>  id											  	    | : COMMA )
<var_tail>  id COMMA LAMBDA									|: COMMA  )
<var>  id											  		    | id  COMMA
<ptype>  int  sci  real currency  string 					| ;
<main>  begin													| end
<statemt_list>   LAMBDA										| return end
<statemt_tail>  id device_open  for repeat 				|  id device_open for repeat  return end
 while read_from_device write_to_device writeln readln LAMBDA   				
<statemt> id device_open for repeat                      | id device_open for repeat while read_from_device write_to_device writeln readln LAMBDA  while read_from_device write_to_device writeln readln return end
<bool>   ( id int real sci currency abs fabs					| )

<relational_op>       <   >   <=   >=   ==   != 			     	   |   ( id int real sci currency abs fabs  string 

<exp>   ( id int real sci currency abs fabs  string           | ;  )  <   >   <=   >=   ==   != 	
<primary_tail> = +  -   LAMBDA									|  ;  )
<primary>   ( id int real sci currency abs fabs			| = +  -   ;  ) ;  )  < | > | <= | >= | == | != 	
<sec_tail>   * / LAMBDA									    |= +  -   ;  )
<secondary>  ( id int real sci currency abs fabs				| * /= +  -   ;  )
<end> = stop"""
tmpList = []
fstr = fstr.replace("\t"," ")
for f in fstr.split("\n"):
    for w in f.split(" "):
        if w != '':
            tmpList.append(w)
productionsNaturals = ['<program>  <libtoken> <libtoken_tail> <start>', '<program>  <start> ', '<libtoken_tail>  <libtoken> LAMBDA ', '<libtoken_tail>  LAMBDA', '<libtoken>  library ',
                       '<start> <code> LAMBDA',
                       '<start>  LAMBDA ',
                       '<code>  program id ; <vars> <main> <end> ',
                       '<vars>  <var> <var_type> : p_type ; <var_type_tail> ',
                       '<var_type_tail> <var_type> : <ptype> ; <var_type_tail>  ',
                       '<var_type_tail>  LAMBDA ',
                       '<var_type>  <var> <var_tail>',
                       '<var_tail> <var>',
                       '<var_tail>  LAMBDA',
                       '<var>  id ',
                       '<ptype>   int  ',
                       '<ptype>   sci ',
                       '<ptype>   real  ',
                       '<ptype>   currency '
                       , '<ptype>   string '
                           , '<main>   begin <statemt_list> return int ; ', '<statemt_list>   <statemt> <statemt_tail>', '<statemt_tail>   <statemt> <statemt_tail>', '<statemt_tail>   LAMBDA ', '<statemt>   id :: <exp> ; ', '<statemt>   device_open file ;', '<statemt>    for id :: id to id do <statemt_list> <end> do ; ', '<statemt>    repeat do <statemt_list> until ( <bool> ) <end> do ; ', '<statemt>    while ( <bool> ) do <statemt_list> <end> do ;', '<statemt>    if ( <bool> ) then begin <statemt_list> <end> ; else begin <statemt_list> <end> ; ', '<statemt>    device_close file ; ', '<statemt>    read_from_device file ; ', '<statemt>    write_to_device file ; ', '<statemt>    writeln ( <exp> ) ; ', '<statemt>    readln ( <var_type> ) ; ', '<bool>   <exp> <relational_op> <exp>',
                    '<relational_op>    <', '<relational_op>   >', '<relational_op>    <=', '<relational_op>    >=', '<relational_op>   ==', '<relational_op>   !=', '<exp>   <primary> <primary_tail>  ', '<exp>    string ', '<primary_tail>   + <primary> <primary_tail> ', '<primary_tail>   - <primary> <primary_tail> ', '<primary_tail>   LAMBDA ', '<primary>   <secondary> <sec_tail> ', '<sec_tail>   * <secondary> <sec_tail> ', '<sec_tail>   / <secondary> <sec_tail> ', '<sec_tail>   LAMBDA ', '<secondary>   ( <exp> ) ', '<secondary>    id ', '<secondary>   int ', '<secondary>   real ', '<secondary>   sci ', '<secondary>   currency ', '<secondary>    abs ( <exp> ) ', '<secondary>   fabs ( <exp> )', '<end>   stop']


firstfollow = {'<program>': [['library', 'id', 'lambda'], ['$', 'id']], '<libtoken_tail>': [['library', 'LAMBDA'], ['$']],
               '<libtoken>': [['library'], ['library', '$']],
            '<start>': [['library', 'LAMBDA'], ['$']],
            '<code>': [['library'], [';', '*', '/', '=', '+', '-', ';', ')']], '<vars>': [['id', 'LAMBDA'], [',', 'begin', 'id']],
               '<var_type_tail>': [['id', 'LAMBDA'], [',', 'begin', 'id']],
               '<var_type>': [['id', ], [ ':', 'COMMA', ')']],
               '<var_tail>': [['id', 'COMMA', 'LAMBDA'], [':', 'COMMA', ')']],
               '<var>': [['id', ], [ 'id', 'COMMA']],
               '<ptype>': [['int', 'sci', 'real', 'currency', 'string'], [';']], '<main>': [['begin'], ['end']],
               '<statemt_list>': [['LAMBDA'], ['return', 'end']],
               '<statemt_tail>': [['id', 'device_open', 'for', 'repeat'], ['id', 'device_open', 'for', 'repeat', 'return', 'end', 'while', 'read_from_device', 'write_to_device', 'writeln', 'readln', 'LAMBDA']],
             '<statemt>': [['id', 'device_open', 'for', 'repeat'], ['id', 'device_open', 'for', 'repeat', 'while', 'read_from_device', 'write_to_device', 'writeln', 'readln', 'LAMBDA', 'while', 'read_from_device', 'write_to_device', 'writeln', 'readln', 'return', 'end']],
             '<bool>': [['(', 'id', 'int', 'real', 'sci', 'currency', 'abs', 'fabs'], [')']],
    '<relational_op>': [[';', ')', '<', '>', '<=', '>=', '==', '!='], ['(', 'id', 'int', 'real', 'sci', 'currency', 'abs', 'fabs', 'string']],
'<exp>': [['(', 'id', 'int', 'real', 'sci', 'currency', 'abs', 'fabs', 'string'], [';', ')', '<', '>', '<=', '>=', '==', '!=']],
'<primary_tail>': [['=', '+', '-', 'LAMBDA'], [';', ')']],
               '<primary>': [['(', 'id', 'int', 'real', 'sci', 'currency', 'abs', 'fabs', ], [ '=', '+', '-', ';', ')', ';', ')', '<',  '>', '<=', '>=',  '==', '|', '!=']], '<sec_tail>': [['*', '/', 'LAMBDA'], ['=', '+', '-', ';', ')']],
               '<secondary>': [['(', 'id', 'int', 'real', 'sci', 'currency', 'abs', 'fabs'], ['*', '/=', '+', '-', ';', ')']],
               '<end>': [['stop'],[';', "'", '*', '/', '=', '+', '', '-', '', '', ';', '', ')']]}
for t in terminals:
    firstfollow[t] = [[t],[]]

count = 0
errorLog = []
predicts = []
lambdas = []
pLines = []
for pn in productionsNaturals:
    for element in pn.split(" "):

        try:
          predicts.append(firstfollow[element])
        except:
            s = element + " not found"
            errorLog.append(s)
            continue
        for a in firstfollow[element]:
            for l in a:
                    if(l == 'LAMBDA'):
                        lambdas.append(count)
    pLines.append(predicts)
    predicts = []
    count = count + 1


leftSideSets = []
# for p in predicts:
#     leftSideSets = p[0]
#     p[0] = None
# print(predicts)
# print(len(productionsNaturals))
# print(len(predicts))

#
count = 0

for p in pLines:
    count = count + 1
    leftSideSets.append(p[0])
    p[0] =None


count = 0
pSets = []
for j in range(len(pLines)):
    pLines[j] = list(filter(None, pLines[j]))
for i in range(60):
    lmbda = False
    s = set()

    for l in range(len(pLines[i])):
       if(pLines[i][l][0].count('LAMBDA') > 0):
           for ele in pLines[i][l][0] :
               s.add(ele)
           for ele in leftSideSets[i][1]:
               s.add(ele)
       else:
           for ele in pLines[i][l][0]:
               s.add(ele)
    pSets.append(s)


pnList = []
for pn in productionsNaturals:
    pnList.append(pn.split(" "))
left = []
right = []
for i, pn in enumerate(pnList):
    firstPass = True
    first = ""
    seconds = []
    for ele in pnList[i]:
        if firstPass :
            left.append(ele)
            first = ele
            firstPass = False

            continue
        if( ele == ''): continue
        seconds.append(ele)
    right.append(seconds)



stack = ['$','<program>']

toks = []

pSets = [{'id', '$', 'LAMBDA', 'library'},
         {'id', '$', 'LAMBDA', 'library'},
         {'$', 'LAMBDA', 'library'},
         {'$', 'LAMBDA'},
         {'LAMBDA'},
         {'$', 'LAMBDA'},
         {'/', '=', ')', 'LAMBDA', 'begin', '+', 'library', ';', 'id', '-', '*', 'lambda', 'stop'},
         {'LAMBDA', 'begin', ',', ':', 'p_type', ';', 'id'},
         {'real', 'LAMBDA', 'begin', ',', 'currency', ':', ';', 'id', 'int', 'string', 'sci'},
         {'begin', 'id', ',', 'LAMBDA'}, {')', 'COMMA', 'LAMBDA', ':', 'id'},
         {')', 'COMMA', 'LAMBDA', ':', 'id'}, {')', 'COMMA', ':', 'LAMBDA'},
         {'id'}, {'int'}, {'sci'}, {'real'}, {'currency'},
         {'string'}, {'LAMBDA', 'return', 'begin', 'end', ';', 'int'},
         {'repeat', 'for', 'device_open', 'id'},
         {'repeat', 'for', 'device_open', 'id'},
         {'for', 'device_open', 'LAMBDA', 'return', 'end', 'while', 'read_from_device', 'write_to_device', 'repeat', 'writeln', 'id', 'readln'},
         {'real', '(', 'fabs', 'currency', ';', 'abs', 'id', 'int', 'string', 'sci'}, {';', 'device_open', 'file'},
         {'do', 'for', 'LAMBDA', 'device_open', 'while', 'write_to_device', 'read_from_device', 'return', 'end', 'to', 'repeat', 'writeln', ';', 'id', 'readln', 'stop'},
         {'do', 'write_to_device', 'LAMBDA', 'until', 'writeln', ';', ')', 'real', 'for', 'device_open', 'while', 'return', 'read_from_device', 'fabs', 'abs', 'id', 'int', '(', 'readln', 'stop', 'end', 'repeat', 'currency', 'sci'},

         {'do', 'write_to_device', 'LAMBDA', 'writeln', ';', ')', 'real', 'for', 'while', 'device_open', 'return', 'fabs', 'read_from_device', 'abs', 'id', '(', 'int', 'readln', 'stop', 'end', 'repeat', 'currency', 'sci'},

         {'write_to_device', 'LAMBDA', 'writeln', ';', 'if', 'then', ')', 'real', 'for', 'device_open', 'while', 'begin', 'return', 'fabs', 'read_from_device', 'abs', 'id', '(', 'int', 'readln', 'stop', 'else', 'end', 'repeat', 'currency', 'sci'},
         {'device_close', ';', 'file'},
         {'read_from_device', ';', 'file'},
         {'write_to_device', ';', 'file'},
         {')', 'real', '(', 'fabs', 'writeln', 'currency', ';', 'abs', 'id', 'int', 'string', 'sci'}, {')', ';', 'id', '(', 'readln'}, {')', 'real', '(', '>=', '==', '!=', 'fabs', 'currency', '>', ';', 'abs', 'id', 'int', 'string', '<', '<=', 'sci'},

         {'<'}, {'>'}, {'<='}, {'>='}, {'=='}, {'!='},

         {'<', '<=', '=', 'LAMBDA', '>', 'sci', ';', ')', 'real', '==', 'fabs', '+', 'abs', 'id', '(', 'int', '!=', 'currency', '-', '>='},
         {'string'},
         {'=', 'real', '(', ')', 'LAMBDA', 'fabs', '+', 'currency', ';', 'abs', 'id', 'int', '-', 'sci'}, {'=', 'real', '(', ')', 'LAMBDA', 'fabs', '+', 'currency', ';', 'abs', 'id', 'int', '-', 'sci'}, {')', ';', 'LAMBDA'},
         {'|', '<', '<=', '/', '=', '>=', 'LAMBDA', '>', ';', '*', ')', 'real', '==', 'fabs', '+', 'abs', 'id', '(', 'int', '!=', 'currency', '-', 'sci'}, {'/', 'real', '(', '=', ')', 'LAMBDA', 'fabs', '+', 'currency', ';', 'abs', 'id', 'int', '-', '*', 'sci'}, {'/', 'real', '(', '=', ')', 'LAMBDA', 'fabs', '+', 'currency', ';', 'abs', 'id', 'int', '-', '*', 'sci'}, {'=', ')', 'LAMBDA', '+', ';', '-'}, {')', 'real', '(', 'fabs', 'currency', 'abs', 'id', 'int', 'string', 'sci'}, {'id'}, {'int'}, {'real'}, {'sci'}, {'currency'}, {')', 'real', '(', 'fabs', 'currency', 'abs', 'id', 'int', 'string', 'sci'}, {')', 'real', '(', 'fabs', 'currency', 'abs', 'id', 'int', 'string', 'sci'}, {'stop'}]


tPointer = 0
print("Ricky Tan Grammar Submission")
terminals.add("LAMBDA")
terminals.add('program')
pred = pSets[0]
tokens.append("$")
while True:
    print("Currently at Token number ", end = " ")
    print(tPointer)
    currentToken = tokens[tPointer]
    if(currentToken == "$"):
        print("Found $")
        print("Ending predictive parsing procedure")
        break
    print(currentToken)

    mappedToken = currentToken[0].lower()
    # lookAhead = tokens[tPointer+1]
    # print("look ahead ")
    # print(lookAhead)
    # nextToken = lookAhead[0].lower()
    # print(nextToken)
    # if (len(lookAhead) == 1):
    #     nextToken= "<" + tokens[tPointer+1] + ">"
    if (mappedToken == "comment"):
        print("Comment, skipped")
        tPointer = tPointer + 1
        continue
    if(len(mappedToken) == 1) :
        mappedToken = "<" + tokens[tPointer] + ">"
    if(mappedToken == "comment") :
        print("Comment, skipped")
        tPointer = tPointer + 1
        continue




    if(stack[-1] in terminals):
        print("MATCH----- POPPING")
        stack.pop()
        tPointer = tPointer + 1
        print("STACK")
        print(stack)
        continue
    else:
        prod = stack.pop()
        print(" non MATCH-----")
        index = left.index(prod)
        print("FIRING PRODUCTION " + str(index), end = " ")
        pred = pSets[index]
        print( left[index] , end = " ")
        print("->" + str(right[index]))

        for r in reversed(right[index]):
            print("Push " + r , end = " ")
            stack.append(r)
        print("STACK")
        print(stack)
    print()

input()
print("Ricky Tan Grammar Submission")
# if(mappedToken == "id" and prod ==";"):
    #     print("Found ID and colon ")
    #     print(mappedToken + prod)
    #     tPointer = tPointer+1
    #     continue
    # if (mappedToken == "id" and prod == ":"):
    #     print("Found ID and colon")
    #     print(mappedToken + prod)
    #     tPointer = tPointer + 1
    #     continue
    #
    # if (mappedToken == "id" and prod == "p_type"):
    #     print("Found TYPE")
    #     print(mappedToken + prod)
    #     tPointer = tPointer + 1
    #     continue
    # if( tokens[tPointer] == 'currency' and prod ==';' ):
    #     print("Found Currensy and semicolon")
    #     print(tokens[tPointer] + prod)
    #     tPointer = tPointer + 1
    #     continue
    # if(mappedToken == "id" and currentToken[len(currentToken)-1]) ==":" :
    #     print("Found assignment ")
    #     print( tokens[tPointer+1])
    #     tPointer = tPointer + 1
    #     continue
    # if(mappedToken == "id" and currentToken[len(currentToken)-1]) ==":" :
    #     print("Found assignment ")
    #     print( tokens[tPointer+1] + ":")
    #     tPointer = tPointer + 1
    #     continue
    # if(mappedToken == "id" and prod  == "int") :
    #     print("Found assignment ")
    #     print("id")
    #     print("int")
    #     tPointer = tPointer + 1
    #     continue
    # if(tokens[tPointer] == "start") :
    #     print("found START")
    #     print(stack)
    #     tPointer = tPointer + 1
    #     continue
    #

    # else:
    #     print(" non MATCH-----")
    #     try:
    #        index = left.index(prod)
    #        print("FIRING PRODUCTION " + index, end = " ")
    #     except:
    #        if(prod in reserved):
    #            continue
    #
    #        pred = pSets[index]
    #
    #
    #     print("Left " + left[index])
    #     print("right " + str(right[index]))
    #
    #     for r in reversed(right[index]):
    #         print("Push " + r , end = " ")
    #         stack.append(r)
    #     print()
    #     print("STACK")
    #     print(stack)
    #     input()




