import pandas as pd
import numpy as np
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',database='project',user='root',password='sohar0409')
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Airport

print("""     +-----------------------------------------------------------+
     | \t\t\tWELCOME TO MUSCAT INTERNATIONAL AIRPORT\t\t\t |
     +-----------------------------------------------------------+""")
print()
print("A study on the Cleanest and Busiest Airports in the Middle East")     

#Graph 1
import matplotlib.pyplot as p
a=['Doha','Muscat','Dubai','Bahrain','Medina','Jeddah','Salalah','Riyadh']
b=[38.8,15.9,86.4,9.5,8.4,45.0,1.25,26.0]
p.xlabel("Airports Name Ordered by Cleanliness")
p.ylabel("Number of Passengers in millions")
p.title("Passenger Traffic in Middle East's Cleanest Airports")
p.bar(a,b,color=['m','c','r','g','y','b','purple','pink'],width=0.6,edgecolor='k',linewidth=0.4,linestyle='dashdot')
p.show()
print()

#Airlines
print("The Top 5 Middle East Airlines")

#Graph 2
a=['Oman Air','Etihad Airyays','Saudi Arabian Airways','Qatar Airways','Emirates']
b=[70.2,40.8,40.6,20.2,10.3]
p.xlabel("Seat Capacity")
p.ylabel("Airlines")
p.title("Top 5 Middle East Airlines in 2019")
p.barh(a,b,color=['m','c','r','y','g'],edgecolor='k',linewidth=0.4,linestyle='dashdot')
p.show()
print()
#Login
print('\t\t----------------------')
print('\t\tSelf Check-in Services')
print('\t\t----------------------')
Name=input("Enter your Full Name:")
def Login():
     
     print('CHOOSE YOUR AIRLINE')   
    
     Airline=int(input("""Choose your Airline
                  1 Oman Air
                  2 Air India
                  3 Jet Airways
                  4 Turkish Airline 
                  5 Emirates
                  6 Ethihad
                  7 Qatar Airways
                  8 Spice Jet
         (Enter the number of the desired Airline)
          Enter::"""))   
     if Airline==1:
         Omanair()
     elif Airline==2:
         AirIndia()
     elif Airline==3:
         JetAirways()
     elif Airline==4:
         TurkishAirlines() 
     elif Airline==5:
         Emirates() 
     elif Airline==6:
         EtihadAirways()    
     elif Airline==7:
         QatarAirways()
     elif Airline==8:
         SpiceJet() 
     else:
          print("invalid input")
          x=input("""enter 'yes' to try again 
                 enter:""")
          if x=='yes':
             Login()
         
#OmanAir
def Omanair():
    print("You chose Oman Air")
    print("\nThe format of Booking Reference for Oman Air is:: OM200'ENTER your last and first name initials'")
    print("\nExample: \n FOR NAME Ravi Krishnan \n the reference ID is OM200RK")
    Reference_ID=input("Your Reference ID:OM200")
    x=len(Reference_ID)
    if x!=2:
        print("Invalid Reference_ID\nTry Again")
        Tryagain=input("Enter 'Yes' to Try Again: ")
        if Tryagain=='Yes':
            Omanair()
    else:
        print("LOGGED IN")
        
#AirIndia        
def AirIndia():
     print("You chose Air India")
     print("\n The format of Booking Reference for Oman Air is:: AI155'ENTER your last and first name initials'")
     print("\n Example: \n FOR NAME Ravi Krishnan \n the reference ID is AI155RK")
     Reference_ID=input("Your Reference ID:AT155") 
     x=len(Reference_ID)
     if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             AirIndia()
     else:
        print('LOGGED IN')

#JetAirways
def JetAirways():
     print("You chose Jet Airways")
     print("\n The format of Booking Reference for Jet Airways is:: JA188'ENTER your last and first name initials'")
     print("\n Example: \n FOR NAME Ravi Krishnan \n the reference ID is JA188RK")
     Reference_ID=input("Your Reference ID:JA188") 
     x=len(Reference_ID)
     if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             JetAirways()
     else:
        print('LOGGED IN')   
         
def TurkishAirlines():
     print("You chose Turkish Airlines")
     print("\n The format of Booking Reference for Turkish Airlines is:: TA345'ENTER your last and first name initials'")
     print("\n Example: \n FOR NAME Ravi Krishnan \n the reference ID is TA345RK")
     Reference_ID=input("Your Reference ID:TA345") 
     x=len(Reference_ID)
     if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             TurkishAirlines()
     else:
        print('LOGGED IN') 

