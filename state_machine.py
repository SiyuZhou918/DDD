from process import process_LRLONLY
import pandas as pd

# read the excel file into a dataframe
df = pd.read_excel('data.xlsx')

# extract the first column into a series
first_column = df.iloc[:, 0]

# convert the series into a list
first_column_list = first_column.tolist()

# print the first 5 values of the list
print(first_column_list[:5])


def input_data():


def DDD_pacemaker():
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
    DDD_pacemaker()
