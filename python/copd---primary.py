# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"10980.0","system":"readv2"},{"code":"1446.0","system":"readv2"},{"code":"106650.0","system":"readv2"},{"code":"21061.0","system":"readv2"},{"code":"99536.0","system":"readv2"},{"code":"10863.0","system":"readv2"},{"code":"40788.0","system":"readv2"},{"code":"63479.0","system":"readv2"},{"code":"12166.0","system":"readv2"},{"code":"794.0","system":"readv2"},{"code":"40159.0","system":"readv2"},{"code":"9876.0","system":"readv2"},{"code":"46578.0","system":"readv2"},{"code":"15157.0","system":"readv2"},{"code":"63216.0","system":"readv2"},{"code":"1001.0","system":"readv2"},{"code":"66058.0","system":"readv2"},{"code":"26306.0","system":"readv2"},{"code":"24248.0","system":"readv2"},{"code":"44525.0","system":"readv2"},{"code":"64721.0","system":"readv2"},{"code":"93568.0","system":"readv2"},{"code":"68662.0","system":"readv2"},{"code":"5710.0","system":"readv2"},{"code":"33450.0","system":"readv2"},{"code":"70787.0","system":"readv2"},{"code":"37247.0","system":"readv2"},{"code":"59263.0","system":"readv2"},{"code":"27819.0","system":"readv2"},{"code":"14798.0","system":"readv2"},{"code":"15626.0","system":"readv2"},{"code":"25603.0","system":"readv2"},{"code":"7884.0","system":"readv2"},{"code":"5798.0","system":"readv2"},{"code":"67040.0","system":"readv2"},{"code":"3243.0","system":"readv2"},{"code":"11150.0","system":"readv2"},{"code":"65733.0","system":"readv2"},{"code":"61513.0","system":"readv2"},{"code":"23492.0","system":"readv2"},{"code":"26125.0","system":"readv2"},{"code":"92955.0","system":"readv2"},{"code":"68066.0","system":"readv2"},{"code":"45089.0","system":"readv2"},{"code":"16410.0","system":"readv2"},{"code":"10802.0","system":"readv2"},{"code":"5909.0","system":"readv2"},{"code":"56860.0","system":"readv2"},{"code":"66043.0","system":"readv2"},{"code":"60188.0","system":"readv2"},{"code":"104608.0","system":"readv2"},{"code":"998.0","system":"readv2"},{"code":"61118.0","system":"readv2"},{"code":"37959.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["copd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["copd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["copd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
