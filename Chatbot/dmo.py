from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
from comtypes import CLSCTX_ALL

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = interface.QueryInterface(IAudioEndpointVolume)


while True:
    input_one = float(input(": "))
    new_volume = min(input_one,1.0)
    volume.SetMasterVolumeLevelScalar(new_volume,None)
    result = (f"Volume New: {new_volume * 100:.2f}%")
    
    if not (0.0 <= input_one <= 1.0):
        print("Maaf Itu terlalu berlebihan!!!!")
    elif new_volume:
        print(result)
    
    
    