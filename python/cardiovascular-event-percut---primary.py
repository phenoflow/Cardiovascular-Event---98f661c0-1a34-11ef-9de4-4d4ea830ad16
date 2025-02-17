# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2024.

import sys, csv, re

codes = [{"code":"7A44000","system":"readv2"},{"code":"7A4B900","system":"readv2"},{"code":"7A4B400","system":"readv2"},{"code":"7A4B300","system":"readv2"},{"code":"7A44400","system":"readv2"},{"code":"7A4B000","system":"readv2"},{"code":"7A4B200","system":"readv2"},{"code":"7A28500","system":"readv2"},{"code":"7A25600","system":"readv2"},{"code":"7A4B500","system":"readv2"},{"code":"7A28200","system":"readv2"},{"code":"7A44100","system":"readv2"},{"code":"7A4B100","system":"readv2"},{"code":"7A22300","system":"readv2"},{"code":"7A22000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-percut---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-percut---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-percut---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
