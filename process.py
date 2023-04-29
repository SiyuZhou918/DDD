from events import A_sensor_on
from events import V_sensor_on

def process_LRLONLY(actual_time):
    print("This is LRLONLY state.")
    timer_expired = 100
    LRL_timer = 0
    whil e(True):
        A_sensor = A_sensor_on(actual_time)
        if A_sensor == True:
            pstate = "AB"
            actual_time += 1
            print("A sensed. There is a P wave.")
            break
        V_sensor = V_sensor_on(actual_time)
        if V_sensor == True:
            pstate = "VB"
            actual_time += 1
            print("V sensed. There is a QRS complex.")
            break
        if LRL_timer == timer_expired:
            pstate = "APace"
            actual_time += 1
            print("LRL timer expired.")
            break
        LRL_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_APACE(actual_time):
    A_Pace()
    A_Pace_timer_on()