import playsound
import keyboard

deez = "deez.wav"
nuts = "nuts.wav"
ha = "ha.wav"
gotem = "get em.wav"

while 1:
    if keyboard.is_pressed("d"):
        playsound.playsound(deez, block = 0)
    if keyboard.is_pressed("n"):
        playsound.playsound(nuts, block = 0)
    if keyboard.is_pressed("h"):
        playsound.playsound(ha, block = 0)
    if keyboard.is_pressed("g"):
        playsound.playsound(gotem, block = 0)