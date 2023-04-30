from process import process_LRLONLY
from process import process_APACE
from process import process_AB
from process import process_ARP
from process import process_AVIONLY
from process import process_VPACE
from process import process_VB
from process import process_VRP
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os


def input_data(filaname):
    df = pd.read_excel(filaname)
    second_column = df.iloc[:, 1]
    second_column_list = second_column.tolist()
    second_column_list[0]=5
    print(second_column_list)
    return second_column_list


def DDD_pacemaker(filename):
    ECG_list = input_data(filename)
    actual_time = 0
    pstate = "LRLONLY"
    while True:
        if pstate == "LRLONLY":
            pstate, actual_time = process_LRLONLY(actual_time, ECG_list)
        elif pstate == "APACE":
            pstate, actual_time, ECG = process_APACE(actual_time, ECG_list)
        elif pstate == "AB":
            pstate, actual_time = process_AB(actual_time)
        elif pstate == "ARP":
            pstate, actual_time = process_ARP(actual_time)
        elif pstate == "AVIONLY":
            pstate, actual_time = process_AVIONLY(actual_time, ECG_list)
        elif pstate == "VPACE":
            pstate, actual_time, ECG = process_VPACE(actual_time, ECG_list)
        elif pstate == "VB":
            pstate, actual_time = process_VB(actual_time)
        elif pstate == "VRP":
            pstate, actual_time = process_VRP(actual_time)
        else:
            print("Illegal state\n")
        if actual_time == 100:
            break
    print("End")


if __name__ == '__main__':
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askopenfilename()
    # filename = os.path.basename(file_path)
    filename = 'ecg_1st_heart_block.xlsx'
    DDD_pacemaker(filename)
