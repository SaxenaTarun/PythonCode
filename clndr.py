
import calendar
def display(x):
    if(x==1):
        print("Monday")
    if(x==2):
        print("Tuesday")
    if(x==3):
        print("Wednesday")
    if(x==4):
        print("Thursday")
    if(x==5):
        print("Friday")
    if(x==6):
        print("Saturday")
    if(x==7):
        print("Sunday")        
    
year=int(input("Enter the Year"))
day=int(input("Enter the day of 1 January of the year"))
month_range=calendar.monthrange(year,day)
display(month_range[0])
