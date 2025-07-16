import time
import os
import subprocess
from datetime import datetime

BLOCK_DURATION = 3 * 60 * 60  # 3 hours
BLOCKED_PROCESSES = [
    "LeagueClient.exe",
    "LeagueClientUx.exe",
    "League of Legends.exe",
]

def is_weekend():
    # 5 = Saturday, 6 = Sunday
    return datetime.now().weekday() >= 5

def is_after_6pm():
    return datetime.now().hour >= 18

def show_parrot():
    # Launch Windows Terminal (`wt`) with UTF-8 code page and emoji support
    command = (
        'wt -w 0 nt --title "League Blocked" cmd /k "chcp 65001 >nul && '
        'echo ----------------------------------------- && '
        'echo  🚫 LEAGUE IS BLOCKED. DO SOMETHING PRODUCTIVE. 💪 && '
        'echo ----------------------------------------- && '
        'timeout /t 2 >nul && '
        'curl parrot.live"'
    )
    subprocess.Popen(command, shell=True)


print("HELLO - League blocking system started.")
startTime = time.time()

while True:
    now = datetime.now()
    elapsedTime = time.time() - startTime

    # Stop if 3 hours passed
    if elapsedTime > BLOCK_DURATION:
        print("3 hours passed. You can now play League 🎮.")
        break

    # Stop if it's the weekend or after 6 PM
    if is_weekend():
        print("It's the weekend 🎉. League is not blocked.")
        break
    if is_after_6pm():
        print("It's after 6:00 PM ⏰. League is no longer blocked.")
        break

    for process in BLOCKED_PROCESSES:
        result = os.system(f'taskkill /f /im "{process}" >nul 2>&1')
        if result == 0:
            show_parrot()

    time.sleep(5)
