convert_from = input("Enter Starting Unit of Measurement(inches, feet, yards):")

convert_to = input("Enter Unit of Measurement to Convert to(inches, feet, yards):")

number_of_inches = input("Enter Starting Measurment in Inches:")

number_of_Yards = input("Enter Starting Measurment in Yards:")

number_of_Feet= input("Enter Starting Measurment in Feet:")

number_of_Miles= input("Enter Starting Measurment in Miles:")

number_of_Meters= input("Enter Starting Measurment in Meters:")

number_of_KiloMeters= input("Enter Starting Measurment in KiloMeters:")

number_of_CentiMeters= input("Enter Starting Measurment in CentiMeters:")

number_of_MilliMeter= input("Enter Starting Measurment in MilliMeter:")

number_of_MicroMeter= input("Enter Starting Measurment in MicroMeter:")

number_of_NanoMeter= input("Enter Starting Measurment in NanoMeter:")

convert_from = input("Enter Starting Unit of Measurement(inches, feet, yards):")

convert_to = input("Enter Unit of Measurement to Convert to(inches, feet, yards):")

if convert_from.lower() in["inches","in","inch"]:
    number_of_inches = int(input("Enter Starting Measurment in Inches:"))
    if convert_to.lower() in ["feet","foot","ft"]:
        print("Result: " + str(number_of_inches)+ " Inches = " + str(round(number_of_inches / 12,2 )) + " Feet")
    elif convert_to.lower() in ["yards","yard","yds","yd","yrds","yrd"]:
        print("Result: " + str(number_of_inches)+ " Inches = " + str(round(number_of_inches / 36,2 )) + " Yards" )
    else:
        print("Please Enter either Inches, Feet, or Yards")
        
elif convert_from.lower() in ["feet","foot","ft"]:
    number_of_Feet = int(input("Enter Starting Measurment in Feet:"))
    if convert_to.lower() in["inches","in","inch"]:
        print("Result: " + str(number_of_Feet)+ " Feet = " + str(round(number_of_Feet * 12 )) + " Inches")
    elif convert_to.lower() in ["yards","yard","yds","yd","yrds","yrd"]:
        print("Result: " + str(number_of_Feet)+ " Feet = " + str(round(number_of_Feet / 3,2 )) + " Yards")
    else:
        print("Please Enter either Inches, Feet, or Yards")

elif convert_from.lower() in ["yards","yard","yds","yd","yrds","yrd"]:
    number_of_Yards = int(input("Enter Starting Measurment in Yards:"))
    if convert_to.lower() in["inches","in","inch"]:
         print("Result: " + str(number_of_Yards)+ " Yards = " + str(round(number_of_Yards * 36 )) + " Inches")
    elif convert_to.lower() in ["feet","foot","ft"]:
        Print("Result: " + str(number_of_Yards)+ " Yards = " + str(round(number_of_Yards * 3 )) + " Feet")
    else:
        print("Please Enter either Inches, Feet, or Yards")

else: 
    print("Please Enter either Inches, Feet, or Yards.")
    