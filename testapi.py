import pandas as pd 
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
writer.save()