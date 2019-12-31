import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from datetime import datetime
import math
master=Tk()
master.geometry("1200x700")
master.title("FoodRestro.")

master.config(background='lightsteelBlue3')

Label(master,text="FoodRestro",font=("arial",25,"bold"),fg='dodgerBlue4',background='lightsteelBlue3').place(x=500,y=10)
##username and phno
res = {
        "burger" : [0, 0 ],
        "cake":[0,0],
        "pizza":[0,0],
        "thali":[0,0],
        "cookie":[0,0],
        "icecream":[0,0],
        "colddrink":[0,0],
        "coffee":[0,0],
        "chai":[0,0],
        "water":[0,0]
    }
amt = {
        "burger" : 65,
        "cake":300,
        "pizza":300,
        "thali":150,
        "cookie":80,
        "icecream":100,
        "colddrink":50,
        "coffee":60,
        "chai":30,
        "water":10
    }
def check1():
    name=enteru.get()
    ph=enterph.get()
    tm=entertm.get()
    
    if name.isalpha() and len(ph)==10:
        connection=pymysql.connect(host='localhost', user='root', password='', db='foodrestro')
        cursor=connection.cursor()
        try:
            sql="INSERT INTO foodrest(uname,mobileno,totalamt)VALUES( '%s','%s','%s')" %(name,ph,tm)
            
            res1=cursor.execute(sql)
            
            connection.commit()
        finally:
            connection.close()
        
        
    else:
        messagebox.showerror("error","name should not contain any numbers and number should be 10 digits long.")
def fooditem():
    connection=pymysql.connect(host='localhost', user='root', password='', db='foodrestro')
    cursor=connection.cursor()
    for i in res:
        print(i)
        if res[i][0]!=0 and res[i][1]!=0:
            sql="INSERT INTO fooditem (uid,foodname,price,quantity) VALUES((select id from foodrest ORDER BY id DESC LIMIT 1),'%s','%s','%s')"% (i,res[i][1],res[i][0])
            cursor.execute(sql)
            connection.commit()
        
    connection.close()
def show():
    connection=pymysql.connect(host='localhost', user='root', password='', db='foodrestro')
    cursor=connection.cursor()
   
    try:
        sql="select * from foodrest ORDER BY id DESC LIMIT 1"
       
        #SELECT fields FROM table ORDER BY id DESC LIMIT 1;
        print(sql)
        cursor.execute(sql)
        
        res=cursor.fetchone()
        
        #u.insert(0,res[0])
        #ph1.insert(0,res[1])
        #entertm.insert(0,res[2])
        connection.commit()
        return res
    finally:
        connection.close()
        #user.delete(0,END)
        #ph1.delete(0,END)
        #entertm1.delete(0,END)

def show1():
    connection=pymysql.connect(host='localhost', user='root', password='', db='foodrestro')
    cursor1=connection.cursor()
    try:
        res=show()
        sql1="select * from fooditem where uid= '%s'"%(res[0])
        cursor1.execute(sql1)
        res1=cursor1.fetchall()
        connection.commit()
        return res1
    finally:
        connection.close()
    #SELECT LAST (CUSTOMER_NAME) AS LAST_CUSTOMER FROM CUSTOMERS;  
################################
#####Bill#######################
def create_window():
    check1()
    fooditem()
    global window
    window=Toplevel(master)
    window.geometry("550x500")
    window.config(background='lightsteelBlue3')
    Label(window,text="FoodRestro",font=("arial",16,"bold"),fg='dodgerBlue4',background='lightsteelBlue3').place(x=130,y=10)
    now = datetime.now()
    date = now.strftime("%a,%b %d ,%Y ")
    time=now.strftime("%H:%M:%S ")
    g="date:",date,"time:",time
    date1=Label(window,text="",font=("arial",11),background='lightsteelBlue3')
    date1.config(text=g)
    date1.place(x=80,y=40)

    
    result=show() #call function show
    result1=show1()
    #items()
    print(result1)
    ul=Label(window,text="Username:",font=("arial",11),background='lightsteelBlue3')
    ul.place(x=20,y=80)
    user=Entry(window,background='lightsteelBlue1')
    user.insert(0,result[1])
    user.place(x=120,y=80)
    ph=Label(window,text="Phonno:",font=("arial",11),background='lightsteelBlue3')
    ph.place(x=20,y=120)
    ph1=Entry(window,background='lightsteelBlue1')
    ph1.insert(0,result[2])
    ph1.place(x=120,y=120)
    tm=Label(window,text="Total Amount",font=("arial",11),background='lightsteelBlue3')
    tm.place(x=20,y=160)
    entertm1=Entry(window,background='lightsteelBlue1')
    entertm1.insert(0,result[3])
    entertm1.place(x=120,y=160)
    labeltext=Label(window,text="uid foodname price quant",font=("arial",10),background='lightsteelBlue3')
    labeltext.place(x=50,y=180)
    text1=Text(window,height=10 ,width=35,font=("arial",12),background='lightsteelBlue1')
    for i in result1:
        text1.insert(INSERT,i)
        text1.insert(INSERT,"\n")
    text1.place(x=50,y=200)
    ok=Button(window,text="pay",font=("arial",11),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=clear)

    ok.config(height=1,width=11)
    ok.place(x=60,y=400)
