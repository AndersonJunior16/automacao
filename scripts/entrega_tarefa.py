import zipfile
import pyautogui as pa
import time
import os

pa.PAUSE = 2

caminho_para_edge = 'edge.png'

local_edge = pa.locateCenterOnScreen(caminho_para_edge, confidence=0.8)

pa.click(local_edge.x, local_edge.y)
zipfile