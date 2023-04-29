from process import process_LRLONLY
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os


def input_data(filaname):
    df = pd.read_excel('data.xlsx')
    second_column = df.iloc[:, 1]
    second_column_list = first_column.tolist()
    return second_column_list


def DDD_pacemaker(filename):
    ECG_list = input_data(filename)
    actual_time = 0
    pstate = "LRLONLY"
    while True:
        if pstate == "LRLONLY":
            pstate, actual_time = process_LRLONLY(actual_time)
        elif pstate == "APACE":
            pstate, actual_time = process_APACE(actual_time)
        elif pstate == "AB":
            pstate, actual_time = process_AB(actual_time)
        elif pstate == "ARP":
            pstate, actual_time = process_ARP(actual_time)
        elif pstate == "AVIONLY":
            pstate, actual_time = process_AVIONLY(actual_time)
        elif pstate == "VPACE":
            pstate, actual_time = process_VPACE(actual_time)
        elif pstate == "VB":
            pstate, actual_time = process_VB(actual_time)
        elif pstate == "VRP":
            pstate, actual_time = process_VRPE(actual_time)
        else:
            print("Illegal state\n")
        actual_time += 1
        if actual_time == 100:
            break
    print("End")


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    filename = os.path.basename(file_path)
    # 'data.xlsx'
    DDD_pacemaker()