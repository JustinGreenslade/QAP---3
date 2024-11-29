#Code for the Hotel Reservation Program
 
# Description:
# Author:
# Date(s):
 
 
# Define required libraries.
import datetime
 
 
# Define program constants.
REG_RATE = 85.00
HIGH_RATE = 105.00
 
 
# Define program functions.
 
 
 
# Main program starts here.
while True:
    print()
    print()
    # Gather user inputs.
    print("The Hotel Reservation System")
    print()
 
    while True:
        try:
            ArrDate = input("Enter the arrival date (YYYY-MM-DD):   ")
            ArrDate = datetime.datetime.strptime(ArrDate, "%Y-%m-%d")
        except:
            print()
            print("   Data Entry Error - Arrival date is invalid - use YYYY-MM-DD format ...")
            print()
        else:
            break
 
    while True:
        try:
            DepDate = input("Enter the departure date (YYYY-MM-DD): ")
            DepDate = datetime.datetime.strptime(DepDate, "%Y-%m-%d")
        except:
            print()
            print("   Data Entry Error - Departure date is invalid - use YYYY-MM-DD format ...")
            print()
        else:
            break
   
 
    # Perform required calculations.
    ArrMonth = ArrDate.month
    if ArrMonth != 7 and ArrMonth != 8:
        NightRate = REG_RATE
        NightMsg = ""
    else:
        NightRate = HIGH_RATE
        NightMsg = "(High Season Rate Applied)"
 
    NumNights = (DepDate - ArrDate).days
    TotalPrice = NumNights * NightRate
 
 
    # Display results
    print()
    print()
    ArrDateDsp = datetime.datetime.strftime(ArrDate, "%B %d, %Y")
    print(f"Arrival date:     {ArrDateDsp:<18}")
    DepDateDsp = datetime.datetime.strftime(DepDate, "%B %d, %Y")
    print(f"Departure date:   {DepDateDsp:<18}")
 
    NightRateDsp = "${:,.2f}".format(NightRate)
    print(f"Nightly rate:     {NightRateDsp:<7s} {NightMsg:<26s}")
    print(f"Total nights:     {NumNights:<2d}")
 
    TotalPriceDsp = "${:,.2f}".format(TotalPrice)
    print(f"Total price:      {TotalPriceDsp:<8s}")
   
    print()
    while True:
        Continue = input("Continue (Y/N): ").upper()
 
        if Continue != "Y" and Continue != "N":
            print()
            print("   Data Entry Error - Contnue option must be a Y or an N ...")
            print()
        else:
            break
   
    if Continue == "N":
        break
 
 
    # Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.
print("Thank you for using The Hotel Reservation Program,  Bye Bye.")
 
 












 
#And here is the code for the Sales Invoice Analysis.
 
# Description:
# Author:
# Date(s):
 
 
# Define required libraries.
import datetime
 
 
# Define program constants.
CUR_DATE = datetime.datetime.now()
 
 
# Define program functions.
 
 
 
# Main program starts here.
while True:
   
    # Gather user inputs.
    print()
    print()
    while True:
        try:
            InvDate = input("Enter the invoice date (YYYY-MM-DD): ")
            InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
        except:
            print()
            print("   Data Entry Error - Invoice date is invalid - use YYYY-MM-DD format ...")
            print()
        else:
            break
 
    while True:
        try:
            InvAmt = input("Enter the invoice amount: ")
            InvAmt = float(InvAmt)
        except:
            print()
            print("   Data Entry Error - Invoice amount is invalid ...")
            print()
        else:
            break
 
 
    # Perform required calculations.
    DisDate = InvDate + datetime.timedelta(days=10)
    DueAfterDis = InvAmt * .98  # or = InvAmt - (InvAmt * .02)
    DueDate = InvDate + datetime.timedelta(days=30)
    InvAge = (CUR_DATE - InvDate).days
 
 
    # Display results
    print()
    print()
    print("INVOICE ANALYSIS")
    print()
 
    InvAmtDsp = "${:,.2f}".format(InvAmt)
    print(f"Invoice amount:            {InvAmtDsp:>10s}")
 
    print()
    DisDateDsp = datetime.datetime.strftime(DisDate, "%Y-%m-%d")
    print(f"Discount date:             {DisDateDsp:>10s}")
    DueAfterDisDsp = "${:,.2f}".format(DueAfterDis)
    print(f"Amount due with discount:  {DueAfterDisDsp:>10s}")
 
    print()
    print(f"Invoice age:                {InvAge} days.")
 
 
    # Write the values to a data file for storage.
 
 
 
# Any housekeeping duties at the end of the program.
 
 