def Emirates():        
    print("You chose Emirates")
    print("\nThe format of Booking Reference for Emirates is:: EM600'ENTER your last and first name initials'")
    print("\nExample: \n For name Ravi Krishnan, \n the reference ID is EM600RK")    
    Reference_ID=input("Your Reference ID:EM600") 
    x=len(Reference_ID) 
    if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             Emirates()
    else:
        print('LOGGED IN')

def EtihadAirways():
    print("You chose Etihad Airways")
    print("\nThe format of Booking Reference for Etihad Airways is:: EA700'ENTER your last and first name initials'")
    print("\nExample: \n FOR Name Ravi Krishnan, \n the reference ID is EA700RK")
    Reference_ID=input("Your Reference ID:EA700")
    x=len(Reference_ID)  
    if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             EtihadAirways()
    else:
        print('LOGGED IN')  
        
def QatarAirways():
    print("You chose Qatar Airways")
    print("\nThe format of Booking Reference for Qatar Airways is:: QA0800'ENTER your last and first name initials'")
    print("\nExample: \n For name Ravi Krishnan, \n the reference ID is QA800RK")
    Reference_ID=input("Your Reference ID:QA800")
    x=len(Reference_ID)  
    if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             QatarAirways()
    else:
        print('LOGGED IN') 
        
def SpiceJet():
    print("You chose Spice Jet")
    print("\nThe format of Booking Reference for Ethihad is:: SJ900'ENTER your last and first name initials'")
    print("\nExample: \n For name Ravi Krishnan, \n the reference ID is SJ900RK")
    Reference_ID=input("Your Reference ID:SJ900")   
    x=len(Reference_ID)
    if x!=2:
         print("Invalid Reference_ID")
         Tryagain=input("Enter 'Yes' to Try Again: ")
         if Tryagain=='Yes':
             SpiceJet()
    else:
        print('LOGGED IN')        
Login()



    


             


        
# restricter items
fig, ax = plt.subplots()

ax.set_xlim(0, 2)
ax.set_ylim(0, 4)

arr_lena = mpimg.imread('C:/Users/HP/Downloads/WhatsApp Image 2022-01-12 at 22.31.37.jpeg')
imagebox = OffsetImage(arr_lena, zoom=0.85)

ab = AnnotationBbox(imagebox, (1,2))

ax.add_artist(ab)

plt.grid()

plt.draw()
plt.show()
#FlightInfo-Table1
print("Flight Confirmation")
print("""\t\t\t\t+------------------------+
                |    Flight Information  |
                +------------------------+""") 
df=pd.read_csv("C:\\Users\\HP\\Downloads\\Flight_Information - Sheet1 (1).csv")
print(df)
print()
flight=int(input("Enter the number from the above table that corresponds with your flight:"))    
    


fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 4)
arr_lena = mpimg.imread('C:/Users/HP/Downloads/WhatsApp Image 2022-01-11 at 00.31.56.jpeg')
imagebox = OffsetImage(arr_lena, zoom=0.89)
ab = AnnotationBbox(imagebox, (1,2))
ax.add_artist(ab)
plt.grid()
plt.draw()
#plt.savefig('C:/Users/HP/Downloads/Red-Rose.jpg',bbox_inches='tight')
plt.show()


def seat():
    
    
    print("""\t\t+------------------------+
        |      Seat Details      |
        +------------------------+""")
    # seat arrangement
    
    print('Would you like to :: CHANGE SEAT OR SKIP')
    print("Enter 1 for Change Seat ")
    print('Enter 2 for Skip')
    change=int(input('Enter:'))
    print("\n")
    if change==1:
        changeseat()
    if change==2:
        print("Refer the above seat arrangement image")
        originalseat=input("""Enter your seat number
                           Example: 6A
                           ENTER:""")
        print("YOUR BORDING PASS NOW READY!!")
        
               
def changeseat():
     Class=int(input("""Choose your class
                 1 Business Class
                 2 Economy Class
                Choose the number for your preferred class:"""))
     if Class==1:
         Business()
         enterseat1()
     elif Class==2:
         Economy()
         enterseat2()
     else:
         print("invalid input")
         x=input("""enter 'yes' to try again 
                 enter:""")
         if x=='yes':
             changeseat()
             
         
         
     
        
         
def Economy():
         df1=pd.read_sql('select * from seat;',mycon)
         print(df1)
         print()
         
