#Austin O'Quinn
#23Nov2018
def Integration(func):
    '''I should add the ability to have more than one term by having the main split the function at pluses and minuses or something similar, This will be anoying'''
    
    #Helps prevent errors in range
    func=' '+func+' '

    #reusable counter and string initialization
    n=''
    d=''
    i=0
    c=0

    #puts coefficient into n variable
    while func[i]!='x':
        n=n+func[i]
        c=c+1
        i=i+1

    #adds 2 to compensate for possible x^
    i=2

    #only exicutes if i is in range of given string
    if i+c<len(func):

        #puts exponent into d variable
        while func[i+c]!=' ':
            d=d+func[i+c]
            i=i+1

    #error handling 
    if n!=' ' and n!=' -':
        n=float(n)
    elif n==' -':
        n=-1
    else:
        n=1
    if d!='':   #why is this not a space
        d=float(d)
    else:
        d=1
    d=k
    d=d+1
    print(str(n)+'/'+str(d),'x^',d)
    n=g
    n=n/d
    return n,d,g,k

from graphics import *    
def main():
    
    func=input('Enter simple polynomial function:')
    graf=input('Would you like to graph the output(yes or no)?:')
    n,d,g,k=Integration(func)
    if graf!='no' and graf!='No':
        Win=GraphWin('original and integral',500,500)
        Win.setCoords(-10,-10,10,10)
       
        
        
        
        
        
        
        
'''consider putting lines from 0 to the height of the graph to simulate shadding'''    
main()
    
