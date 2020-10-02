
year=int(input("Enter Year:"))
day=int(input("Enter Day: 1:Monday,2:Tuesday,3:Wednesday,4:Thursday,5:Friday,6:Saturday,7:Sunday:"))
day-=1
days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
m=12
for month in range(1,m+1):
    if month==1:
        print("1 January",year,"is",days[day])
    if month==2:
        day+=31
        day%=7
        print("1 February",year,"is",days[day])
    if month==3:
        if ((year%400==0) or ((year%4==0)and(year%100!= 0))):
            day+=29
            day%=7
        else:
            day+=28
            day%=7
        print("1 March",year,"is",days[day])
    if month==4:
        day+=31
        day%=7
        print("1 April",year,"is",days[day])
    if month==5:
        day+=30
        day%=7
        print("1 May",year,"is",days[day])
    if month==6:
        day+=31
        day%=7
        print("1 June",year,"is",days[day])
    if month==7:
        day+=30
        day%=7
        print("1 July",year,"is",days[day])
    if month==8:
        day+=31
        day%=7
        print("1 August",year,"is",days[day])
    if month==9:
        day+=31
        day%=7
        print("1 September",year,"is",days[day])
    if month==10:
        day+=30
        day%=7
        print("1 October",year,"is",days[day])
    if month==11:
        day+=31
        day%=7
        print("1 November",year,"is",days[day])
    if month==12:
        day+=30
        day%=7
        print("1 December",year,"is",days[day])
