def roman(s):
        s=s.upper()
        num=0
        i=0
        while(i<len(s)): 
            if s[i]=='I':
                if(i+1<len(s) and s[i+1]=='V'):
                    num=num+4
                    i=i+1
                elif(i+1<len(s) and s[i+1]=='X'):
                    num=num+9
                    i=i+1
                else:
                    num=num+1
            elif s[i]=='V':
                num=num+5
            elif s[i]=='X':
                if(i+1<len(s) and s[i+1]=='L'):
                    num=num+40
                    i=i+1
                elif(i+1<len(s) and s[i+1]=='C'):
                    num=num+90
                    i=i+1
                else:
                    num=num+10
            elif s[i]=='L':
                num=num+50
                print("Number in condition of L: ",num)
            elif s[i]=='C':
                if(i+1<len(s) and s[i+1]=='D'):
                    num=num+400
                    i=i+1
                elif(i+1<len(s) and s[i+1]=='M'):
                    num=num+900
                    i=i+1
                else:
                    num=num+100
            elif s[i]=='D':
                num=num+500
            elif s[i]=='M':
                num=num+1000
            i=i+1
        return num


a=input("Enter any number")
print(roman(a))