import threading
def des():
    print("nothing")
t= threading.Thread(target=des,daemon=True)
t.start
print(isinstance(t,threading.Thread))