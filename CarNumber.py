"""
Car Registration Program.
Enter your Car's Plate number and receive some details related to it.
"""
statesStr = "Andaman and Nicobar,Andhra Pradesh,Arunachal Pradesh,Assam,Bihar,Chandigarh,Dadra and Nagar Haveli,Daman and Diu,Delhi,Goa,Gujarat,Haryana,Himachal Pradesh,Jammu and Kashmir,Karnataka,Kerala,Lakshadweep,Madhya Pradesh,Maharashtra,Manipur,Meghalaya,Mizoram,Nagaland,Orissa,Pondicherry,Punjab,Rajasthan,Sikkim,Tamil Nadu,Tripura,Uttar Pradesh,West Bengal,"
regStr = "ANAPARASBRCHDNDDDLGAGJHRHPJKKAKLLDMPMHMNMLMZNLORPYPNRJSKTNTRUPWB" # Reg States as raw data.
regList = []
l = len(regStr)

for i in range(0,l,2): # Using a loop to append each reg state to a list. 
    temp = regStr[i:i+2]
    regList.append(temp)

i = 0
statesList = []
while statesStr != "": # Using a loop to append each state name to a list
    index = statesStr.find(',')
    temp = statesStr[i:index]
    statesList.append(temp)
    statesStr = statesStr.strip(temp)
    statesStr =  statesStr[1:]

LicensePlate = input("Enter the car license plate (Example : KA04MB1226) : ") # Taking the license plate as input.
LicensePlate =  LicensePlate.upper() # Converting to uppercase just in case someone enters in lowercase.
print("`"*25)
print("\tDetails")
print("`"*25)

state = LicensePlate[:2] # Extracting reg state from plate.
print("State :", end = " ")
# Printing State 
try:
    i = regList.index(state)
    print(statesList[i])
except:
    print("N/A (No such state)")

LicensePlate = LicensePlate[2:] # Slicing the state from plate.
rtonum = LicensePlate[:2] # Extracting RTO Number from plate.
print("RTO Number :",rtonum)

i = 0 # Keeping a counter to slice off rto series later.
rtoseries = ""
LicensePlate = LicensePlate[2:] # Slicing the rto number from plate.
for temp in LicensePlate: # Iterating through loop until a number is found.
    if temp.isdigit() == False:
        rtoseries += temp
        i += 1
print("RTO Series (Counter):",rtoseries)

LicensePlate = LicensePlate[i:] # Slicing the rto series from plate.
print("Unique Plate Number :",LicensePlate) # Directly printing the string as nothing else is left to slice.
print("`"*25)















