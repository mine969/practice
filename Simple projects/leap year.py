def checkyear(year):
    if (year%4==0 and year%100 !=0 )or year %400==0:
        print("It's Leap Year")
    else :
        (print("Not a leap year"))
        

#mock data
year=int(input("Input to check Check Leap Year"))
checkyear(year)