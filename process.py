from events import A_sensor_on
from events import V_sensor_on
from events import APACE
from events import VPACE


def process_LRLONLY(actual_time, ECG):
    print("This is LRLONLY state. Time is {}".format(actual_time))
    timer_expired = 100
    LRL_timer = 0
    while True:
        A_sensor = A_sensor_on(actual_time, ECG)
        if A_sensor == True:
            pstate = "AB"
            print("A sensed. There is a P wave. Time is {}".format(actual_time))
            actual_time += 1
            break
        V_sensor = V_sensor_on(actual_time, ECG)
        if V_sensor == True:
            pstate = "VB"
            print("V sensed. There is a QRS complex. Time is {}".format(actual_time))
            actual_time += 1
            break
        if LRL_timer == timer_expired:
            pstate = "VPACE"
            print("LRL timer expired. Time is {}".format(actual_time))
            actual_time += 1
            break
        LRL_timer += 1
        actual_time += 1
        if actual_time == 113:
            print(ECG)
    return pstate, actual_time


def process_VPACE(actual_time, ECG):
    print("This is VPACE state. Time is {}. Pace ventricular here.".format(actual_time))
    ECG, actual_time = VPACE(actual_time, ECG)
    pstate = "VB"
    actual_time += 1
    return pstate, actual_time, ECG


def process_VB(actual_time):
    print("This is VB state. Time is {}".format(actual_time))
    timer_expired = 5
    VB_timer = 0
    while True:
        if VB_timer == timer_expired:
            pstate = "VRP"
            print("VB timer expired. Time is {}".format(actual_time))
            actual_time += 1
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
            pstate = "VAIONLY"
            print("ARP timer expired. Time is {}".format(actual_time))
            actual_time += 1
            break
        VRP_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_VAIONLY(actual_time, ECG):
    print("This is VAIONLY state. Time is {}".format(actual_time))
    timer_expired = 42
    AVI_timer = 0
    while True:
        A_sensor = A_sensor_on(actual_time, ECG)
        if A_sensor == True:
            pstate = "AB"
            print("A sensed. There is a P wave. Time is {}".format(actual_time))
            actual_time += 1
            break
        V_sensor = V_sensor_on(actual_time, ECG)
        if V_sensor == True:
            pstate = "VB"
            print("V sensed. There is a QRS complex. Time is {}".format(actual_time))
            actual_time += 1
            break
        if AVI_timer == timer_expired:
            pstate = "APACE"
            print("VAI timer expired. Time is {}".format(actual_time))
            actual_time += 1
            break
        AVI_timer += 1
        actual_time += 1
    return pstate, actual_time


def process_APACE(actual_time, ECG):
    print("This is APACE state. Time is {}. Pace atrium here.".format(actual_time))
    ECG, actual_time = APACE(actual_time, ECG)
    pstate = "AB"
    actual_time += 1
    return pstate, actual_time, ECG


def process_AB(actual_time):
    print("This is AB state. Time is {}".format(actual_time))
    timer_expired = 5
    AB_timer = 0
    while True:
        if AB_timer == timer_expired:
            pstate = "ARP"
            print("AB timer expired. Time is {}".format(actual_time))
            actual_time += 1
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
            pstate = "LRLONLY"
            print("ARP timer expired. Time is {}".format(actual_time))
            actual_time += 1
            break
        ARP_timer += 1
        actual_time += 1
    return pstate, actual_time