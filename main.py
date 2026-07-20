import cv2
import numpy as np
import mss
import pydirectinput as input
import keyboard
import time
import random


level = 2      # niveau de lenteur de 2 à 10, 3 est bien, 2 est le plus rapide, 1 est instable




input.FAILSAFE = False
input.PAUSE = 0
running = False
stop_program = False

def toggle():
    global running
    running = not running
    print("Bot ACTIVÉ" if running else "Bot EN PAUSE")

def stop():
    global stop_program
    stop_program = True
    print("Arrêt du programme...")

keyboard.add_hotkey("x", toggle)
keyboard.add_hotkey("c", stop)

def get_targets(mask, min_area=5000, single_target_area=20000):
    kernel = np.ones((15, 15), np.uint8)
    closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    targets = []

    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(c)

        # combien de cibles sont probablement fusionnées dans ce blob ?
        n = max(1, round(area / single_target_area))

        if n == 1:
            targets.append((x + w // 2 , y + h // 2 ))
        else:
                cx = x + w // 2  + random.choice([-60,60])
                cy = y + h // 2  + random.choice([-60,60])
                targets.append((cx, cy))

    return targets

def move_smooth(dx, dy, steps=level):
    step_x = int(dx/steps)
    step_y = int(dy/steps)
    for _ in range(steps):
        input.moveRel(int(step_x), int(step_y))
        time.sleep(0.01)
    input.moveRel(dx - (step_x * steps), dy - (step_y * steps))



def main():
    global running, stop_program
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        while running == False:
            time.sleep(0.01)
        

        while stop_program == False:
            if running:
                img = np.array(sct.grab(monitor))
                hsv = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
                lower = np.array([5, 130, 130])
                upper = np.array([30, 255, 255])
                mask = cv2.inRange(hsv, lower, upper)

                targets = get_targets(mask)
                if targets !=[] :
                    close_target = targets[0]
                    for t in targets:
                        if (t[0]-1920//2)**2 + (t[1]-1080//2)**2 < (close_target[0]-1920//2)**2 + (close_target[1]-1080//2)**2:
                            close_target = t
                    move_smooth(close_target[0]-1920//2 , close_target[1]-1080//2 )
                    input.click()
                    time.sleep(0.03)
                    targets=[]
                    img = np.array(0)
                else:
                    img = np.array(0)

    print("Programme arrêté.")

if __name__ == "__main__":
    main()