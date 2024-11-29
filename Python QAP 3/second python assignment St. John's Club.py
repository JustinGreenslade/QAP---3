# Description: This program creates a receipt for the St. John's Marina & Yacht Club.
# Author: Justin Greenslade. 
# Class: Python SD 13.
# Dates: Sept 27 - Oct 6/ 2024 


#Assigned program constants
EVEN_SITE = 80.00 # Cost of even site number per month.
ODD_SITE = 120.00 # Cost of odd site number per month (More expensive due to the odd sites being larger).
ALT_MEMBER = 5.00 # Cost of alternate member per month.
SITE_CLEAN = 50.00 #Cost of weekly site cleaning per month.
VIDEO_SUR = 35.00 #Cost of video surveillance per month.
HST = .15 # Rate of 15% tax
STANDARD_MEMBER = 75.00 # Monthly due of a standard member.
EXECUTIVE_MEMBER = 150.00 # Monthly due of a executive member.
PROCESSING_FEE = 59.99 # The processing fee.
CANCEL_FEE = .60 # 60% of yearly site charges for cancellation charges.


#Gathered user input.
CurrentDate = input("Enter the current date (YYYY-MM-DD): ")
SiteNum = input("Enter the site number (1-100): ")
SiteNum = int(SiteNum) # Turns SiteNum into a integer.
print()
MemberName = input("Enter the member name: ")
StreetAdd = input("Enter the Customers street addresss: ")
City = input("Enter the Customers city: ")
Province = input("Enter the Customers province (NL): ").upper()# insures input will be a capaital.
PostalCode = input("Enter the Customers postal code (A1B2C3): ")
HomePhone = input("Enter the Customers home phone number (000)000-0000: ")
CellPhone = input("Enter the Customers cellphone number (000)000-0000): ")
print()
MemberType = input("Enter the Customers member type (S for Standard, E for Executive): ").upper()# insures input will be a capaital.
AltMembers = input("Enter the number of alternate members: ") # friends and family that will be allowed to access the grounds.
AltMembers = int(AltMembers) # Turns AltMembers into a integer.
SiteClean = input("Optional Weekly site cleaning service (Y for Yes, N for No): ").upper()# insures input will be a capaital.
Surveillance = input("Optional surveillance service (Y for Yes, N for No): ").upper()# insures input will be a capaital.
print()


# If statments.

# Determines if Site is odd or even 
SiteOption = SiteNum % 2 # reducsed site number to 0 or 1 based on if the number given is even or odd.

if SiteOption == 0: # Determines if site cost should be based on even or odd cost.
    SiteCost = EVEN_SITE
else:
    SiteCost = ODD_SITE

# Determins membership type and cost.
if MemberType == "S":
    MemberTypeMsg = "Standard"
    MonthDuesAmt = STANDARD_MEMBER
else:
    MemberTypeMsg = "Executive"
    MonthDuesAmt = EXECUTIVE_MEMBER

# Determines choice of site cleaning service.
if SiteClean == "Y":
    SiteCleanCost = SITE_CLEAN
    SiteCleanMsg = "Yes"
else:
    SiteCleanCost = 0.00
    SiteCleanMsg = "No"


# Determins choice of surveillance service.
if Surveillance == "Y":
    SurveillanceCost = VIDEO_SUR
    SurveillanceMsg = "Yes"
else:
    SurveillanceCost = 0.00
    SurveillanceMsg = "No"



# Calculations 

AltMembersCost = AltMembers * ALT_MEMBER # Calculates the total cost for the alternative members.
SiteCharges = SiteCost + AltMembersCost # Calculates the site charges 
ExtraCharges = SiteCleanCost + SurveillanceCost #Calculates the extra charges based on customers (Y/N) for both optional services.

SubTotal = SiteCharges + ExtraCharges # Calculates sub total 
Tax = SubTotal * HST # Calculates the amount of tax charged on the sub total (at 15%).
TotalMonthCharge = SubTotal + Tax # Calculates total monthly charge with tax

MonthDues = MonthDuesAmt # Gives the monthly due amount based on member type
TotalMonthFee = TotalMonthCharge + MonthDues # Calculates total monthly fee 
YearlyFee = TotalMonthFee * 12 # Calculates the yearly fee

MonthlyPayment = (YearlyFee + PROCESSING_FEE) / 12 # Calculates monthly payment
CancelFee = (SiteCharges*12) * CANCEL_FEE # # Calculates the cancellation fee ( 60 %)


#Print/Display all values.

print(f"   St. John's Marina & Yacht Club")
print(f"        Yearly Member Receipt")
print()
print(f"--------------------------------------")
print()
print(f"Client Name and Address:")
print()
print(f"{MemberName:<24s}")
print(f"{StreetAdd:<24s}")
print(f"{City:<15s},{Province:<2s} {PostalCode:<6s}")

print()

print(f"Phone: {HomePhone:<10s} (H)")
print(f"       {CellPhone:<10s} (C)")
print()
print(f"Site #:{SiteNum:>3d}   Member type:   {MemberTypeMsg:>9s}")
print()
print(f"Alternate members:                 {AltMembers:>2d}")
print(f"Weekly site cleaning:             {SiteCleanMsg:>3s}")
print(f"Video surveillance:               {SurveillanceMsg:>3s}")

print()

SiteChargesMsg = "${:,.2f}".format(SiteCharges)
print(f"Site charges:               {SiteChargesMsg:>9s}")
ExtraChargesMsg = "${:,.2f}".format(ExtraCharges)
print(f"Extra charges:                {ExtraChargesMsg:>7s}")
print(f"                            ----------")
SubTotalMsg = "${:,.2f}".format(SubTotal)
print(f"Subtotal:                   {SubTotalMsg:>9s}")
TaxMsg = "${:,.2f}".format(Tax)
print(f"Sales tax(HST):               {TaxMsg:>7s}")
print(f"                           -----------")
TotalMonthChargeMsg = "${:,.2f}".format(TotalMonthCharge)
print(f"Total monthly charges:      {TotalMonthChargeMsg:>9s}")
MonthDuesMsg = "${:,.2f}".format(MonthDues)
print(f"Monthly dues:                 {MonthDuesMsg:>7s}")
print(f"                           -----------")
TotalMonthFeeMsg = "${:,.2f}".format(TotalMonthFee)
print(f"Total monthly fees:         {TotalMonthFeeMsg:>9s}")
YearlyFeeMsg = "${:,.2f}".format(YearlyFee)
print(f"Total yearly fees:         {YearlyFeeMsg:>10s}")

print()

MonthlyPaymentMsg = "${:,.2f}".format(MonthlyPayment)
print(f"Monthly payment:            {MonthlyPaymentMsg:>9s}")

print()
print(f"--------------------------------------")
print()

print(f"Issued: {CurrentDate:<10s}")
print(f"HST Reg No: 549-33-5849-4720-9885")

print()

CancelFeeMsg = "${:,.2f}".format(CancelFee)
print(f"Cancellation fee:           {CancelFeeMsg:>9s}")
print()