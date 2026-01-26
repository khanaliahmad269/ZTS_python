seat_type=input("Enter the Seat Type(AC/Sleeper/Economy/BusinessClass): ").lower()

match seat_type:
    case "ac":
        print("This train will contain AC")
    case "sleeper":
        print("This train berth")
    case "economy":
        print("This is the cheapest option available")
    case "businessclass":
        print("This is the most premium option")
    case _ :
        print("Invalid seat type")
    