from tkinter import *
from random import *

w = Tk()#建立主視窗
w.title("chess")
w.geometry("700x400")
w.config(background="gray")

global round
round=int(2)

button_choice={}
L = sample(range(1,33),32)
C = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],-1],
    [-1,L[8],L[9],L[10],L[11],L[12],L[13],L[14],L[15],-1],
    [-1,L[16],L[17],L[18],L[19],L[20],L[21],L[22],L[23],-1],
    [-1,L[24],L[25],L[26],L[27],L[28],L[29],L[30],L[31],-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
F = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,0,0,0,0,0,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,-1],
    [-1,0,0,0,0,0,0,0,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
    
#1~5  卒 17~21兵
#6    將 22   帥
#7,8  士 23,24
#9,10 象 25,26
#11,12車 27,28
#13,14馬 29,30
#15,16包 31,32

img0= PhotoImage    (file="blankchess.png")
img15= PhotoImage   (file="black_zu.png")
img6= PhotoImage    (file="black_jiang.png")
img78= PhotoImage   (file="black_shi.png")
img910= PhotoImage  (file="black_xiang.png")
img1112= PhotoImage (file="black_che.png")
img1314= PhotoImage (file="black_ma.png")
img1516= PhotoImage (file="black_pao.png")
img1721= PhotoImage (file="red_bing.png")
img22= PhotoImage   (file="red_shuai.png")
img2324= PhotoImage (file="red_shi.png")
img2526= PhotoImage (file="red_xiang.png")
img2728= PhotoImage (file="red_che.png")
img2930= PhotoImage (file="red_ma.png")
img3132= PhotoImage (file="red_pao.png")


def choose(x,y):
    #print(C[y-1][x],C[y][x])
    if C[y][x]>=1 and C[y][x]<=5:
        black_zu(x,y)
        
    elif C[y][x]==6:
        black_jiang(x,y)
        
    elif C[y][x]==7 or C[y][x]==8:
        black_shi(x,y)
        
    elif C[y][x]==9 or C[y][x]==10:
        black_xiang(x, y)
        
    elif C[y][x]==11 or C[y][x]==12:
        black_che(x, y)
        
    elif C[y][x]==13 or C[y][x]==14:
        black_ma(x, y)
        
    elif C[y][x]==15 or C[y][x]==16:
        black_pao(x, y)
        
    elif C[y][x]>=17 and C[y][x]<=21:
        red_bing(x, y)
        
    elif C[y][x]==22:
        red_shuai(x, y)
        
    elif C[y][x]==23 or C[y][x]==24:
        red_shi(x, y)
        
    elif C[y][x]==25 or C[y][x]==26:
        red_xiang(x, y)
        
    elif C[y][x]==27 or C[y][x]==28:
        red_che(x, y)
        
    elif C[y][x]==29 or C[y][x]==30:
        red_ma(x, y)
        
    elif C[y][x]==31 or C[y][x]==32:
        red_pao(x, y)

def clear():
    for i in range (1,33):
        
        if F[(i-1)//8+1][(i-1)%8+1]==1 and not C[(i-1)//8+1][(i-1)%8+1]==0:
            def fun(a=(i-1)%8+1,b=(i-1)//8+1):
                choose(a,b)
            button_choice[i].config(command = fun)
        button_choice[i]["state"] = "normal"
        button_choice[i].config(bg="grey")
    if round==0:
        for i in range (1,33):
            if F[(i-1)//8+1][(i-1)%8+1]==1:
                if C[(i-1)//8+1][(i-1)%8+1]>=1 and C[(i-1)//8+1][(i-1)%8+1]<=16:
                    button_choice[i]["state"] = "disabled"
    elif round==1:
        for i in range (1,33):
            if F[(i-1)//8+1][(i-1)%8+1]==1:
                if C[(i-1)//8+1][(i-1)%8+1]>=17 and C[(i-1)//8+1][(i-1)%8+1]<=32:
                    button_choice[i]["state"] = "disabled"

def goback (x,y):
    button_choice[8*(y-1)+x].config(command=lambda: choose(x,y))
    clear()
    
def none():
    pass
    
def move (x1,y1,x,y):
    C[y][x]=C[y1][x1]
    C[y1][x1]=0
    print(x1,y1,x,y,C[y][x],C[y1][x1],"A")
    button_choice[8*(y1-1)+x1].config(image= "",command=none())
    if C[y][x]>=1 and C[y][x]<=5:
        button_choice[8*(y-1)+x].config(image= img15)

    elif C[y][x]==6:
        button_choice[8*(y-1)+x].config(image= img6)

    elif C[y][x]==7 or C[y][x]==8:
        button_choice[8*(y-1)+x].config(image= img78)

    elif C[y][x]==9 or C[y][x]==10:
        button_choice[8*(y-1)+x].config(image= img910)

    elif C[y][x]==11 or C[y][x]==12:
        button_choice[8*(y-1)+x].config(image= img1112)

    elif C[y][x]==13 or C[y][x]==14:
        button_choice[8*(y-1)+x].config(image= img1314)

    elif C[y][x]==15 or C[y][x]==16:
        button_choice[8*(y-1)+x].config(image= img1516)

    elif C[y][x]>=17 and C[y][x]<=21:
        button_choice[8*(y-1)+x].config(image= img1721)

    elif C[y][x]==22:
        button_choice[8*(y-1)+x].config(image= img22)

    elif C[y][x]==23 or C[y][x]==24:
        button_choice[8*(y-1)+x].config(image= img2324)

    elif C[y][x]==25 or C[y][x]==26:
        button_choice[8*(y-1)+x].config(image= img2526)

    elif C[y][x]==27 or C[y][x]==28:
        button_choice[8*(y-1)+x].config(image= img2728)

    elif C[y][x]==29 or C[y][x]==30:
        button_choice[8*(y-1)+x].config(image= img2930)

    elif C[y][x]==31 or C[y][x]==32:
        button_choice[8*(y-1)+x].config(image= img3132)
    button_choice[8*(y-1)+x].config(command=lambda: choose(x,y))
    global round
    if round==1:
        round=0
    elif round==0:
        round=1
    clear()

def black_zu(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    if (C[y+1][x]>=17 and C[y+1][x]<=22 and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (C[y-1][x]>=17 and C[y-1][x]<=22 and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (C[y][x+1]>=17 and C[y][x+1]<=22 and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (C[y][x-1]>=17 and C[y][x-1]<=22 and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def black_jiang(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    
    if (C[y+1][x]>=22 and C[y+1][x]<=32 and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
        
    if (C[y-1][x]>=22 and C[y-1][x]<=32 and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
        
    if (C[y][x+1]>=22 and C[y][x+1]<=32 and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
        
    if (C[y][x-1]>=22 and C[y][x-1]<=32 and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"      
def black_shi(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    if (((C[y+1][x]>=23 and C[y+1][x]<=32) or (C[y+1][x]>=17 and C[y+1][x]<=21)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
        
    if (((C[y-1][x]>=23 and C[y-1][x]<=32) or (C[y-1][x]>=17 and C[y-1][x]<=21)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
        
    if (((C[y][x+1]>=23 and C[y][x+1]<=32) or (C[y][x+1]>=17 and C[y][x+1]<=21)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
        
    if (((C[y][x-1]>=23 and C[y][x-1]<=32) or (C[y][x-1]>=17 and C[y][x-1]<=21)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def black_xiang(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    if (((C[y+1][x]>=25 and C[y+1][x]<=32) or (C[y+1][x]>=17 and C[y+1][x]<=21)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=25 and C[y-1][x]<=32) or (C[y-1][x]>=17 and C[y-1][x]<=21)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=25 and C[y][x+1]<=32) or (C[y][x+1]>=17 and C[y][x+1]<=21)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=25 and C[y][x-1]<=32) or (C[y][x-1]>=17 and C[y][x-1]<=21)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def black_che(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    option1=[x+1,x-1]
    option2=[y+1,y-1]
    if (((C[y+1][x]>=27 and C[y+1][x]<=32) or (C[y+1][x]>=17 and C[y+1][x]<=21)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=27 and C[y-1][x]<=32) or (C[y-1][x]>=17 and C[y-1][x]<=21)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=27 and C[y][x+1]<=32) or (C[y][x+1]>=17 and C[y][x+1]<=21)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=27 and C[y][x-1]<=32) or (C[y][x-1]>=17 and C[y][x-1]<=21)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def black_ma(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    option1=[x+1,x-1]
    option2=[y+1,y-1]
    if (((C[y+1][x]>=29 and C[y+1][x]<=32) or (C[y+1][x]>=17 and C[y+1][x]<=21)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=29 and C[y-1][x]<=32) or (C[y-1][x]>=17 and C[y-1][x]<=21)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=29 and C[y][x+1]<=32) or (C[y][x+1]>=17 and C[y][x+1]<=21)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=29 and C[y][x-1]<=32) or (C[y][x-1]>=17 and C[y][x-1]<=21)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def black_pao(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    
    if C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
        
    for i in range (1,10):
        if (C[y+i][x]==-1):
            jumpd=0
            break
        if (C[y+i][x]>=1 and C[y+i][x]<=32):
            jumpd=i
            break
    for i in range (1,10):
        if C[y+jumpd+i][x]==-1 or (C[y+jumpd+i][x]>=1 and C[y+jumpd+i][x]<=16):
            break
        if ((C[y+jumpd+i][x]>=17 and C[y+jumpd+i][x]<=32) and F[y+jumpd+i][x]==1):
            def f(a=x,b=y,c=x,d=y+jumpd+i):
                move(a,b,c,d)
            button_choice[8*(y+jumpd+i-1)+x].config(bg="green",command = f)
            button_choice[8*(y+jumpd+i-1)+x]["state"] = "normal"
            print(x,y,x,y+i+jumpd,jumpd,i)    
            break
            
    for i in range (1,10):
        if C[y-i][x]==-1:
            jumpu=0
            break
        if (C[y-i][x]>=1 and C[y-i][x]<=32):
            jumpu=i
            break
    for i in range (1,10):
        if C[y-jumpu-i][x]==-1 or (C[y-jumpu-i][x]>=1 and C[y-jumpu-i][x]<=16):
            break
        if ((C[y-jumpu-i][x]>=17 and C[y-jumpu-i][x]<=32) and F[y-jumpu-i][x]==1):
            def f(a=x,b=y,c=x,d=y-jumpu-i):
                move(a,b,c,d)
            button_choice[8*(y-jumpu-i-1)+x].config(bg="green",command = f)
            button_choice[8*(y-jumpu-i-1)+x]["state"] = "normal" 
            print (x,y,x,y-i-jumpu,jumpu,i)  
            break
            
    for i in range (1,10):
        if (C[y][x+i]==-1):
            jumpr=0
            break
        if (C[y][x+i]>=1 and C[y][x+i]<=32):
            jumpr=i
            break
    for i in range (1,10):
        if (C[y][x+jumpr+i]==-1) or (C[y][x+jumpr+i]>=1 and C[y][x+jumpr+i]<=16):
            break
        if ((C[y][x+jumpr+i]>=17 and C[y][x+jumpr+i]<=32) and F[y][x+jumpr+i]==1):
            def f(a=x,b=y,c=x+jumpr+i,d=y):
                move(a,b,c,d)
            button_choice[8*(y-1)+x+jumpr+i]["state"] = "normal"
            button_choice[8*(y-1)+x+jumpr+i].config(bg="green",command =f)
            print(x,y,x+jumpr+i,y,jumpr,i)
            break
            
    for i in range (1,10):
        if (C[y][x-i]==-1):
            jumpl=0
            break
        if (C[y][x-i]>=1 and C[y][x-i]<=32):
            jumpl=i
            break
    for i in range (1,10):
        if C[y][x-jumpl-i]==-1 or (C[y][x-jumpl-i]>=1 and C[y][x-jumpl-i]<=16):
            break
        if ((C[y][x-jumpl-i]>=17 and C[y][x-jumpl-i]<=32) and F[y][x-jumpl-i]==1):
            def f(a=x,b=y,c=x-jumpl-i,d=y):
                move(a,b,c,d)
            button_choice[8*(y-1)+x-jumpl-i].config(bg="green",command =f)
            button_choice[8*(y-1)+x-jumpl-i]["state"] = "normal"  
            print(x,y,x-jumpl-i,y,jumpl,i)
            break

def red_bing(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    option1=[x+1,x-1]
    option2=[y+1,y-1]
    if (((C[y+1][x]==6) or (C[y+1][x]>=1 and C[y+1][x]<=5)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]==6) or (C[y-1][x]>=1 and C[y-1][x]<=5)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]==6) or (C[y][x+1]>=1 and C[y][x+1]<=5)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]==6) or (C[y][x-1]>=1 and C[y][x-1]<=5)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_shuai(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    
    if (C[y+1][x]>=6 and C[y+1][x]<=16 and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
        
    if (C[y-1][x]>=6 and C[y-1][x]<=16 and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
        
    if (C[y][x+1]>=6 and C[y][x+1]<=16 and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
        
    if (C[y][x-1]>=6 and C[y][x-1]<=16 and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_shi(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    if (((C[y+1][x]>=7 and C[y+1][x]<=16) or (C[y+1][x]>=1 and C[y+1][x]<=5)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=7 and C[y-1][x]<=16) or (C[y-1][x]>=1 and C[y-1][x]<=5)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=7 and C[y][x+1]<=16) or (C[y][x+1]>=1 and C[y][x+1]<=5)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=7 and C[y][x-1]<=16) or (C[y][x-1]>=1 and C[y][x-1]<=5)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_xiang(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    option1=[x+1,x-1]
    option2=[y+1,y-1]
    if (((C[y+1][x]>=9 and C[y+1][x]<=16) or (C[y+1][x]>=1 and C[y+1][x]<=5)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=9 and C[y-1][x]<=16) or (C[y-1][x]>=1 and C[y-1][x]<=5)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=9 and C[y][x+1]<=16) or (C[y][x+1]>=1 and C[y][x+1]<=5)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=9 and C[y][x-1]<=16) or (C[y][x-1]>=1 and C[y][x-1]<=5)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_che(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    option1=[x+1,x-1]
    option2=[y+1,y-1]
    if (((C[y+1][x]>=11 and C[y+1][x]<=16) or (C[y+1][x]>=1 and C[y+1][x]<=5)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=11 and C[y-1][x]<=16) or (C[y-1][x]>=1 and C[y-1][x]<=5)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=11 and C[y][x+1]<=16) or (C[y][x+1]>=1 and C[y][x+1]<=5)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=11 and C[y][x-1]<=16) or (C[y][x-1]>=1 and C[y][x-1]<=5)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_ma(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    if (((C[y+1][x]>=13 and C[y+1][x]<=16) or (C[y+1][x]>=1 and C[y+1][x]<=5)) and F[y+1][x]==1) or C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if (((C[y-1][x]>=13 and C[y-1][x]<=16) or (C[y-1][x]>=1 and C[y-1][x]<=5)) and F[y-1][x]==1) or C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if (((C[y][x+1]>=13 and C[y][x+1]<=16) or (C[y][x+1]>=1 and C[y][x+1]<=5)) and F[y][x+1]==1) or C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if (((C[y][x-1]>=13 and C[y][x-1]<=16) or (C[y][x-1]>=1 and C[y][x-1]<=5)) and F[y][x-1]==1) or C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
def red_pao(x,y):
    button_choice[8*(y-1)+x].config(bg="red",command = lambda:goback(x,y))
    for i in range (1,33):
        button_choice[i]["state"] = "disabled"
    button_choice[8*(y-1)+x]["state"] = "normal"
    
    if C[y+1][x]==0:
        button_choice[8*(y+1-1)+x].config(bg="green",command = lambda:move(x,y,x,y+1))
        button_choice[8*(y+1-1)+x]["state"] = "normal"
    if C[y-1][x]==0:
        button_choice[8*(y-1-1)+x].config(bg="green",command = lambda:move(x,y,x,y-1))
        button_choice[8*(y-1-1)+x]["state"] = "normal"
    if C[y][x+1]==0:
        button_choice[8*(y-1)+x+1].config(bg="green",command = lambda:move(x,y,x+1,y))
        button_choice[8*(y-1)+x+1]["state"] = "normal"
    if C[y][x-1]==0:
        button_choice[8*(y-1)+x-1].config(bg="green",command = lambda:move(x,y,x-1,y))
        button_choice[8*(y-1)+x-1]["state"] = "normal"
        
    for i in range (1,10):
        if (C[y+i][x]==-1):
            jumpd=0
            break
        if (C[y+i][x]>=1 and C[y+i][x]<=32):
            jumpd=i
            break
    for i in range (1,10):
        if C[y+jumpd+i][x]==-1 or (C[y+jumpd+i][x]>=17 and C[y+jumpd+i][x]<=32):
            break
        if ((C[y+jumpd+i][x]>=1 and C[y+jumpd+i][x]<=16) and F[y+jumpd+i][x]==1):
            def f(a=x,b=y,c=x,d=y+jumpd+i):
                move(a,b,c,d)
            button_choice[8*(y+jumpd+i-1)+x].config(bg="green",command = f)
            button_choice[8*(y+jumpd+i-1)+x]["state"] = "normal"
            print(x,y,x,y+i+jumpd,jumpd,i)    
            break
            
    for i in range (1,10):
        if C[y-i][x]==-1:
            jumpu=0
            break
        if (C[y-i][x]>=1 and C[y-i][x]<=32):
            jumpu=i
            break
    for i in range (1,10):
        if C[y-jumpu-i][x]==-1 or (C[y-jumpu-i][x]>=17 and C[y-jumpu-i][x]<=32):
            break
        if ((C[y-jumpu-i][x]>=1 and C[y-jumpu-i][x]<=16) and F[y-jumpu-i][x]==1):
            def f(a=x,b=y,c=x,d=y-jumpu-i):
                move(a,b,c,d)
            button_choice[8*(y-jumpu-i-1)+x].config(bg="green",command = f)
            button_choice[8*(y-jumpu-i-1)+x]["state"] = "normal" 
            print (x,y,x,y-i-jumpu,jumpu,i)  
            break
            
    for i in range (1,10):
        if (C[y][x+i]==-1):
            jumpr=0
            break
        if (C[y][x+i]>=1 and C[y][x+i]<=32):
            jumpr=i
            break
    for i in range (1,10):
        if (C[y][x+jumpr+i]==-1) or (C[y][x+jumpr+i]>=17 and C[y][x+jumpr+i]<=32):
            break
        if ((C[y][x+jumpr+i]>=1 and C[y][x+jumpr+i]<=16) and F[y][x+jumpr+i]==1):
            def f(a=x,b=y,c=x+jumpr+i,d=y):
                move(a,b,c,d)
            button_choice[8*(y-1)+x+jumpr+i]["state"] = "normal"
            button_choice[8*(y-1)+x+jumpr+i].config(bg="green",command =f)
            print(x,y,x+jumpr+i,y,jumpr,i)
            break
            
    for i in range (1,10):
        if (C[y][x-i]==-1):
            jumpl=0
            break
        if (C[y][x-i]>=1 and C[y][x-i]<=32):
            jumpl=i
            break
    for i in range (1,10):
        if C[y][x-jumpl-i]==-1 or (C[y][x-jumpl-i]>=17 and C[y][x-jumpl-i]<=32):
            break
        if ((C[y][x-jumpl-i]>=1 and C[y][x-jumpl-i]<=16) and F[y][x-jumpl-i]==1):
            def f(a=x,b=y,c=x-jumpl-i,d=y):
                move(a,b,c,d)
            button_choice[8*(y-1)+x-jumpl-i].config(bg="green",command =f)
            button_choice[8*(y-1)+x-jumpl-i]["state"] = "normal"  
            print(x,y,x-jumpl-i,y,jumpl,i)
            break

def flip(x,y):
    #print(C[y-1][x],C[y][x])
    global round
    if round==2:
        if C[y][x]>16:
            round=0
        else:
            round=1
    button_choice[8*(y-1)+x].config(command=lambda: choose(x,y))
    F[y][x]=1
    if C[y][x]>=1 and C[y][x]<=5:
        button_choice[8*(y-1)+x].config(image= img15)

    elif C[y][x]==6:
        button_choice[8*(y-1)+x].config(image= img6)

    elif C[y][x]==7 or C[y][x]==8:
        button_choice[8*(y-1)+x].config(image= img78)

    elif C[y][x]==9 or C[y][x]==10:
        button_choice[8*(y-1)+x].config(image= img910)

    elif C[y][x]==11 or C[y][x]==12:
        button_choice[8*(y-1)+x].config(image= img1112)

    elif C[y][x]==13 or C[y][x]==14:
        button_choice[8*(y-1)+x].config(image= img1314)

    elif C[y][x]==15 or C[y][x]==16:
        button_choice[8*(y-1)+x].config(image= img1516)

    elif C[y][x]>=17 and C[y][x]<=21:
        button_choice[8*(y-1)+x].config(image= img1721)

    elif C[y][x]==22:
        button_choice[8*(y-1)+x].config(image= img22)

    elif C[y][x]==23 or C[y][x]==24:
        button_choice[8*(y-1)+x].config(image= img2324)

    elif C[y][x]==25 or C[y][x]==26:
        button_choice[8*(y-1)+x].config(image= img2526)

    elif C[y][x]==27 or C[y][x]==28:
        button_choice[8*(y-1)+x].config(image= img2728)

    elif C[y][x]==29 or C[y][x]==30:
        button_choice[8*(y-1)+x].config(image= img2930)

    elif C[y][x]==31 or C[y][x]==32:
        button_choice[8*(y-1)+x].config(image= img3132)
    if round==1:
        round=0
    elif round==0:
        round=1
    clear()

for y in range (1,5):
    for x in range (1,9):
        def func(a=x,b=y):
            #print(a,b,x,y)
            flip(a,b)
        button_choice[8*(y-1)+x] = Button(w,image= img0,bg="gray")
        button_choice[8*(y-1)+x].config(command = func)
        button_choice[8*(y-1)+x].grid(row=y, column=x, sticky='nsew')



user = Label(text="暗棋")
user.grid(row=0, column=0)

w.mainloop()#常駐主視窗