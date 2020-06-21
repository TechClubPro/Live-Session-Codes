month = input("Enter the Month: ")

if month in ("Jan", "Mar","May","Jul","Aug","Oct","Dec"):
    print("31 Days")
    
elif month=="Feb":
    print("28/29 Days")
    
else:
    print("30 days")
