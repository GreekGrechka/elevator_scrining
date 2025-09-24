#      Шум (норма): 25-75 дБ       Вибрации (норма): 10–1000 Гц
from random import *
from time import *
from datetime import *
import aiofiles
import asyncio
async def generate_data(): 
    async with aiofiles.open('data/file_2.txt', 'a') as file:
        while True:
            sound = str(randint(20, 100))
            vibrations = str(randint(10, 1100))
            s = [sound, vibrations, str(time())]
            s = ' '.join(s)
            s += '\n'
            await file.write(s)
            await asyncio.sleep(1)
            


