import time
start = time.clock()

t=5             #dlugosc kroku
b=0.1           #wspolczynnik korygujacy
s=0.001         #dokladnosc obliczen
d=1              #kierunek

x1=-8           # punkty poczatkowe
x2=-89          

x1p=x1
x2p=x2

def funkcja(x1,x2):
    global y
    y=(2*(x1-25.4)**2)+(4*(x2-7.5)**4)
    return y

def funkcjaX1add():
    global x1
    x1=x1+t*d
    return x1

def funkcjaX2add():
    global x2
    x2=x2+t*d
    return x2

def funkcjaX1sub():
    global x1
    x1=x1-t*d
    return x1

def funkcjaX2sub():
    global x2
    x2=x2-t*d
    return x2

while t>=s:
    #print(x1,x2)
    
    q1=funkcja(x1, x2)                  # poczatkowa
    funkcjaX1add()
    q2=funkcja(x1, x2)                   # po dodaniu do x1                       
    if q2<q1:
        print("X1 +",x1)
        x1min=True
        funkcjaX2add()                   # dodajemy do x2
        q3=funkcja(x1,x2)                # wartosc funkcji dla x1 i x2+
        if q2<q3:                         # jezeli funkcja x1,x2+ jest wieksza od poczatkowej
            funkcjaX2sub()
            funkcjaX2sub()
            q4=funkcja(x1,x2)
            if q2<q4:                    # jezeli po odjeciu funkcja jest wieksza to
                funkcjaX2add()
                print("X2 MIN",x2)
                x2min=False
            elif q4<q2:
                print("X2 - o",x2)
                x2min=True               
        elif q3<q2:
            print("X2 + o",x2)
            x2min=True
    elif q1<q2:                         # jezeli po dodaniu jest wieksza to rob to
        funkcjaX1sub()
        funkcjaX1sub()
        q3=funkcja(x1,x2)
        if q3<q1:
            print("X1 -",x1)
            x1min=True
            funkcjaX2add()               # dodajemy do x2
            q4=funkcja(x1,x2)            # wartosc funkcji dla x1 i x2+
            if q3<q4:                    # jezeli funkcja x1,x2+ jest wieksza od poczatkowej
                funkcjaX2sub()
                funkcjaX2sub()
                q5=funkcja(x1,x2)
                if q3<q5:                # jezeli po odjeciu funkcja jest wieksza to
                    funkcjaX2add()
                    print("X2 MIN",x2)
                    
                    x2min=False
                elif q5<q3:
                    print("X2 - o",x2)
                    x2min=True                 
            elif q4<q3:
                print("X2 + o",x2)
                x2min=True 

        elif q1<q3:
            funkcjaX1add()
            q3=funkcja(x1,x2)
            print("X1 MIN",x1)
            
            x1min=False
            funkcjaX2add()               # dodajemy do x2
            q4=funkcja(x1,x2)            # wartosc funkcji dla x1 i x2+
            if q3<q4:                    # jezeli funkcja x1,x2+ jest wieksza od poczatkowej
                funkcjaX2sub()
                funkcjaX2sub()
                q5=funkcja(x1,x2)
                if q3<q5:                # jezeli po odjeciu funkcja jest wieksza to
                    funkcjaX2add()
                    print("X2 MIN",x2)                    
                    x2min=False
                elif q5<q3:
                    print("X2 - o",x2)
                    x2min=True                 
            elif q4<q3:
                print("X2 + o",x2)
                x2min=True                              
    else:
        break
       
    if (x1min and x2min)==True:
        
        x1p=(2*x1)-x1p
        x22=(2*x2)-x2p

        #print("X1p i X2p zmienione")
        
    elif x1min==True and x2min==False :
        x1p=(2*x1)-x1p

        #print("X1p Zmienione")
                    
    elif x1min==False and x2min==True :
        x2p=(2*x2)-x2p
        #print("X2p zmienione")
        
    elif t>s and (x1min and x2min)==False :
        t=t*b
        print("zmiejszam T",t)
        x1min=True
        x2min=True       
    else:
        print("Blad")
        break
    
q1=funkcja(x1, x2)
print("Znaleziono minimum funkcji ktorej wartosc wynosi",q1," w punktach x1=",x1," oraz x2=",x2)
end= time.clock()
total= end-start
print("Czas wykonywania",total)
wcisnij=input("Wcisnij klawisz")
