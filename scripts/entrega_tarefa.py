import pyautogui as pa
import time
import os

pa.PAUSE = 2

edge = 'edge.png'

local_edge = pa.locateCenterOnScreen(edge, confidence=0.8)

pa.click(local_edge.x, local_edge.y)


teams = 'teams.png'

local_teams = pa.locateCenterOnScreen(teams, confidence=0.8)

pa.click(local_teams.x, local_teams.y)

hahahaha