def clear():
    
    window.destroy()
    for i in res:
        res[i][0]=0
        res[i][1]=0
    enteru.delete(0,END)
    enterph.delete(0,END)
    entertm.delete(0,END)
    enter1.delete(0,END)
    enter2.delete(0,END)
    enter4.delete(0,END)
    enter5.delete(0,END)
    enter6.delete(0,END)
    enter7.delete(0,END)
    enter8.delete(0,END)
    enter10.delete(0,END)
    enter11.delete(0,END)
    enter12.delete(0,END)
    enter13.delete(0,END)
    enter14.delete(0,END)
    enter15.delete(0,END)
    enter16.delete(0,END)
    enterc1.delete(0,END)
    enterc2.delete(0,END)
    enter17.delete(0,END)
    enter18.delete(0,END)
    enter19.delete(0,END)
    enter20.delete(0,END)
button11=Button(master, text="Bill",font=("arial",15),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=create_window)
button11.config(height=1,width=11)
button11.place(x=400, y=620)
uname=Label(master,text="Username:",font=("arial",15),background='lightsteelBlue3')
uname.place(x=25,y=50)
enteru=Entry(master,background='lightsteelBlue1')
#enteru.insert(0,"Enter user name")
#enteru.bind('<Return>',getuserrval)
enteru.place(x=125,y=55)
phno=Label(master,text="Phoneno:",font=("arial",15),background='lightsteelBlue3')
phno.place(x=260,y=50)
enterph=Entry(master,background='lightsteelBlue1')
#enterph.bind('<Return>',getphnoval)
enterph.place(x=350,y=55)


def totalamt():
    total = sum( [ i[1] for i in res.values()])
    #print(total)
    entertm.delete(0,END)
    entertm.insert(0,total)
        
#by manually typing value
def getburgerval(event):
    quant=enter1.get()   #fetch value from enter1
    f="burger"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter2.delete(0,END)
    enter2.insert(0,total) #show amount in amount label entry
    totalamt()
def getcakesval(event):
    quant=enter4.get()
    f="cake"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter5.delete(0,END)
    enter5.insert(0,total)  #showing cake amt
def getpizzaval(event):
    quant=enter6.get()
    f="pizza"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter7.delete(0,END)
    enter7.insert(0,total)   #showing pizza amt
    totalamt()
def getthalival(event):
    quant=enter8.get()
    f="thali"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter10.delete(0,END)
    enter10.insert(0,total)
    totalamt()
def getcookiesval(event):
    quant=enter11.get()
    f="cookie"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter12.delete(0,END)
    enter12.insert(0,total)
    totalamt()
def geticecreamval(event):
    quant=enter13.get()
    f="icecream"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter14.delete(0,END)
    enter14.insert(0,total)
    totalamt()
def getcolddrinkval(event):
    quant=enter15.get()
    f="colddrink"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter16.delete(0,END)
    enter16.insert(0,total)
    totalamt()
def getcoffeeval(event):
    quant=enterc1.get()
    f="coffee"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enterc2.delete(0,END)
    enterc2.insert(0,total)
    totalamt()
def getchaival(event):
    quant=enter17.get()
    f="chai"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter18.delete(0,END)
    enter18.insert(0,total)
    totalamt()
def getwaterval(event):
    quant=enter19.get()     
    f="water"
    res[f][0]=int(quant)
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    enter20.delete(0,END)
    enter20.insert(0,total)
    totalamt()
##################################
#####total amount###########3####

