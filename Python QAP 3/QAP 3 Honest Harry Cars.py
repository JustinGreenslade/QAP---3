# Description: This program keeps track of sales for Honest Harry's used car lot.
# Author: Justin Greenslade.
# Class: Python SD 13.
# Dates: Oct 09 - Oct 18, 2024


# Define required libraries.
import datetime


# Define program constants.
INVOICE_DATE = datetime.datetime.now()
STANDARD_RATE_LICENCE_FEE = 75.00 # Licence fee on cars up to and including $15,000.00
OVER_PRICE_LICENCE_FEE = 165.00 # Licence fee on cars over $15,000.00
TRANSFER_FEE = .01 # The transfer fee 1% of the selling price
LUXURY_TAX = .016 # luxury tax is calculated on the selling price if it is over $20,000 then added to the transfer fee.
HST = .15 # Taxes (HST) are calculated at 15% on the Subtotal.
FINACING_FEE = 39.99 # The financing fee at 39.99 per year
ALLOWED_NAME_CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVTXYZ abcdefghijklmnopqrstuvwxyz-")
ALLOWED_NUMBER_CHARACTERS = set("1234567890")
ALLOWED_PLATE_LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVTXYZ")


# Main program starts here.
print()
while True:
    
    # Gather user inputs.

    #Gets Customers first name.
    while True:
        FirstName = input("Enter the Customer first name (To end program type END): ").title()
        if FirstName == "":
            print()
            print("Data entry error - first name must be entered...")
            print()
        elif set(FirstName).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - first name must be valid characters...")
            print()
        else:
            break

    #If Customers first name entered "END" it will end the program.
    if FirstName.upper() == "END":
        break

    #Gets Customers last name.
    while True:
        LastName = input("Enter the Customer last name: ").title()
        if LastName == "":
            print()
            print("Data entry error - last name must be entered...")
            print()
        elif set(LastName).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - last name must be valid characters...")
            print()
        else:
            break

    #Gets Customers phone number.
    while True: 
        PhoneNumber = input("Enter the Customer phone number (0000000000): ")
        if PhoneNumber == "":
            print()
            print("Data entry error - phone number must be entered...")
            print()
        elif set(PhoneNumber).issubset(ALLOWED_NUMBER_CHARACTERS) == False:
            print()
            print("Data entry error - phone number must be valid characters...")
            print()
        elif len(PhoneNumber) != 10:
            print()
            print("Data entry error - phone number must be 10 characters...")
            print()
        else:
            break

    ##Gets Customers plate number.
    while True:
        PlateNumber = input("Enter the Customer plate number (XXX999): ").upper()
        if PlateNumber == "":
            print()
            print("Data entry error - plate number must be entered...")
            print()
        elif set(PlateNumber[0:3]).issubset(ALLOWED_PLATE_LETTERS) == False:
            print()
            print("Data entry error - plate number must start with letters (XXX999)...")
            print()
        elif set(PlateNumber[3:6]).issubset(ALLOWED_NUMBER_CHARACTERS) == False:
            print()
            print("Data entry error - plate number must end with numbers (XXX999)...")
            print()
        elif len(PlateNumber) != 6:
            print()
            print("Data entry error - plate number must be 6 characters...")
            print()
        else:
            break

    #Gets Customers Car Make.
    while True:
        CarMake = input("Enter the car make (ie: Toyota): ").title()
        if CarMake == "":
            print()
            print("Data entry error - car make must be entered...")
            print()
        elif set(CarMake).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - car make must be valid characters...")
            print()
        else:
            break

    #Gets Customers Car Model.
    while True:
        CarModel = input("Enter the car model (ie: Corolla): ").title()
        if CarModel == "":
            print()
            print("Data entry error - car model must be entered...")
            print()
        elif set(CarModel).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - car model must be valid characters...")
            print()
        else:
            break

    #Gets Customers Car year.
    while True:
        CarYear = input("Enter the car year (ie: 2018): ")
        if CarYear == "":
            print()
            print("Data entry error - car year must be entered...")
            print()
        elif set(CarYear).issubset(ALLOWED_NUMBER_CHARACTERS) == False:
            print()
            print("Data entry error - car year must be valid characters...")
            print()
        else:
            break

    #Gets Selling price of the car.
    while True:
        try:
            SellingPrice = input("Enter the car selling price (Cannot exceed $50,000): ")
            SellingPrice = float(SellingPrice)

        except:
            print()
            print("Data entry error - sales price must be a valid number...")
            print()
        else:
            if SellingPrice > 50000:
                print()
                print("Data entry error - sales price cannot exceed $50,000...")
                print()
            else:
                break

    #Gets Customers trade in amount.
    while True:
        try:
            TradeInAmount = input("Enter the amount of the trade in (Cannot exceed the selling price): ")
            TradeInAmount = float(TradeInAmount)

        except:
            print()
            print("Data entry error - trade in amount must be a valid number...")
            print()
        else:
            if TradeInAmount > SellingPrice:
                print()
                print("Data entry error - trade in amount cannot exceed the selling price...")
                print()
            else:
                break

    #Gets Sale persons name.
    while True:
        SalesPersonName = input("Enter the sales person name: ").title()
        if SalesPersonName == "":
            print()
            print("Data entry error - sales person name must be entered...")
            print()
        elif set(SalesPersonName).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - sales person name must be valid characters...")
            print()
        else:
            break

    # Perform required calculations.

    # Caculates the new selling price after the trade in amount is deducted.
    PriceAfterTrade = SellingPrice - TradeInAmount 

    # Calculates the transfer fee at 1% of the selling price
    TransferFee = SellingPrice * TRANSFER_FEE 

    # Determines Liensse fee based on selling price.
    if SellingPrice <= 15000:
        LicenseFee = STANDARD_RATE_LICENCE_FEE
    else:
        LicenseFee = OVER_PRICE_LICENCE_FEE

    #Determines if luxury tax is applied.
    LuxuryTax = 0
    if SellingPrice > 20000:
        LuxuryTax = SellingPrice * LUXURY_TAX

    # calculates total transfer fee wither luxury tax is added or not.
    TransferFeeUpdated =  TransferFee + LuxuryTax   

    # The Subtotal is the Price after trade plus the License Fee plus the Transfer Fee.
    Subtotal = PriceAfterTrade + LicenseFee + TransferFeeUpdated 
    
    # Calculates the taxs at 15% of the Subtotal.
    Tax = Subtotal * HST 
    
    # Calculates the total sales price.
    TotalSalesPrice = Subtotal + Tax 

    # Display results

    # Properly formats requried feilds.
    CustName = FirstName[0] + ". " + LastName
    PhoneNum = "(" + PhoneNumber[0:3] + ")" + " " + PhoneNumber[3:6] + "-" + PhoneNumber[6:10]
    CarDetails = CarYear + " " + CarMake + " " + CarModel

    InvoiceDateDsp = datetime.datetime.strftime(INVOICE_DATE, "%B %d, %Y")
    ReceiptID = FirstName[0] + LastName[0] + "-" + PlateNumber[3:6] + "-" + PhoneNumber[6:10]


    # First section of Invoice.
    print()
    print(f"Honest Harry Car Sales                       Invoice Date: {InvoiceDateDsp:>18s}")
    print(f"Used Car Sale and Receipt                    Receipt No:          {ReceiptID:>11s}")
    print()
    SellingPriceDsp = "${:,.2f}".format(SellingPrice)
    print(f"                                       Sale price:                 {SellingPriceDsp:>10s}")
    TradeInAmountDsp = "${:,.2f}".format(TradeInAmount)
    print(f"Sold to:                               Trade Allowance:            {TradeInAmountDsp:>10s}")
    print("                                       --------------------------------------")
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    print(f"     {CustName:<29s}     Price after Trade:          {PriceAfterTradeDsp:>10s}")
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    print(f"     {PhoneNum:<14s}                    License Fee:                {LicenseFeeDsp:>10s}")
    TransferFeeUpdatedDsp = "${:,.2f}".format(TransferFeeUpdated)
    print(f"                                       Transfer Fee:               {TransferFeeUpdatedDsp:>10s}")
    print("                                       --------------------------------------")
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    print(f"Car Details:                           Subtotal:                   {SubtotalDsp:>10s}")
    TaxDsp = "${:,.2f}".format(Tax)
    print(f"                                       HST:                        {TaxDsp:>10s}")
    print(f"     {CarDetails:<29s}     --------------------------------------")
    TotalSalesPriceDsp = "${:,.2f}".format(TotalSalesPrice)
    print(f"                                       Total sales prices:         {TotalSalesPriceDsp:>10s}")
    print()
    print(f"-----------------------------------------------------------------------------")
    print()
    print(f"                               Financing         Total          Monthly")
    print(f"     # Years      # Payments      Fee            Price          Payment")
    print(f"     ------------------------------------------------------------------")

    # Creates a loop for 1 - 4 years 
    for Years in range(1, 5): 

        # Calculates total months to get monthly payment.
        NumMonthlyPayments = Years * 12

        # Calculates finacing fee for said number of years. 
        FinancingFee = FINACING_FEE * Years

        # Calculates total price with finacing fee.
        TotalPrice = TotalSalesPrice + FinancingFee

        # Breaks total price down into the monthly payments.
        MonthlyPayment = TotalPrice / NumMonthlyPayments

        # Calculates the date of the first payment.
        FirstPayment = INVOICE_DATE + datetime.timedelta(days = 30)

        # Properly formats requried feilds.
        FinancingFeeDsp = "${:,.2f}".format(FinancingFee)
        MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)

        print(f"        {Years:>1d}             {NumMonthlyPayments:>2d}        {FinancingFeeDsp:>7s}        {TotalSalesPriceDsp:>10s}    {MonthlyPaymentDsp:>10s}")
    
    print(f"     ------------------------------------------------------------------")

    # Properly formats requried feilds.
    UpdatedInvoiceDateDsp = datetime.datetime.strftime(INVOICE_DATE, "%d-%b-%y").upper()
    FirstPaymentDsp = datetime.datetime.strftime(FirstPayment, "%d-%b-%y").upper()

    print(f"     Invoice date: {UpdatedInvoiceDateDsp:<9s}              First payment date: {FirstPaymentDsp:<9s}")
    print()
    print(f"---------------------------------------------------------------------------")
    print(f"                    Best used cars at the best prices!")
    print()

