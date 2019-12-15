input_string=input("Enter the String in format of  name:number")
list_input=[]
final_string=''
list_input=input_string.split(',')

for i in list_input:
    temp=i.split(':')
    name=temp[0]
    number=temp[1]
    length=len(name)
    max=0

    for digit in number:
        if(int(digit)<=length):
            if max<int(digit):
                max=int(digit)
    if max==0:
        final_string+='X'  
    else:
        final_string+=name[max-1] 
print(final_string)              

    