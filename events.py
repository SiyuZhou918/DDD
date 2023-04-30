def A_sensor_on(actual_time, ECG):
    if ECG[actual_time] == 5:
        return True
    else:
        return False


def V_sensor_on(actual_time, ECG):
    if ECG[actual_time] == 20:
        return True
    else:
        return False

def APACE(actual_time, ECG):
    ECG[actual_time] = 5
    actual_time += 1
    return ECG, actual_time

def VPACE(actual_time, ECG):
    ECG[actual_time] = 20
    actual_time += 1
    return ECG, actual_time