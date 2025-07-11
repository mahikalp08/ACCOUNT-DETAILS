import pickle as p
a=open("acc.dat","wb")
n=int(input("No. of entries:"))
for i in range(n):
    I=int(input("ID:"))
    N=input("Name:")
    P=int(input("Phone no.:"))
    B=float(input("Bank Balance:"))
    p.dump([I,N,P,B],a)
a.close()
def read():
    a=open("acc.dat","rb")
    try:
        while True:
            b=p.load(a)
            print(b)
    except EOFError:
        a.close()
def append():
    a=open("acc.dat","ab")
    n=int(input("No. of entries:"))
    for i in range(n):
        I=int(input("ID:"))
        N=input("Name:")
        P=int(input("Phone no.:"))
        B=float(input("Bank Balance:"))
        p.dump([I,N,P,B],a)
    a.close()
    read()
def update():
    a=open("acc.dat","rb")
    l=[]
    try:
        while True:
            b=p.load(a)
            l.append(b)
    except EOFError:
        a.close()
    a=open("acc.dat","wb")
    p.dump(l,a)
    a.close()
    a=open("acc.dat","rb+")
    b=p.load(a)
    I=int(input("ID to be updated:"))
    B=float(input("Updated Balance:"))
    for i in b:
        if(i[0]==I):
            i[3]=B
    a.seek(0)
    for i in b:
        p.dump(i,a)
    a.seek(0)
    read()
    a.close()
def search():
    a=open("acc.dat","rb")
    I=int(input("ID to be searched:"))
    s=""
    try:
        while True:
            b=p.load(a)
            if(b[0]==I):
                s=b
                print(b)
                break
    except EOFError:
        a.close()
    if(s==""):
        print("ID not found")
import os
def delete():
    a=open("acc.dat","rb")
    b=open("newacc.dat","wb")
    I=int(input("ID to be deleted:"))
    try:
        while True:
           c=p.load(a)
           if(I!=c[0]):
               p.dump(c,b)
    except EOFError:
        a.close()
        b.close()
    os.remove("acc.dat")
    os.rename("newacc.dat","acc.dat")
    read()
print()
print("""1. Read
2. Append
3. Update
4. Search
5.Delete""")
while True:
    c=input("Choice:")
    if(c=="1"):
        read()
    elif(c=="2"):
        append()
    elif(c=="3"):
        update()
    elif(c=="4"):
        search()
    elif(c=="5"):
        delete()
    elif(c=="quit"):
        break
