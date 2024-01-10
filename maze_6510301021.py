import time
import random

def move_forward():
    print("Moving forward")

def turn_left():
    print("Turning left")

def turn_right():
    print("Turning right")

def stop():
    print("Stopping")

def is_obstacle_detected():
    # ตัวอย่าง: สร้างการตรวจจับขอบเขตสุ่ม
    return random.choice([True, False])

def walk_out_of_maze():
    while True:
        # เคลื่อนที่ไปข้างหน้า
        move_forward()
        time.sleep(1)  # พัก 1 วินาที

        # ตรวจจับขอบเขตหรืออุปสรรค
        if is_obstacle_detected():
            # หากตรวจจับขอบเขต หรืออุปสรรค ให้หยุด
            stop()
            # สุ่มเลือกทิศทางเพื่อหัน
            if random.choice([True, False]):
                turn_left()
            else:
                turn_right()
            time.sleep(1)  # พัก 1 วินาที

# เรียกใช้งานฟังก์ชันสำหรับการเดินออกจากเขาวงกต
walk_out_of_maze()
