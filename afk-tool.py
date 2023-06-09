#   A SIMPLE AFK BOT TO MOVE YOUR MOVE AND CLICK RANDOMLY
#                   by Devin Foust
#
#                   LINUX VERSION


# Library import
import pyautogui as pyauto
import sys, os, random, time

# Title
os.system("clear")
print("\nPYTHON AUTO-CLICKER AFK TOOL")
print("     by Devin Foust")
print("\nEdit script as needed :)")
print("Press ctrl+C any time to exit")

# Settings input and variables
try:
    resx = int(input("\nResolution Width (x) > "))
    resy = int(input("\nResolution Height (y) > "))
    print("\nHow long to wait before starting the script?")
    waitInit = int(input("(In seconds) > "))
    print("\nHow long in-between mouse movements?")
    waitBetw = float(input("(In seconds) > "))
    print("\nWhat should the duration of the mouse movements be?")
    duration = float(input("(In seconds) > "))
    print("\nHow long to run the script for? > ")
    runTimeMin = input("(In minutes) > ")
    runTimeSec = float(runTimeMin)*60
    cycles = int((runTimeSec/(waitBetw+duration)))
    print("\nDo you want the mouse to click?")
    click = str.casefold(input("(Y/N) > "))
    
    # WAIT!
    for i in range(waitInit,0,-1):
        os.system("clear")
        print("\nScript will begin after",i,"seconds...")
        time.sleep(1)
        
    # ACTION!
    for i in range(0,cycles):
        os.system("clear")
        print("\nRUNNING SCRIPT")
        print("Time between movements:",waitBetw,"seconds")
        print("Movement duration:",duration,"seconds")
        print("Movements made:",i)
        print("\nPress ctrl+C to quit...")
        time.sleep(waitBetw)
        x = random.randint(0, (resx-1))    # The "-1" here is to account for the zero, which is counted as an integer in the resolution range
        y = random.randint (0, (resy-1))    # The "-1" here is to account for the zero
        pyauto.moveTo(x,y,duration)
        if click == "yes" or click == "y":
            pyauto.click(button="left")
        else:
            continue
            
# Ctrl+C Behavior
except KeyboardInterrupt:
    os.system("clear")
    print("\nClosing program...")
    time.sleep(1)
    print("\nBye!\n")
    sys.exit()

# FINISHED!
os.system("clear")
print("\nSCRIPT FINISHED!")
print("Ran",cycles,"cycles in",runTimeMin,"minutes.")
input("\nPress any key to exit...")
exit

