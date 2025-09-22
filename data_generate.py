#      Шум (норма): 25-75 дБ       Вибрации (норма): 10–1000 Гц
from random import *
from time import *
from datetime import *
with open('data/file_2.txt', 'w') as file:
    for i in range(10):
        now = datetime.now()
        now = now.strftime("%d.%m.%Y %H:%M:%S")
        sound = str(randint(20, 100))
        vibrations = str(randint(10, 1100))
        s = [sound, vibrations, now]
        s = ' '.join(s)
        s += '\n'
        file.write(s)
        sleep(1)