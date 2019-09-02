import time
import csv
import os
from datetime import datetime


def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("\n",""))

while True:
        current_temp=measure_temp()
        print(current_temp)
        today_date_string =  datetime.strftime(datetime.now(), '%d-%m-%Y')
        currentime=datetime.now()
        csvData = [[current_temp, currentime]]
        with open('data/'+today_date_string+'.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
                csvFile.close()
        # Log time every 5 minutes
        time.sleep(300)
