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
