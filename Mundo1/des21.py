# desafio 21: tocando um mp3. // 10 segundos é o tempo que a canção irá tocar.

from pygame import mixer
import time
mixer.init()
mixer.music.load('song1.mp3')
mixer.music.play()
time.sleep(10)

