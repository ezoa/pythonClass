text=input("Enter the text")
''' in order to eliminate all space around of this text '''
text=text.strip() 
if len(text)<1 :
    print("input a new text")
else :
    if all(text[i] in "0123456789" for i in range(len(text))) :
        '''in order to compare all element in table with set digit'''
        print("it is an integer")
        '''compare this number if they are not a sign'''
    elif text[0] in "-+" and all(text[i] in "0123456789" for i range (1,len(text))):
        print("it is an integer")
    else :
        print("it is an string"


n=input("write a number")
if n==1:
    print("first day of mnonth")
else:
    print()