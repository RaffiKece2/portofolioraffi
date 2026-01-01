import random

data_karakter = {
    
    "phoenix": {"api": 20, "wall": 15, "flash": 1 , "regen": 90},
    "yoru": {"teleport": 20, "flash" : 2, "clone": 10, "invicible": 65},
    "skye": {"detection": 1, "flash": 2, "heal_area" : 10, "target": 90},
    "vyse": {"flash": 1, "trap": 50, "wall": 2, "lock_weapon": 99}
    
}

class Player:
    def __init__(self,nama,skill):
        self.nama = nama
        self.skill = skill
        self.nyawa = 100
    
    def interaksi(self,objek):
        if objek is None:
            print("tidak ada objek")
        else:
            print(objek)

    
    def menyerang(self,musuh,damage):
        kuras_nyawa = damage
        if musuh.nyawa > 0:
            musuh.nyawa -= kuras_nyawa
            print(f"sisah nyawa musuh: {musuh.nyawa}")
        else:
            
            
        


class Game:
    def __init__(self):
        self.player = None
        self.enemy = None
        
  
        
        
        





