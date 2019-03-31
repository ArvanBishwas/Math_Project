import time
print("Select The Temperature.")
print("1.Celsius")
print("2.Fahrenheit")
print("3.Kelvin")
print("4.Romer")
print("5.Rankine") 
print("if you don't understand, enter 'help'for the temperature details.")
print("Enter 'quit' for Exit")

while True:
    choice = input ("\nEnter choiceing temperature(1/2/3/4/5): ")
    time.sleep(1)
#=====================================

    if choice == '1':
        print("\nWelcome to Celsius temperature department.")
        print("1.Celsius to Fahrenheit")
        print("2.Celsius to Kelvin")
        print("3.Celsius to Romer")
        print("4.Celsius to Rankine")
        choice = input("Please choose an option: ")

        if choice == '1':
            celsius = float(input("Please enter the Celsius temperature: "))
            fahrenheit = (celsius*1.8)-32
            print('%0.2f degree Celsius is = %0.2f degree Fahrenheit'%(celsius,fahrenheit))
        elif choice == '2':
            celsius = float(input("Please enter the Celsius temprature: "))
            kelvin = celsius + 273
            print('%0.2f degree Celsius is = %0.2f degree Kelvin'%(celsius,kelvin))
        elif choice == '3':
            celsius = float(input("Please enter the Celsius temperature: "))
            romer =celsius/0.8
            print('%0.2f degree celsius is = %0.2f degree romer'%(celsius,romer))
        elif choice == '4':
            celsius = float(input("Please enter the Celsius temperature: "))
            rankine =(celsius*1.8)+492
            print('%0.2f degree celsius is = %0.2f degree rankine'%(celsius,rankine))
        elif choice == 'back':
            break
        
        else:
            print("Invalide Input")
            print("Please try again")



#=====================================

    elif choice == '2':
        print("\nWelcome to Fahrenheit temperature department.")
        print("1.Fahrenheit to Celsius")
        print("2.Fahrenheit to Kelvin")
        print("3.Fahrenheit to Romer")
        print("4.Fahrenheit to Rankine")
        choice = input("Please choose an option: ")
        
        if choice == '1':
            fahrenheit = float(input("Please enter the Fahrenheit temperature: "))
            celsius = (fahrenheit-32)/1.8
            print('%0.2f degree Fahrenheit is = %0.2f degree Celsius'%(fahrenheit,celsius))    
        elif choice == '2':
            fahrenheit = float(input("please enter the farhenheit temprature: "))
            kelvin = ((fahrenheit -32)/1.8)+273
            print('%0.2f degree Fahrenheit is = %0.2f degree Kelvin'%(fahrenheit,kelvin))
        elif choice == '3':
            fahrenheit = float(input("Please enter the fahrenheit temprature: "))
            romer =(fahrenheit-32)/2.25 
            print('%0.2f degree fahrenheit is = %0.2f degree romer'%(fahrenheit,romer))
        elif choice == '4':
            fahrenheit = float(input("Please enter the fahrenheit temprature: "))
            rankine = fahrenheit + 460
            print('%0.2f degree fahrenheit is = %0.2f degree rankine'%(fahrenheit,rankine))
        elif choice == 'back':
            break
        else:
            print("Invalide Input")
            print("Please try again")

#========================================

    elif choice == '3':
        print("\nWelcome to Kelvin temperature department.")
        print("1.Kelvin to Celsius")
        print("2.Kelvin to Fahrenheit")
        print("3.Kelvin to Romer")
        print("4.Kelvin to Rankine")
        choice = input("Please choose an option: ")
        if choice == '1':
            kelvin = float(input("Please enter the Kelvin temprature: "))
            celsius = (kelvin-273)
            print('%0.2f degree Kelvin is = %0.2f degree Celsius'%(kelvin,celsius))
        elif choice == '2':
            kelvin = float(input("Please enter the Kelvin temprature: "))
            fahrenheit = (1.8*(kelvin-273))+32
            print('%0.2f degree Kelvin is = %0.2f degree Fahrenheit'%(kelvin,fahrenheit))
        elif choice == '3':
            kelvin = float(input("Please enter the Kelvin temprature: "))
            romer = (kelvin-273)/0.8
            print('%0.2f degree Kelvin is = %0.2f degree Romer'%(kelvin,romer))
        elif choice == '4':
            kelvin = float(input("Please enter the Kelvin temprature: "))
            rankine = ((kelvin-273)/1.8)+492
            print('%0.2f degree Kelvin is = %0.2f degree Rankine'%(kelvin,rankine))
        elif choice == 'back':
            break
        else:
            print("Invalide Input")
            print("Please try again")

#=======================================

    elif choice == '4':
        print("\nWelcome to Romer temperature department.")
        print("1.Romer to Celsius")
        print("2.Romer to Fahrenheit")
        print("3.Romer to kalvin")
        print("4.Romer to Rankine")

        choice = input("Please choose an option: ")
        if choice == '1':
            romer = float(input("Please enter the Romer temprature: "))
            celsius = romer/0.8
            print('%0.2f degree romer is = %0.2f degree Celsius'%(romer,celsius))
        elif choice == '2':
            romer = float(input("Please enter the Romer temprature: "))
            fahrenheit = (2.25*romer)+32
            print('%0.2f degree romer is = %0.2f degree Fahrenheit'%(romer,fahrenheit))
        elif choice == '3':
            romer = float(input("Please enter the Romer temprature: "))
            kelvin = (romer*0.8)+273
            print('%0.2f degree Romer is = %0.2f degree Kelvin'%(romer,kelvin))
        elif choice == '4':
            romer = float(input("Please enter the Romer temprature: "))
            rankine = (romer*2.25)+492
            print('%0.2f degree Romer is = %0.2f degree Rankine'%(romer,rankine))
        elif choice == 'back':
            break
        else:
            print("Invalide Input")
            print("Please try again")

#======================================

    elif choice == '5':
        print("\nWelcome to Rankine temperature department.")
        print("1.Rankine to Celsius")
        print("2.Rankine to Fahrenheit")
        print("3.Rankine to kalvin")
        print("4.Rankine to Rankine") 
        choice = input("Please choose an option: ")
        if choice == '1':
            rankine = float(input("Please enter the Rankine temprature: "))
            celsius = (rankine-492)/1.8
            print('%0.2f degree Rankine is = %0.2f degree Celsius'%(rankine,celsius))
        elif choice == '2':
            rankine = float(input("Please enter the Rankine temprature: "))
            fahrenheit = rankine - 460
            print('%0.2f degree rankine is = %0.2f degree Fahrenheit'%(rankine,fahrenheit))
        elif choice == '3':
            rankine = float(input("Please enter the Rankine temprature: "))
            kelvin = ((rankine-492)/1.8)+273
            print('%0.2f degree Rankine is = %0.2f degree Kelvin'%(rankine,kelvin))
        elif choice == '4':
            rankine = float(input("Please enter the Rankine temprature: "))
            romer = (rankine-492)/2.25
            print('%0.2f degre Rankine is = %0.2f degree Romer'%(rankine,romer))
        elif choice == 'back':
            break
        else:
            print("Invalide Input")
            print("Please try again")

#======================================

    elif choice == 'help':
        print("here,\nC = Celsuis,\nF = Fahrenheit,\nK = Kelvin,\nR = Romer,\nRn = Rankine\n")
        print("We know,\nC/5 = (F-32)/9 = (K-273)/5 = R/4 = (Rn-492)/9") 


    elif choice == 'quit':
            break 
            

    else:
        print("INVALIDE INPUT")
        print("Try again")





        
