import random
wlcm = "please  print what is your gusee： "
paswd = 123
def xunh():    
    
        
        print("")
        print("------------------------------")
        print("----------AGAIN  ！ ！  ！----")
        print("------------------------------")
        gus()
def sc():
    print("good!!!!!!")
    xunh()
    
def gus():
    com_num = random.randint(1,100)
    print("RANDOM WILL BE :",com_num)
    a =1 
    while a<5:
#        com_num = random.randint(1,100)
        y_num = int(input(wlcm))
        if y_num == com_num:
            print("SUSSEEFUL!!!")
            sc()
        elif y_num > com_num:
            print("biger ，try again as lower")
        else:
            print("lower ,try uper")
        a += 1
    b=1
    while b<4:
        ch=4-b
        print("猜数字机会用完了，输入密码再来一次,还有",ch,"次机会")
        pppps = input("请输入密码:  ")
        if paswd == int(pppps):
            gus()
            
        elif 3-b>0:
            print("密码错误，再次输入")
            
        else:
            
            print("密码全错了,再来一局")
            xunh()
        b +=1
       
xunh()    


gus()