label21=Label(master,text="Total Amount",font=("arial",15),background='lightsteelBlue3')
label21.place(x=400,y=550)
entertm=Entry(master,background='lightsteelBlue1',font=("arial",15,"bold"))

entertm.place(x=400,y=580)

###entery widgets
#burger
enter1=Entry(master,background='lightsteelBlue1')
enter1.insert(0,'0')
enter1.bind('<Return>',getburgerval)
enter1.place(x=125,y=120)
enter2=Entry(master,background='lightsteelBlue1')
enter2.insert(0,'0')
enter2.place(x=125,y=164)
#cakes
enter4=Entry(master,background='lightsteelBlue1')
enter4.bind('<Return>',getcakesval)
enter4.place(x=125,y=220)
enter5=Entry(master,background='lightsteelBlue1')
enter5.place(x=125,y=264)
#pizza
enter6=Entry(master,background='lightsteelBlue1')
enter6.bind('<Return>',getpizzaval)
enter6.place(x=125,y=320)
enter7=Entry(master,background='lightsteelBlue1')
enter7.place(x=125,y=364)
#thali
enter8=Entry(master,background='lightsteelBlue1')
enter8.bind('<Return>',getthalival)
enter8.place(x=125,y=420)
enter10=Entry(master,background='lightsteelBlue1')
enter10.place(x=125,y=464)
#cookies
enter11=Entry(master,background='lightsteelBlue1')
enter11.bind('<Return>',getcookiesval)
enter11.place(x=125,y=520)
enter12=Entry(master,background='lightsteelBlue1')
enter12.place(x=125,y=564)
#ice cream
enter13=Entry(master,background='lightsteelBlue1')
enter13.bind('<Return>',geticecreamval)
enter13.place(x=125,y=620)
enter14=Entry(master,background='lightsteelBlue1')
enter14.place(x=125,y=664)
#colddrink
enter15=Entry(master,background='lightsteelBlue1')
enter15.bind('<Return>',getcolddrinkval)
enter15.place(x=430,y=120)
enter16=Entry(master,background='lightsteelBlue1')
enter16.place(x=430,y=164)
#coffee
enterc1=Entry(master,background='lightsteelBlue1')
enterc1.bind('<Return>',getcoffeeval)
enterc1.place(x=430,y=220)
enterc2=Entry(master,background='lightsteelBlue1')
enterc2.place(x=430,y=264)
#chai
enter17=Entry(master,background='lightsteelBlue1')
enter17.bind('<Return>',getchaival)
enter17.place(x=430,y=320)
enter18=Entry(master,background='lightsteelBlue1')
enter18.place(x=430,y=364)
#water
enter19=Entry(master,background='lightsteelBlue1')
enter19.bind('<Return>',getwaterval)
enter19.place(x=430,y=420)
enter20=Entry(master,background='lightsteelBlue1')
enter20.place(x=430,y=464)
#photo = PhotoImage(file = r"burger.png") 
# here, image option is used to 
# set image on button


##########for adding items to cart#########
def food1( f ):
    res[f][0]+=1
    res[f][1] = res[f][0]* amt[f]
    total=res[f][1]
    quant=res[f][0]
    return quant,total

def burger():
    b=food1("burger")
    #print(type(b))
    #print(b)
    enter1.delete(0,END)
    enter1.insert(0,b[0])
    enter2.delete(0,END)
    enter2.insert(0,b[1])
    totalamt()
def cakes():
    c=food1("cake")
    #print(c)
    enter4.delete(0,END)
    enter4.insert(0,c[0])
    enter5.delete(0,END)
    enter5.insert(0,c[1])
    totalamt()
def pizza():
    p=food1("pizza")
    #print(p)
    enter6.delete(0,END)
    enter6.insert(0,p[0])
    enter7.delete(0,END)
    enter7.insert(0,p[1])
    totalamt()
def thali():
    t=food1("thali")
    #print(t)
    enter8.delete(0,END)
    enter8.insert(0,t[0])
    enter10.delete(0,END)
    enter10.insert(0,t[1])
    totalamt()
def cookies():
    c=food1("cookie")
    #print(c)
    enter11.delete(0,END)
    enter11.insert(0,c[0])
    enter12.delete(0,END)
    enter12.insert(0,c[1])
    totalamt()
def icecream():
    i=food1("icecream")
    #print(i)
    enter13.delete(0,END)
    enter13.insert(0,i[0])
    enter14.delete(0,END)
    enter14.insert(0,i[1])
    totalamt()
