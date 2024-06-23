import math
digit={'ноль':0,"один":1,"два":2,"три":3,"четыре":4,"пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,\
    "одиннадцать":11,"двенадцать":12,"тринадцать":13,"четырнадцать":14,"пятнадцать":15,"шестнадцать":16,"семнадцать":17,"восемнадцать":18,"девятнадцать":19,\
    "десять":10,"двадцать":20,"тридцать":30,"сорок":40,"пятьдесят":50,"шестьдесят":60,"семьдесят":70,"восемьдесят":80,"девяносто":90,\
    'плюс':'+','минус':'-','умножить':'*'}
tabl={0:'ноль',1:"один",2:"два",3:"три",4:"четыре",5:"пять",6:"шесть",7:"семь",8:"восемь",9:"девять",\
    11:"одиннадцать",12:"двенадцать",13:"тринадцать",14:"четырнадцать",15:"пятнадцать",16:"шестнадцать",17:"семнадцать",18:"восемнадцать",19:"девятнадцать",\
    10:"десять",20:"двадцать",30:"тридцать",40:"сорок",50:"пятьдесят",60:"шестьдесят",70:"семьдесят",80:"восемьдесят",90:"девяносто",\
    100:'сто',200:'двести',300:'триста',400:'четыреста',500:'пятьсот',600:'шестьсот',700:'семьсот',800:'восемьсот',900:'девятьсот',\
    1000:'тысяча',2000:'две тысячи',3000:'три тысячи',4000:'четыре тысячи',5000:'пять тысяч',6000:'шесть тысяч',7000:'семь тысяч',8000:'восемь тысяч',9000:'девять тысяч'}
komb={'ноль':0,"одного":1,"двух":2,"трех":3,"четырех":4,"пяти":5,"шести":6,"семи":7,"восьми":8,"девяти":9,\
    "одиннадцати":11,"двенадцати":12,"тринадцати":13,"четырнадцати":14,"пятнадцати":15,"шестнадцати":16,"семнадцати":17,"восемнадцати":18,"девятнадцати":19,\
    "десяти":10,"двадцати":20,"тридцати":30,"сорока":40,"пятьдесяти":50,"шестьдесяти":60,"семьдесяти":70,"восемьдесяти":80,"девяноста":90,}

def f(result=str(input()).split(' ')):
    pov=list(result)
    ls=[]
    for i in range(len(pov)):
        if pov[i] not in ['на','из','по']:
            ls.append(pov[i])
    count=len(ls)
    k=''
    itog=0
    if ls[0] in ['размещений','перестановка','сочетаний']:
        if ls[0]=='размещений':
            kb=1
        if ls[0]=='перестановка':
            kb=2
        if ls[0]=='сочетаний':
            kb=3
        ls.remove(ls[0])
        if kb==1:
            ls[0]=komb.get(ls[0])
            ls[-1]=digit.get(ls[-1])
            itog=math.factorial(ls[0])//math.factorial(ls[0]-ls[-1])
        if kb==2:
            ls[0]=komb.get(ls[0])
            itog=math.factorial(ls[0])
        if kb==3:
            ls[0]=komb.get(ls[0])
            ls[-1]=digit.get(ls[-1])
            itog=math.factorial(ls[0])//(math.factorial(ls[-1])*math.factorial(ls[0]-ls[-1]))

    else:
        for i in range(count):
            ls[i]=digit.get(ls[i])
        znak1=1
        znak2=1
        if ls[0]=='-':
            znak1=-1
            del ls[0]
        count=len(ls)
        k=0
        for i in range(count):
            if ls[i]=='-' or ls[i]=='+' or ls[i]=='*':
                k=i
                break
        if ls[k+1]=='-':
            znak2=-1
            del ls[k+1]
        count=len(ls)
        if count==3:
            for i in range(count):
                if ls[i]=='-':
                    itog=znak1*ls[0]-znak2*ls[-1]
                if ls[i]=='+':
                    itog=znak1*ls[0]+znak2*ls[-1]
                if ls[i]=='*':
                    itog=znak1*ls[0]*znak2*ls[-1]
                    
        if count==4:
            for i in range(count):
                if ls[i]=='-' and i==1:
                    itog=znak1*ls[0]-znak2*(ls[-1]+ls[-2])
                if ls[i]=='-' and i==2:
                    itog=znak1*(ls[0]+ls[1])-znak2*ls[-1]  
                if ls[i]=='+' and i==1:
                    itog=znak1*ls[0]+znak2*(ls[-1]+ls[-2])
                if ls[i]=='+' and i==2:
                    itog=znak1*(ls[0]+ls[1])+znak2*ls[-1]
                if ls[i]=='*' and i==1:
                    itog=znak1*ls[0]*znak2*(ls[-1]+ls[-2])
                if ls[i]=='*' and i==2:
                    itog=znak1*(ls[0]+ls[1])*znak2*ls[-1]
                
        if count==5:
            for i in range(count):
                if ls[i]=='-':
                    itog=znak1*(ls[0]+ls[1])-znak2*(ls[-1]+ls[-2])
                if ls[i]=='+':
                    itog=znak1*(ls[0]+ls[1])+znak2*(ls[-1]+ls[-2])
                if ls[i]=='*':
                    itog=znak1*(ls[0]+ls[1])*znak2*(ls[-1]+ls[-2])

    if itog<0:
        itog*=-1
        k='минус '

    if len(str(itog))==1 or (len(str(itog))==2 and str(itog)[0]=='1'):
        part1=tabl.get(itog)
        if itog=='ноль':
            print('ноль')
        if k=='минус ':
            return k+part1
        if k!='минус ':
            return part1
    if len(str(itog))==2:
        perv=itog//10*10
        vtr=itog%10
        part1=tabl.get(perv)
        part2=tabl.get(vtr)
        if k=='минус ' and part2=='ноль':
            return k+part1
        if k=='минус ' and part2!='ноль':
            return k+part1+' '+part2
        if k!='минус ' and part2=='ноль':
            return part1
        if k!='минус ' and part2!='ноль':
            return part1+' '+part2
        
    if len(str(itog))==3:
        perv=itog//100*100
        vtr=itog%100//10*10
        tret=itog%10
        part1=tabl.get(perv)
        part2=tabl.get(vtr)
        part3=tabl.get(tret)
        if k=='минус ' and part2=='ноль' and part3=='ноль':
            return k+part1
        if k!='минус ' and part2=='ноль' and part3=='ноль':
            return part1
        if k=='минус ' and part3=='ноль':
            return k+part1+' '+part2
        if k=='минус ' and part3!='ноль':
            return k+part1+' '+part2+' '+part3
        if k!='минус ' and part3=='ноль':
            return part1+' '+part2
        if k!='минус ' and part3!='ноль':
            return part1+' '+part2+' '+part3
        if k=='минус ' and part2=='ноль':
            return k+part1+' '+part3
        if k=='минус ' and part2!='ноль':
            return k+part1+' '+part2+' '+part3
        if k!='минус ' and part2=='ноль':
            return part1+' '+part3
        if k!='минус ' and part2!='ноль':
            return part1+' '+part2+' '+part3

    if len(str(itog))==4:
        perv=itog//1000*1000
        vtr=itog//100%10*100
        tret=itog%100//10*10
        chet=itog%10
        part1=tabl.get(perv)
        part2=tabl.get(vtr)
        part3=tabl.get(tret)
        part4=tabl.get(chet)
    if k=='минус ' and part2=='ноль' and part3=='ноль' and part4=='ноль':
        return k+part1
    if k!='минус ' and part2=='ноль' and part3=='ноль' and part4=='ноль':
        return part1
    if k=='минус ' and part2=='ноль' and part3=='ноль':
        return k+part1+' ' +part4
    if k!='минус ' and part2=='ноль' and part3=='ноль':
        return part1+' ' +part4
    if k=='минус ' and part2=='ноль' and part4=='ноль':
        return part1+' ' +part3
    if k!='минус ' and part2=='ноль' and part4=='ноль':
        return part1+' ' +part3
    if k=='минус ' and part3=='ноль' and part4=='ноль':
        return k+part1+' '+part2
    if k!='минус ' and part3=='ноль' and part4=='ноль':
        return part1+' '+part2
    if k=='минус ' and part3=='ноль':
            return k+part1+' '+part2+' '+part4
    if k=='минус ' and part3!='ноль':
        return k+part1+' '+part2+' '+part3+' '+part4
    if k!='минус ' and part3=='ноль':
            return part1+' '+part2+' '+part4
    if k!='минус ' and part3!='ноль':
        return part1+' '+part2+' '+part3+' '+part4
    if k!='минус ' and part3!='ноль':
        return part1+' '+part2+' '+part3+' '+part4
    if k=='минус ' and part2=='ноль':
        return k+part1+' '+part3+' '+part4
    if k=='минус ' and part2!='ноль':
        return k+part1+' '+part2+' '+part3+' '+part4
    if k!='минус ' and part2=='ноль':
        return part1+' '+part3+' '+part4
    if k!='минус ' and part2!='ноль':
        return part1+' '+part2+' '+part3+' '+part4
    if k!='минус ' and part4!='ноль':
        return part1+' '+part2+' '+part3
    if k=='минус ' and part4=='ноль':
        return k+part1+' '+part3
    if k=='минус ' and part4!='ноль':
        return k+part1+' '+part2+' '+part3
    if k!='минус ' and part4=='ноль':
        return part1+' '+part3
    if k!='минус ' and part4!='ноль':
        return part1+' '+part2+' '+part3
    
    return ls,itog
print(f())

        


    
