count = 0
Jan_prices = []
Dec_prices = []
space= "     "

gasprices = open("gas prices.txt")
print("*-- Press enter to continue--*")
print("----Gas Price----*")
input()

# Prints table of prices
for gas in gasprices:
    print(gas)
input()

# The first question
gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")

for x in range(2):
    for gas in gasprices:
        gas.split(",")
        # This if gets the columns of the prices
        if count == 0:
            Jan = gas[5:10]
            Dec = gas[49:]
        # This if puts the prices into a list except the month
        if x == 0 and gas[5:10] != Jan:
            Jan = gas[5:10]
            Jan_prices.append(gas[5:10])
            #print(Jan)
        # This if puts the prices for December into a list and take out the '\n'.
        if x == 0 and gas[49:] != Dec and count < 11:
            #if count == 12:
            #print(gas[49:])
            Dec = gas[71:77]
            Dec_prices.append(gas[71:77].replace("\n",""))
        #print(gas[5:10].strip("F\t"),space , Dec.strip())
        count+=1
print()
# This prints the prices of the months on each line.
print("December ", ", ".join(Dec_prices))
print("January ", ", ".join(Jan_prices))

# This function gets the years with the smalles prices. 
def the_less():
    year = ""
    years = 2009
    #ordered_years
    # Make sure it does go out of range
    for index in range(len(Dec_prices)):
        # Compare the to values in the list and count the years at the end
        if Dec_prices[index] < Jan_prices[index]:
            year+=(str(years))
            year+= ", "
            year.rstrip(", ")
        years+=1
    return year[:-2]
print()
print("1. Which years had the price of gas in December be less than the price in January?" )
input()
print("The prices in December were less than January prices during the years: "+the_less()+".")            
input()

# The second question

last = 0
count2=0
newcount = 0
year = 0
gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")

for gas in gasprices:
    if count2 > 0:
        newcount = 0
        # Gets each string on each line excluding the years
        for a in gas.split("\t"):
            if newcount != 0:
                # Compare the last value to the first value. 
                if float(a.strip("\n")) > float(last):
                    last = float(a.strip("\n"))
                    print(last)
                    #print(newcount, count2)
                    month = newcount
                    year = count2
            newcount+=1
    count2+=1

print()
print("2. Which month and year were gas prices the highest?")

input()
gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")

month_table = 0
countsec = 0
year_table = 1
highest_MY = ""
# Gets the month and years of the highest price
for gas in gasprices:
    # For Month
    if countsec == 0:
        for a in gas.split("\t"):
            if month_table == month:
                #print(bill, a.strip("\n"))
                highest_MY += a.strip("\n")
                countsec = 1
            month_table+=1
    if countsec == 1:
        # For Year
        month_table = 0
        for a in gas.split("\t"):
            if month_table == 0 and a != "Year":
                if year_table == year:
                    #print(jill,a)
                    highest_MY += " "
                    highest_MY += a
                year_table+=1
            month_table+=1
   
print("Gas prices were highest during", highest_MY + ".")
print()
# The third question

print("3. Which month and year do we see the highest percent decrease in gas prices.")
input()
gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")

original = float()
previous = float()
h_perc_d = float()
perc_d = float()
change = 0
month = 0 
year = 0
h_num_year = 0
h_num_month = 0
h_month = ""
h_year = ""
for gas in gasprices:
    month=0
    # Prints each string on the line
    for single in gas.split("\t"):
            # Take out the month and years to leave the gas prices
        dif = single
        #print(dif)
        # Take out anything except the prices, adds up the months and find the highest percentage decrease
        if single not in "JanFebMarAprMayJunJulAugSepOctNovDec\nYear20092010201120122013201420152016201720182019":
            original = float(single)
            # Check if previous number has a value in it
            if previous > 0:
                change = original - previous
                perc_d = ((change)/(previous)) * 100
            if  perc_d < h_perc_d:
                h_perc_d = perc_d
                h_num_year = year
                h_num_month = month
                #print(year,h_num_year)
            previous = float(single)
            month+=1
    year+=1
# This funtion take the numeric value from the year and finds the year from the table
def highest_dec_year():
    gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")
    count = 0
    Year = []
    for gas in gasprices:
        for five in gas.split("\t"):
            if "20" in five and "." not in five:
                Year.append(five)
                #print(five)
        count+=1
    if h_num_year in range(len(Year)):
        return Year[h_num_year-1]

# This funtion take the numerica value of the months and finds the month from the table. 
def highest_dec_month():
    gasprices = open("c:\\Users\Brandon\Documents\gas prices.txt")
    count3 = 0
    Month = []
    for gas in gasprices:
        for five in gas.split("\t"):
            if count3 == 0 and five != "Year":
                Month.append(five.strip("\n"))
                #print(count3,five)
        count3 +=1 
    return Month[h_num_month]

highest_dec_year()
highest_dec_month()

if h_perc_d < 0:
    print("The highest percentage decrease happened before and at the month of",highest_dec_month(),"in the year",highest_dec_year()+".") 
input()
