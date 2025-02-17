# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2024.

import sys, csv, re

codes = [{"code":"G33z100","system":"readv2"},{"code":"Gyu6600","system":"readv2"},{"code":"Gyu6300","system":"readv2"},{"code":"G677300","system":"readv2"},{"code":"G677200","system":"readv2"},{"code":"G6X..00","system":"readv2"},{"code":"G677100","system":"readv2"},{"code":"G677000","system":"readv2"},{"code":"G677400","system":"readv2"},{"code":"G634.00","system":"readv2"},{"code":"G631.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-steno---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-steno---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-steno---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
