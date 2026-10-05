sec=int(input("enter the seconds"))
hours=int(sec/3600)
minute=int((sec%3600)/60)
sec=(sec%3600)%60652
print("hours=",hours,"minutes=",minute,"seconds=",sec)