def colddrink():
    cd=food1("colddrink")
    #print(cd)
    enter15.delete(0,END)
    enter15.insert(0,cd[0])
    enter16.delete(0,END)
    enter16.insert(0,cd[1])
    totalamt()
def coffee():
    cof=food1("coffee")
    #print(cof)
    enterc1.delete(0,END)
    enterc1.insert(0,cof[0])
    enterc2.delete(0,END)
    enterc2.insert(0,cof[1])
    totalamt()
def chai():
    ch=food1("chai")
    #print(ch)
    enter17.delete(0,END)
    enter17.insert(0,ch[0])
    enter18.delete(0,END)
    enter18.insert(0,ch[1])
    totalamt()
def water():
    w=food1("water")
    #print(w)
    enter19.delete(0,END)
    enter19.insert(0,w[0])
    enter20.delete(0,END)
    enter20.insert(0,w[1])
    totalamt()
########## for removing items from cart #########
def foodremove(f):
    if res[f][0] <= 0 and res[f][1]<= 0:
        return res[f][0],res[f][1]
    res[f][0] -=1
    res[f][1]=res[f][0]*amt[f]
    total=res[f][1]
    quant=res[f][0]
    return quant,total
def rembur():
    rb=foodremove("burger")
    #print(rb)
    enter1.delete(0,END)
    enter1.insert(0,rb[0])
    enter2.delete(0,END)
    enter2.insert(0,rb[1])
    totalamt()
def remcake():
    rc=foodremove("cake")
    #print(rc)
    enter4.delete(0,END)
    enter4.insert(0,rc[0])
    enter5.delete(0,END)
    enter5.insert(0,rc[1])
    totalamt()
def rempizza():
    rp=foodremove("pizza")
    #print(rp)
    enter6.delete(0,END)
    enter6.insert(0,rp[0])
    enter7.delete(0,END)
    enter7.insert(0,rp[1])
    totalamt()
def remthali():
    rt=foodremove("thali")
    #print(rt)
    enter8.delete(0,END)
    enter8.insert(0,rt[0])
    enter10.delete(0,END)
    enter10.insert(0,rt[1])
    totalamt()
def remcookies():
    rc=foodremove("cookie")
    #print(rc)
    enter11.delete(0,END)
    enter11.insert(0,rc[0])
    enter12.delete(0,END)
    enter12.insert(0,rc[1])
    totalamt()
def remicecream():
    ri=foodremove("icecream")
    #print(ri)
    enter13.delete(0,END)
    enter13.insert(0,ri[0])
    enter14.delete(0,END)
    enter14.insert(0,ri[1])
    totalamt()
def remcolddrink():
    rc=foodremove("colddrink")
    #print(rc)
    enter15.delete(0,END)
    enter15.insert(0,rc[0])
    enter16.delete(0,END)
    enter16.insert(0,rc[1])
    totalamt()
def remcoffee():
    rc=foodremove("coffee")
    #print(rc)
    enterc1.delete(0,END)
    enterc1.insert(0,rc[0])
    enterc2.delete(0,END)
    enterc2.insert(0,rc[1])
    totalamt()
def remchai():
    rc=foodremove("chai")
    #print(rc)
    enter17.delete(0,END)
    enter17.insert(0,rc[0])
    enter18.delete(0,END)
    enter18.insert(0,rc[1])
    totalamt()
def remwater():
    rw=foodremove("water")
    #print(rw)
    enter19.delete(0,END)
    enter19.insert(0,rw[0])
    enter20.delete(0,END)
    enter20.insert(0,rw[1])
    totalamt()