def enterseat2():
    seatinput=input("""Your Seat Number
                    Example:6A
                    Enter:""")
    X=['6A','7E','10B','12F','14B','14E','15A','15D','16C','18A','18C','18F','20D','20E','22F','25C']
    if seatinput in X:
     print("YOUR BORDING PASS IS NOW READY!!")
    else:
       print('invalid')
       enterseat2()
   
         
def Business():
    df1=pd.read_sql('select * from Business_Class;',mycon)
    print(df1)
    print()
    
         
def enterseat1():
    seatinput=input("""Your Seat Number
                    Example:6A
                    Enter:""")
    X=['1A','1D','2C','3A','3F','4A','4C','4D']                
    if seatinput in X:
     print("YOUR BORDING PASS IS NOW READY!!")
    else:
       print('invalid')
       enterseat1() 
seat()



if flight ==0:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)    HYD             SHTI2J          |
        | from oman     /        to India         flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        10:02                1A          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==1:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)    SHJ             QFTO6U          |
        | from oman     /        to Dubai         flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        08:34                3B          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==2:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)    DIA             BAWT4E          |
        | from oman     /        to Qatar         flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        12:51                5E          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==3:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)     AMS            EING9Q          |
        | from oman     /        to Netherlands   flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        01:03               10J          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==4:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)     SYD            UK10TIO         |
        | from oman     /        to Australia     flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        04:46                7H          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==5:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)     MOW            IXERT12         |
        | from oman     /        to Netherlands   flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        06:53               4D           |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==6:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|               \                                         |
        |           _____\___                                     |
        |  MCT      _________)     BKK            RJVP10          |
        | from oman     /        to Bangkok       flightNo.       | 
        |              /                                          |""")
    print("""\t\t|                        11:11               12C          |
        |                      departure time      gateNo.        |""") 
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")
elif flight==7:
    print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
    print(""" \t\t|                \                                        |
        |            _____\___                                    |
        |  MCT       _________)    DEL            IXERT78         |
        | from oman       /        to India              flightNo.|
        |                /                                        |""")
    print("""\t\t|                        16:21                3E          |
        |                      departure time      gateNo.        |""")
    print("\t\t|  ",Name)
    print("\t\t| passenger name                                          |")
    print("\t\t+---------------------------------------------------------+")    
elif flight==8:
   print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
   print(""" \t\t|                \                                        |
        |            _____\___                                    |
        |  MCT       _________)    LON             SRIJ2P         |
        | from oman       /        to UK                 flightNo.|
        |                /                                        |""")
   print("""\t\t|                        12:54                8F          |
        |                      departure time      gateNo.        |""")
   print("\t\t|  ",Name)
   print("\t\t| passenger name                                          |")
   print("\t\t+---------------------------------------------------------+")  
elif flight==9:
   print("""\t\t+---------------------------------------------------------+
        |  BOARDING PASS                                          |""")
   print(""" \t\t|                \                                        |
        |            _____\___                                    |
        |  MCT       _________)    IST             HANT5C         |
        | from oman       /        to Turkey             flightNo.|
        |                /                                        |""")
   print("""\t\t|                        18:30                6K          |
        |                      departure time      gateNo.        |""")
   print("\t\t|  ",Name)
   print("\t\t| passenger name                                          |")
   print("\t\t+---------------------------------------------------------+")

print()
print("The total baggage allowance per person is max 30kg ")
print("The total no of bags allowed per person is 3")
Bagtags=int(input("enter the no of bags you are carryinng:"))
if Bagtags==1:
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")
elif Bagtags==2:
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")
elif Bagtags==3:
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")    
    print("""\t\t\t\t            +-----------+
                            |           |
                            |  BAGGAGE  |
                            |    TAG    |
                            |   =====   |
                            |   =====   |
                            |  MCT INT  |
                            |           |
                            |  MCTIA108 |
                            |           |
                            \   SAFE    /
                             \ TRAVELS /
                              \       /
                               +-----+""")    
# covid restrictions
fig, ax = plt.subplots()

ax.set_xlim(0, 2)
ax.set_ylim(0, 4)

arr_lena = mpimg.imread('C:/Users/HP/Pictures/covid safety.jpg')

imagebox = OffsetImage(arr_lena, zoom=0.65)

ab = AnnotationBbox(imagebox, (1,2))

ax.add_artist(ab)

plt.grid()

plt.draw()
plt.show()
print('THANK YOU FOR USING OUR SERVICES!')



















