import sys
from time import sleep


def lirik_lagu():
    lines = [
        ("Sakit dadaku,kumulai terseduh",0.1),
        ("Kubayangkan dosa-dosa semua dan khilafku raffi bot",0.04),
        ("Dimalam yang syahdu",0.07),
        ("Kuambilkan wudhu'ku",0.07),
        ("Tundukan wajahku",0.05),
        ("Memohon ampunan mu",0.05),
        ("Astaghfirullah,maafkan ya Allah",0.1),
        ("Ku tak mampu sendiri,tanpamu ilahi raffi bot",0.1),
        ("Ampunilah daku, seluas Rahmat mu",0.1)
        
    ]


    delays = [0.7,0.5,0.5,0.7,0.5,0.8,0.2,0.2,0.2]
    
    for i, (line,char_delay) in enumerate(lines):
        for char in line:
            print(char,end = "")
            sys.stdout.flush()
            sleep(char_delay)
            
        sleep(delays[i])
        print('')
        

lirik_lagu()