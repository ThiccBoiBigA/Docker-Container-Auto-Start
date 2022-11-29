import psutil
import time
import os

programName = None
procList = []
i = None
x = 0
timeout = 300
dockerRunning = False
timer = 1

def iterateProcName():
    for proc in psutil.process_iter():
        procList.append(proc.name())

while i != "Docker Desktop.exe":
    iterateProcName()
    for i in procList:
        print(i)
        if i == "Docker Desktop.exe":
            print("Docker is starting.")
            time.sleep(1)
            print("Starting command line in 30 seconds.")

            while timer < 31:
                print(timer)
                timer += 1
                time.sleep(1)
            dockerRunning = True
            break
    if i != "Docker Desktop.exe":
        if x< timeout:
            print("Docker is not running. Trying again in 5 seconds.")
            x += 5
            time.sleep(5)
            print(x)
        else:
            print("Docker was not detected. Timed out after " + str(timeout) + " seconds.")
            break

if dockerRunning == True:
    print("Starting command line args")
    time.sleep(1)
    os.system('cmd /c "INSERT YOUR DOCKER RUN COMMANDS HERE SEPARATED BY & IF THERES MORE THAN ONE"')
