import re


def convert(py):


    numbers=['1','2','3','4','5','6','7','8','9','0']
    def ser(st,el): #returns el val
        for i in range(len(st)):
            if st[i] == el:
                return i
    def Convert(string): 
        li = list(string.split(" ")) 
        return li 


    def forl(l):
        for i in l:
            fls=''
            if i[:3] == "    ":
                fl+=i+'\n'
        #print(fls)
        return fls
    #preperations
    sl=[]
    fl=[]
    for i in py:
        
        app=''
        if i!='':
            app+=i
        else:
            app=''
        sl.append(app)
    app=''
    for i in sl:
        if i != '\n':
            app+=i 
        else:
            if app != '':
                fl.append(app)
            app=''
    sl=[]
    for i in fl:
        if i == '':
            #print('i reached here')
            fl.remove(i)
        
        if 'import' not in i :
            sl.append(i)
        else:
            sl.append(i)
        
    php_code = []
    ml=[] #all lines in same list ALWAYS
    for i in sl:
        #print(i)
        if i is not None:
            r1 = re.findall(r"print\(.*?\)",i)
            if r1:
                stri=''
                for i in r1:
                    stri+=i
                r2 = re.findall(r"\(.*?\)",stri)
                if r2 is not None:
                    stri=''
                    for j in r2:
                        j = j[1:-1]
                        stri+=j
                        if j[0]=="'" or j[0]=='"':
                            code = "echo " + j + ';'
                            php_code.append(code)
                        else:
                            code = "echo $" + j.strip() + ';'
                            php_code.append(code)
                        
                        for l in j:
                            if l == ",":
                                php_code.pop()
                                j= "echo " + j[:j.index(l)+1]+" $" + j[j.index(l)+2:] + " ;"
                                #j= j[:j.index(l)+3]+  j[j.index(l)+4:] + " ;"
                                php_code.append(j)
    #equations
        #print(i)
        lister = Convert(i)
        #print(lister)
        ml.append(lister)
        for k in lister:
            stri=''
            c=0
            #print(j)
            for j in k:
                #print(k)
                if j == "=" or j=="-" or j=="+" or j=="/" or j=="*":
                    c=1
            if c==1:
                #print(re.match(r"[A-Za-z]*",k))
                if re.match(r"[A-Za-z]*",k) and j is not None:
                    stri='$'+k
                    #print(stri)
                    #for j in r1 :
                    #   print(j)

            #php_code.append(i)

        if i is not None:
            r1 = re.findall(r"for\ .?in range\(.?\)",i)
            if r1:
                stri=''
                variable=''
                range=''
                lis=[]
                for j in r1:
                    stri+=j
                    print(j)
                lis = Convert(stri)
                #print(lis)
                for m in lis:
                    if m == "for":
                        variable = lis[lis.index(m)+1]
                range = lis[-1]
                range = range.split("(")
                range = range[1].split(")")[0]
                range = range.split(',')
                #print("for ("+"$"+variable+"; $"+variable+"<="+range[1]+"; $"+variable+"+="+range[2])
                
                if len(range) == 3: 
                    for_loop = "for ("+"$"+variable+";"+ range[0] +"<= $"+variable+"<="+range[1]+"; $"+variable+"+="+range[2]+"){"
                elif len(range)==2:
                    for_loop = "for ("+"$"+variable+";"+range[0]+" $"+variable+"<="+range[1]+" {"
                elif len(range)==1:
                    for_loop = "for ("+"$"+variable+"; $"+variable+"<="+range[0]+" {"
                php_code.append(for_loop)
                php_code.append(forl(sl)+"\n }")
                
                
                




                                
                             

                    


    
    print(ml)
    print(php_code)






py = '''



import manboobs
n= input()
a= input()
b= input()



for x in range(2,n,2):
    answer= (a+b)/x

print("Tewari", akshat)
'''
convert(py)