#burgers
width = 80
height = 80
img = Image.open("burger.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
but1 = Button(master,image=photoImg,height=80,  width=80 , bg='lightsteelBlue3',command=burger)
but1.place(x=25,y=100)
label1=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label1.place(x=125,y=96)
label2=Label(master,text="Amount:65",font=("arial",11),background='lightsteelBlue3')
label2.place(x=125,y=140)
button50=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=rembur)
button50.config(height=1,width=6)
button50.place(x=255, y=120)
#cakes
img1 = Image.open("cake.png")
img1 = img1.resize((width,height), Image.ANTIALIAS)
photoImg1 =  ImageTk.PhotoImage(img1)
but2 = Button(master,image=photoImg1,height=80,  width=80 , bg='lightsteelBlue3',command=cakes)
but2.place(x=25,y=200)
label4=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label4.place(x=125,y=196)
label5=Label(master,text="Amount:300",font=("arial",11),background='lightsteelBlue3')
label5.place(x=125,y=240)
button51=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remcake)
button51.config(height=1,width=6)
button51.place(x=255, y=220)
# pizza
img2 = Image.open("pizza.png")
img2 = img2.resize((width,height), Image.ANTIALIAS)
photoImg2 =  ImageTk.PhotoImage(img2)
but3 = Button(master,image=photoImg2, height=80,  width=80 , bg='lightsteelBlue3',command=pizza)
but3.place(x=25,y=300)
label6=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label6.place(x=125,y=296)
label7=Label(master,text="Amount:300",font=("arial",11),background='lightsteelBlue3')
label7.place(x=125,y=340)
button52=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=rempizza)
button52.config(height=1,width=6)
button52.place(x=255, y=320)
#thali
img3 = Image.open("thali1.png")
img3 = img3.resize((width,height), Image.ANTIALIAS)
photoImg3 =  ImageTk.PhotoImage(img3)
but4 = Button(master,image=photoImg3, height=80,  width=80 , bg='lightsteelBlue3',command=thali)
but4.place(x=25,y=400)
label8=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label8.place(x=125,y=396)
label9=Label(master,text="Amount:150",font=("arial",11),background='lightsteelBlue3')
label9.place(x=125,y=440)
button53=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remthali)
button53.config(height=1,width=6)
button53.place(x=255, y=420)
#cookies
img4 = Image.open("cookie.png")
img4 = img4.resize((width,height), Image.ANTIALIAS)
photoImg4 =  ImageTk.PhotoImage(img4)
but5 = Button(master,image=photoImg4, height=80,  width=80 , bg='lightsteelBlue3',command=cookies)
but5.place(x=25,y=500)
label11=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label11.place(x=125,y=496)
label12=Label(master,text="Amount:80",font=("arial",11),background='lightsteelBlue3')
label12.place(x=125,y=540)
button54=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remcookies)
button54.config(height=1,width=6)
button54.place(x=255, y=520)
#ice cream
img5 = Image.open("icecream.png")
img5 = img5.resize((width,height), Image.ANTIALIAS)
photoImg5 =  ImageTk.PhotoImage(img5)
but6 = Button(master,image=photoImg5, height=80,  width=80 , bg='lightsteelBlue3',command=icecream)
but6.place(x=25,y=600)
label13=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label13.place(x=125,y=596)
label14=Label(master,text="Amount:100",font=("arial",11),background='lightsteelBlue3')
label14.place(x=125,y=640)
button55=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remicecream)
button55.config(height=1,width=6)
button55.place(x=255, y=620)
##but=Button(master, text = 'Click Me !', image = photo)
##but.
##but.config(height=50,width=50)

