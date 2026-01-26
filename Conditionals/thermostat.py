device_status ="offline"


if device_status == "Active":
    temperature = int(input("Enter the temperature of thermostat: "))
    if temperature > 35:
        print("High Temperature Alert!!")
else:
    print("The device is offline")