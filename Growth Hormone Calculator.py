#------------------------------------------------------------------------------#
# Program: Growth Hormone Calculator
# By: Ty Stoner
#
# Desc:
# This program takes a selected Growth Hormone Drug and converts to day supply
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Function: get_inputs
# @brief
# Prompt user for calculation inputs, return a tuple of the inputs
#------------------------------------------------------------------------------#
def get_inputs():
    print("  Information for calculation")
    print("-------------------------------")

    Q = float(input("Number of Pens: "))
    D = float(input("Dose (mg): "))
    I = float(input("Injections per week: "))

    if D < 0.025 or D > 2:
        print("ERROR: D value", D, "is invalid!")
        exit(1)

    return (Q, D, I)

#------------------------------------------------------------------------------#
# Begin Main
#------------------------------------------------------------------------------#
print("Growth Hormone Calculator ")
print("""
This program is capable of calculating day supply for growth hormone drugs:
    Command   Drug Description
    -------   ----------------
    A -- Norditropin Flexpro 5mg/1.5ml
    B -- Norditropin Flexpro 10mg/1.5ml
""")

hormone_dict = {
    "A" : 4.975,
    "B" : 9.95       
}

command = input("Select Drug: ")

if command in hormone_dict:
    (Q, D, I) = get_inputs()
    const = hormone_dict[command]

    # Perform Calculation
    DS = (const * Q * (1 / D) * (7 / I))

    print ('Days Supply:', DS)

    print ("""
    Enter 2 for each 1.5ml pen
    Stability 28 days after initial injection
    Needs pen needles supply
    Device supplied by manufacturer
    CIII in CO, ID, MN, NV, RI, WV
    Sub-Q only
    """)
else:
    print("Error: invalid selection!")

promptExit = input("Press Enter to Exit...")
exit(0)
