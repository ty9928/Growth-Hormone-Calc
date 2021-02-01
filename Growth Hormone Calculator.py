#Ty Stoner
#This program takes a selected Growth Hormone Drug and converts to day supply



print("Growth Hormone Calculator ")
print("""
This program is capable of calculating day supply for growth hormone drugs:
    Command   Drug Description
    -------   ----------------
    A -- Norditropin Flexpro 5mg/1.5ml
    B -- Norditropin Flexpro 10mg/1.5ml
    C -- 
""")

command=str(input("Select Drug: "))

if command == "A":
    print ("Please provide following information for calculation")
    Q = int(input("Number of Pens: "))
    D = float(input("Dose (mg): "))
    D1 = int(D)
    I = int(input("Injections per week: "))
    while True:
        try:
            input=int(D)
        except ValueError:
            print("That's not a number")
        else:
            if 0.025 <= input <= 2:
                DS = (4.975*Q*(1/D)*(7/I))
                print ('Days Supply: ',DS)
                print ("""
                Enter 2 for each 1.5ml pen
                Stability 28 days after initial injection
                Needs pen needles supply
                Device supplied by manufacturer
                CIII in CO, ID, MN, NV, RI, WV
                Sub-Q only
                """)
                break
            else:
                print("Not in dose range for this medication")
                break
    
elif command == "B":
    print ("Please provide following information for calculation")
    Q = int(input("Number of Pens: "))
    D = float(input("Dose (mg): "))
    D1 = int(D)
    I = int(input("Injections per week: "))
    while True:
        try:
            input=int(D)
        except ValueError:
            print("That's not a number")
        else:
            if 0.05 <= input <= 4:
                DS = (9.95*Q*(1/D)*(7/I))
                print ('Days Supply: ',DS)
                print("""
                Enter 2 for each 1.5ml pen
                Stability 28 days after initial injection
                Needs pen needles supply
                Device supplied by manufacturer
                CIII in CO, ID, MN, NV, RI, WV
                Sub-Q only
                """)
                break
            else:
                print("Not in dose range for this medication")
                break
        
else:
    print("Error: invalid selection")
    print(description)   

