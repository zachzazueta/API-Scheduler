# API-Scheduler

I will be trying to create an API Scheduler to pull in Citibike station data over time - using this method to revisit my capstone project.

It looks like one way to do this will be to write a script in Python and then use Windows Task Scheduler to refresh the script daily.

To begin this project, I wrote out the following script; this is a call to the CitiBike station information API - when you call this API, a file with information about each station is returned. The goal is to query information about each station daily in 15 minute intervals from the hours of 8am to 8pm. Here is the code:

'''import pandas as pd 
import requests
import time
import datetime

starttime=time.time()
count=0
j = pd.DataFrame(columns=['station_id', 'num_bikes_available', 
                          'num_ebikes_available', 'num_bikes_disabled', 
                          'num_docks_available', 'num_docks_disabled', 
                          'is_installed', 'is_renting', 'is_returning', 
                          'last_reported', 'eightd_has_available_keys'])
while count<2:
    resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
    response = resp.json()
    for i in response['data']['stations']:
        currentDT = datetime.datetime.now()
        i['time_pulled'] = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        j = j.append(i, ignore_index=True)
    time.sleep(90.0 - ((time.time() - starttime) % 90.0))
    count+=1

stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
day = stamp
writer = pd.ExcelWriter('C:\Users\zazue\Data Science\Capstone\{}.xlsx'.format(stamp))
j.to_excel(writer, sheet_name=day)
writer.save()'''
