#!/usr/bin/python
import os, re, sys, subprocess
from os.path import exists
import tix
import csv

def main():
    print("main function")
    cmd = "rm -r temp_tix"
    subprocess.call(cmd, shell=True)
    cmd = "mkdir temp_tix"
    subprocess.call(cmd, shell=True)

    with open("test_input.csv", "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            print("ROW", row)
            print(row['home'])
            time = row['time']
            date = row['date']
            home_team = row['home']
            opponent = row['opponent']
            section = row['section']
            row_num = row['row']
            seat = row['seat']
            entry = row['entry']
            path = "temp_tix/" + row['section'] + "-" + row['row'] + "-" + row['seat'] + ".jpeg"
            tix.bruins(time, date, opponent, section, row_num, seat, entry, path)

if __name__ == "__main__":
    import os, re, sys, subprocess
    import tix
    main()