def den():
    from datetime import datetime,timedelta

    today=datetime.now()
    now3=today.weekday()
    if now3==0:
        print(today, " monday")
    elif now3==1:
        print(today, " tuesday")
    elif now3==2:
        print(today, "wednesday")
    elif now3==3:
        print(today, " thursday")
    elif now3==4:
        print(today, "friday")
    elif now3==5:
        print(today, " saturday")
    else:
        print(today, "sunday")
print(den())