import time
while True:
    print("How old are you in seconds? Let's Find out! ")
    time.sleep(2)
    years = float(input("How old are you? "))
    months = float(input("How many more months until your birthday? "))
    days = float(input("How many more days until your birth date? "))
    hours = float(input("How many more hours until midnight? "))
    minutes = float(input("How many minutes until the next hour? "))
    seconds = float(input("How many seconds until the current minute is over? "))
    runningtotal = years * 365.25 * 24 * 3600
    runningtotal = runningtotal + (months * 30.42 * 24 * 3600)
    runningtotal = runningtotal + (days * 24 *3600)
    runningtotal = runningtotal + (hours * 3600)
    runningtotal = runningtotal + (minutes * 60)
    runningtotal = runningtotal + (seconds)
    runningtotal = int(runningtotal)
    print("calculating...")
    time.sleep(2.5)
    print("You are",runningtotal,"seconds old! (roughly)")
    time.sleep(2)
    

    

