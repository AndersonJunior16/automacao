import pyautogui as pa
import time
import os

pa.PAUSE = 1

edge = 'C:/Users/0220482413046/Documents/pedro/macro/automacao/img/teams.png'

local_edge = pa.locateCenterOnScreen(edge, confidence=0.8)

pa.click(local_edge.x, local_edge.y)


teams = 'C:/Users/0220482413046/Documents/pedro/macro/automacao/img/edge.png'

local_teams = pa.locateCenterOnScreen(teams, confidence=0.8)

pa.click(local_teams.x, local_teams.y)