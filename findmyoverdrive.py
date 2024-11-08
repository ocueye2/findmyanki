import asyncio
from bleak import BleakScanner
from overdrive import Overdrive

async def find_anki_overdrive_cars():

    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()

    anki_cars = []
    
    # find cars
    for device in devices:
        if "Drive" in device.name or "Anki" in device.name:
            anki_cars.append((device.name, device.address))
            print(f"Found Anki Overdrive car: Name={device.name}, MAC={device.address}")

    if not anki_cars:
        print("No Anki Overdrive cars found.")
    else:
        print()
        print("This program will now ping all cars it has found")
        print("type n if the car light does not change and y if it does")
        print("type y to continue")
            
        print()
        while not input() == "y":
            print("to reclarify")
            print("This program will now ping all cars it has found")
            print("type n if the car light does not change and y if it does")
            print("type y to continue")
        restart = True
        ans = ""
        for car in anki_cars:
            restart = True
            while restart == True:
                restart = False
                print(f"trying '{car[0]}'")
                tcar = Overdrive(str(car[1]))
                test = Overdrive.ping(tcar)
                tcar.disconnect()
                print("did your car light change? (y/n)")
                ans = input()
                if ans == "y":
                    print()
                    print(f"Your car is: {car[0]}")
                    print(f"mac: {car[1]}")
                    exit()
                elif ans == "n":
                    print("continuing")
                else:
                    restart = True
                    print("retrying car")
    print()
    print("could not find you car")
    print("make sure its on and working")

# Run the scanner
asyncio.run(find_anki_overdrive_cars())