#cold drink
img6 = Image.open("cold drink.png")
img6 = img6.resize((width,height), Image.ANTIALIAS)
photoImg6 =  ImageTk.PhotoImage(img6)
but7 = Button(master,image=photoImg6, height=80,  width=80 , bg='lightsteelBlue3',command=colddrink)
but7.place(x=330,y=100)
label15=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label15.place(x=430,y=96)
label16=Label(master,text="Amount:50",font=("arial",11),background='lightsteelBlue3')
label16.place(x=430,y=140)
button56=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remcolddrink)
button56.config(height=1,width=6)
button56.place(x=560, y=120)
#coffee
img7 = Image.open("coffe.png")
img7 = img7.resize((70,70), Image.ANTIALIAS)
photoImg7 =  ImageTk.PhotoImage(img7)
but8 = Button(master,image=photoImg7, height=80,  width=80 , bg='lightsteelBlue3',command=coffee)
but8.place(x=330,y=200)
label21=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label21.place(x=430,y=196)
label22=Label(master,text="Amount:60",font=("arial",11),background='lightsteelBlue3')
label22.place(x=430,y=240)
button57=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remcoffee)
button57.config(height=1,width=6)
button57.place(x=560, y=220)
#chai
img8 = Image.open("chai.png")
img8 = img8.resize((width,height), Image.ANTIALIAS)
photoImg8 =  ImageTk.PhotoImage(img8)
but9 = Button(master,image=photoImg8, height=80,  width=80 , bg='lightsteelBlue3',command=chai)
but9.place(x=330,y=300)
label17=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label17.place(x=430,y=296)
label18=Label(master,text="Amount:30",font=("arial",11),background='lightsteelBlue3')
label18.place(x=430,y=340)
button58=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remchai)
button58.config(height=1,width=6)
button58.place(x=560, y=320)
# Normal water
img9 = Image.open("water.png")
img9 = img9.resize((100,100), Image.ANTIALIAS)
photoImg9 =  ImageTk.PhotoImage(img9)
but10 = Button(master,image=photoImg9, height=80,  width=80 , bg='lightsteelBlue3',command=water)
but10.place(x=330,y=400)
label19=Label(master,text="Quantity",font=("arial",11),background='lightsteelBlue3')
label19.place(x=430,y=396)
label20=Label(master,text="Amount:10",font=("arial",11),background='lightsteelBlue3')
label20.place(x=430,y=440)
button58=Button(master, text="remove",font=("arial",12,"bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=remwater)
button58.config(height=1,width=6)
button58.place(x=560, y=420)






## calculator
def getandreplace():
    expression = enter21.get()
    newtext=expression.replace('/','/') 
    newtext=newtext.replace('x','*') 
    return newtext
  
def equals(): 
    newtext=getandreplace()
    try: 
            # evaluate the expression using the eval function 
        value= eval(newtext)  
    except SyntaxError or NameError: 
        enter21.delete(0,END) 
        enter21.insert(0,'Invalid Input!') 
    else: 
        enter21.delete(0,END) 
        enter21.insert(0,value) 
def clearall():
    enter21.delete(0,END) 
  
def clear1(): 
    txt=enter21.get()[:-1]
    enter21.delete(0,END) 
    enter21.insert(0,txt) 
  
def action(argi):
    enter21.insert(END,argi)

label21=Label(master,text="Calculator",font=("arial",20),background='lightsteelBlue3')
label21.place(x=900,y=190)
enter21=Entry(master,background='lightsteelBlue1')
enter21.place(x=900,y=225)

button12=Button(master, text="c",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=clearall)
button12.config(height=1,width=2)
button12.place(x=900, y=250)
button12=Button(master, text="Ac",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=clear1)
button12.config(height=1,width=2)
button12.place(x=940, y=250)
button12=Button(master, text="%",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('%'))
button12.config(height=1,width=2)
button12.place(x=980, y=250)
button12=Button(master, text="/",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('/'))
button12.config(height=1,width=2)
button12.place(x=1020, y=250)
button12=Button(master, text="7",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(7))
button12.config(height=1,width=2)
button12.place(x=900, y=300)

button12=Button(master, text="8",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(8))
button12.config(height=1,width=2)
button12.place(x=940, y=300)

button12=Button(master, text="9",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(9))
button12.config(height=1,width=2)
button12.place(x=980, y=300)
button12=Button(master, text="x",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('x'))
button12.config(height=1,width=2)
button12.place(x=1020, y=300)
button12=Button(master, text="4",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(4))
button12.config(height=1,width=2)
button12.place(x=900, y=350)
button12=Button(master, text="5",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(5))
button12.config(height=1,width=2)
button12.place(x=940, y=350)
button12=Button(master, text="6",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(6))
button12.config(height=1,width=2)
button12.place(x=980, y=350)
button12=Button(master, text="-",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('-'))
button12.config(height=1,width=2)
button12.place(x=1020, y=350)

button12=Button(master, text="1",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(1))
button12.config(height=1,width=2)
button12.place(x=900, y=400)
button12=Button(master, text="2",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(2))
button12.config(height=1,width=2)
button12.place(x=940, y=400)
button12=Button(master, text="3",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(3))
button12.config(height=1,width=2)
button12.place(x=980, y=400)
button12=Button(master, text="+",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('+'))
button12.config(height=1,width=2)
button12.place(x=1020, y=400)
button12=Button(master, text="0",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action(0))
button12.config(height=1,width=2)
button12.place(x=900, y=450)
button12=Button(master, text=".",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=lambda:action('.'))
button12.config(height=1,width=2)
button12.place(x=940, y=450)
button12=Button(master, text="=",font=("arial", 16, "bold"),borderwidth=1,relief='solid',fg="snow2",background='lightsteelBlue4',command=equals)
button12.config(height=1,width=5)
button12.place(x=980, y=450)


mainloop()
