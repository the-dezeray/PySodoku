from gui.app import start_application

#Start Game

try:
    start_application()
except KeyboardInterrupt:
    print("Game closed : forced exit")