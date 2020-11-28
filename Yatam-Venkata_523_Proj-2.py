from CarClassFile import Car #import Car class from CarClassfile
import datetime as tm

myhybrid = Car(20)
while True:
    infile1=open("LogFuel.txt","a")  #inputs to new log file
    print('select from the below menu ')     #display menu
    print(' '*10,'1. see current fuel')
    print(' '*10,'2.drive')
    print(' '*10,'3.add gas ')
    print(' '*10,'4.exit')
    value=int(input('enter your choice from above: '))  #user enters choice from menu
    print('Selected option is',value)   
    if value==1:
        infile1.write('\n' + str(tm.datetime.now())+ ' >User Choice is 1\n') #write timestamp and user choice to log
        infile1.write("     The current fuel level is "+ str(myhybrid.getfuellevel())+ "\n") #write current fuel level
        print('Gas in car is: ',myhybrid.getfuellevel())
    elif value ==2:
        b=float(input('How many miles you would like to Drive? :')) #user inputs miles to drive
        infile1.write('\n'+ str(tm.datetime.now())+ ' >User Choice is 2\n') #timestamp and user choice updated to log
        infile1.write("     Miles to drive "+str(b)+" - ")
        n= myhybrid.drive(b) #access class and processess distance driven
        nm= myhybrid._totaldistance #distance car can still travel
        print('you can drive '+str(n)+' miles - still '+str(nm)+'  miles are left') #show miles to drive and miles left
        infile1.write('You can drive '+str(n)+' miles - still '+str(nm)+'  miles are left\n')#writes to log
    elif value==3:
        c=float(input('How much gallons of gas you want to fill: ')) #user inputs gas to be filled
        d = myhybrid.addGas(c)  #gas which can be added to tank
        print('Total gas in tank is ',myhybrid.getfuellevel(),' gallons')
        infile1.write('\n' + str(tm.datetime.now())+ ' >User Choice is 3\n') #writes to log
        infile1.write("     Number of gallons to be added "+str(d)+ ' - Total gas in tank is '+ str(myhybrid.getfuellevel())+' gallons\n')		
    elif value==4:
        infile1.write('\n' + str(tm.datetime.now())+ ' >User Choice is 4\n')
        infile1.write('Exit')
        print('exited')
        infile1.close
        exit()
    else:
        print("Bad Input")
        infile1.close
        exit()
        
   

   