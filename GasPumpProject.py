from math import ceil
import sys
def main():
    print("Hello and Welcome to Tuck's Gas ")  
    print('{:_<50}'.format("_"))
    keepGoing = input("\nPress any key to start pumping, otherwise press 'Q' to quit: ")
    while keepGoing != "Q" and keepGoing != "q":
        try:
            Reg = 2.59
            Med = 3.25
            Pre = 3.82
            print("Please select a fuel type")
            print()
            print("-Reg unleaded: $%s" % Reg)
            print("-Med unleaded: $%s" % Med)
            print("-Premium unleaded: $%s" % Pre)          
            GasType =  input('\n Press R for Regular, M for Medium, and P for Premium: ')
            while GasType == "R" or GasType == "r":
                UserGallons = input("How many gallons would you like?: ")
                print()
                try:
                    UserGallons = float(UserGallons)
                    #UserGallons was a float, I needed to change it to an iterable integer for the for loop
                    #while presserving the input, used ceil and created an iterable number 
                    iterableGallon = int(ceil(UserGallons))
                    if UserGallons > 0:
                        GasLabel = "Regular"
                        GasType = Reg
                        tax = .06 * (UserGallons * Reg)
                        price = tax + (UserGallons * Reg)
                        priceCount = 0
                        for i in range(iterableGallon):
                            priceCount += GasType
                            print("      $%s" % round(priceCount, 2),"|",i +1,"Gallons\n")
                        GasType = Recipte(GasLabel, GasType, price, UserGallons)
                        keepGoing = input("\nPress any key to start pumping, otherwise press 'Q' to quit: ")
                    else:
                        print("Must be positive number of gallons")                
                except:
                    print("Must be a number")
    
            while GasType == "M" or GasType == "m":
                UserGallons = input("How many gallons would you like?: ")
                try:
                    UserGallons = float(UserGallons)
                    iterableGallon = int(ceil(UserGallons))
                    if UserGallons > 0:
                        GasLabel = "Medium"
                        GasType = Med
                        tax = .06 * (UserGallons * Med)
                        price = tax + (UserGallons * Med)
                        priceCount = 0
                        for i in range(iterableGallon):
                            priceCount += GasType
                            print("      $%s" % round(priceCount, 2),"|",i +1,"Gallons\n")
                        GasType = Recipte(GasLabel, GasType, price, UserGallons)
                        keepGoing = input("\nPress any key to start pumping, otherwise press 'Q' to quit: ")
                    else:
                        print("Must be positive number of gallons")
                except:
                    print("Must be a number")
            while GasType == "P" or GasType == 'p':
                UserGallons = input("How many gallons would you like?: ")
                try:
                    UserGallons = float(UserGallons)
                    iterableGallon = int(ceil(UserGallons))
                    if UserGallons > 0:
                        GasLabel = "Premium"
                        GasType = Pre
                        tax = .06 * (UserGallons * Pre)
                        price = tax + (UserGallons * Pre)
                        priceCount = 0
                        for i in range(iterableGallon):
                            priceCount += GasType
                            print("      $%s" % round(priceCount, 2),"|",i +1,"Gallons\n")
                        GasType = Recipte(GasLabel, GasType, price, UserGallons)
                        keepGoing = input("\nPress any key to start pumping, otherwise press 'Q' to quit: ")
                    else:
                        print("Must be positive number of gallons\n")
                except:
                    print("Must be a number")
        except:
            print("Please enter a valid option \n\n")
    else:
        sys.quit()
       
def Recipte(GasLabel, GasType, price, UserGallons):
    #Recipt function called only if all the booleans above are passed, used to generate a recipt with final product info
    print('{:*<50}'.format("*"))
    print("\nThank you for using Tuck's Gas come back to see us again\n")
    print("           Hebron \n      1684 Petersburg RD \n            KY\n")
    print("Product: ",GasLabel)
    print("Price per Gallon: $%s" % GasType)
    print("Tax: 6%")
    print("Total: $%s" % round(price,2))
    print()
    print(UserGallons,"Gallons of gas at $%s" % GasType,"equals $%s" % round(price,2),"total.\n")
    return(GasType)
main()