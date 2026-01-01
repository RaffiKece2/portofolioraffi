import sys
from time import sleep

def print_lyric():
    lines = [
        ("The club isn't the best place to find a lover",0.090),
        ("So the bar is where I go",0.050),
        ("Me and my friends at the table doing shots",0.050),
        ("Drinking fast and then we talk slow",0.050),
        ("Come over and start up a conversation with just me",0.050),
        ("And trust me I'll give it a chance now",0.030),
        ("Take my hand, stop, put Van the Man on the jukebox",0.050),
        ("And then we start to dance, and now I'm singing like",0.050),
        ("Girl, you know I want your love",0.050),
        ("Your love was handmade for somebody like me",0.030),
        ("Come on now, follow my lead",0.050),
        ("I may be crazy, don't mind me",0.050),
        ("Say, boy,",0.030),
        (" let's not talk too much",0.050),
        ("Grab on my waist and put that body on me",0.050),
        ("Come on now, follow my lead",0.050),
        ("Come, come on now, follow my lead",0.030),
        ("I'm in love with the shape of you",0.050),
        ("We push and pull like a magnet do",0.050),
        ("Although my heart is falling too",0.050),
        ("I'm in love with your body",0.050),
        ("And last night you were in my room",0.050),
        ("And now my bedsheets smell like you",0.050),
        ("Every day discovering something brand new",0.050),
        ("I'm in love with your body",0.050)
    ]
    
    delays = [8,0.5,0.2,0.8,1,0.3,0.2,0.2,1,1,1,1,0.3,1,1,1,0.2,1,1,1,1,1,1,1,3]  
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="", flush=True)
            sleep(char_delay)  
        sleep(delays[i])  
        print("")  
        
print_lyric()
