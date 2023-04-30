from events import A_sensor_on
from events import V_sensor_on
from events import APACE
from events import VPACE


def process_LRLONLY(actual_time):
    print("This is LRLONLY state. Time is {}".format(actual_time))
    timer_expired = 100
    LRL_timer = 0
    while True:
        A_sensor = A_sensor_on(actual_time)
        if A_sensor == True:
            pstate = "AB"
            actual_time += 1
            print("A sensed. There is a P wave. Time is {}".format(actual_time))
            break
        V_sensor = V_sensor_on(actual_time)
        if V_sensor == True:
            pstate = "VB"
            actual_time += 1
            print("V sensed. There is a QRS complex. Time is {}".format(actual_time))
            break
        if LRL_timer == timer_expired:
            pstate = "APace"
            actual_time += 1
            print("LRL timer expired. Time is {}".format(actual_time))
            break
        LRL_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_APACE(actual_time):
    print("This is APACE state. Time is {}".format(actual_time))
    ECG, actual_time = APACE(actual_time)
    pstate = "AB"
    return pstate, actual_time, ECG


def process_AB(actual_time):
    print("This is AB state. Time is {}".format(actual_time))
    timer_expired = 5
    AB_timer = 0
    while True:
        if AB_timer == timer_expired:
            pstate = "ARP"
            actual_time += 1
            print("AB timer expired. Time is {}".format(actual_time))
            break
        AB_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_ARP(actual_time):
    print("This is ARP state. Time is {}".format(actual_time))
    timer_expired = 10
    ARP_timer = 0
    while True:
        if ARP_timer == timer_expired:
            pstate = "AVIONLY"
            actual_time += 1
            print("ARP timer expired. Time is {}".format(actual_time))
            break
        AB_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_AVIONLY(actual_time):
    print("This is AVIONLY state. Time is {}".format(actual_time))
    timer_expired = 2
    AVI_timer = 0
    while True:
        A_sensor = A_sensor_on(actual_time)
        if A_sensor == True:
            pstate = "AB"
            actual_time += 1
            print("A sensed. There is a P wave. Time is {}".format(actual_time))
            break
        V_sensor = V_sensor_on(actual_time)
        if V_sensor == True:
            pstate = "VB"
            actual_time += 1
            print("V sensed. There is a QRS complex. Time is {}".format(actual_time))
            break
        if AVI_timer == timer_expired:
            pstate = "VPace"
            actual_time += 1
            print("LRL timer expired. Time is {}".format(actual_time))
            break
        AVI_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_VPACE(actual_time):
    print("This is VPACE state. Time is {}".format(actual_time))
    ECG, actual_time = VPACE(actual_time)
    pstate = "VB"
    return pstate, actual_time, ECG


def process_VB(actual_time):
    print("This is VB state. Time is {}".format(actual_time))
    timer_expired = 5
    VB_timer = 0
    while True:
        if VB_timer == timer_expired:
            pstate = "VRP"
            actual_time += 1
            print("VB timer expired. Time is {}".format(actual_time))
            break
        VB_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_VRP(actual_time):
    print("This is VRP state. Time is {}".format(actual_time))
    timer_expired = 10
    VRP_timer = 0
    while True:
        if VRP_timer == timer_expired:
            pstate = "LRLONLY"
            actual_time += 1
            print("ARP timer expired. Time is {}".format(actual_time))
            break
        VRP_timer += 1
        actual_time += 1
    return pstate, actual_time


