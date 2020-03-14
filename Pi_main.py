import msvcrt
import requests
from bs4 import BeautifulSoup
import time
import msvcrt
import  os
import json

if os.path.isfile('statistic.json')!=True:
    raw_data  = '{"record":0, "total_time": 0, "total_tries":0, "total_average":0, "games": 0}'

    data = json.loads(raw_data)
    print (type(data))

    with open ('statistic.json','w') as outfile:
        json.dump(data,outfile, ensure_ascii=False)
        print ('creating file')

else:
    with open('statistic.json','r') as json_file:
        data = json.load(json_file)
        print (data)



def get_PI():
    req= requests.get('http://mathshistory.st-andrews.ac.uk/HistTopics/1000_places.html')
    soup = BeautifulSoup(req.text, 'html.parser')
    pi = soup.select('pre')[0].text
    pi = pi.splitlines()
    pi = "".join(pi)
    pi = pi.rstrip('\n')
    pi = pi.replace(" ", "")
    return (pi)

pi =  get_PI()

while True:
    display=True
    # variables set
    i = 0
    time_sum=0
    total_time = time.time()
    old_time = total_time
    while True:
        new_time  = time.time()
        if i>0:
            time_sum +=new_time-old_time

        old_time = new_time
        key = msvcrt.getch()



        if key==b'\x1b' or key==b'\r':
            display=False
            break


        key = key.decode('utf-8')

        if key==pi[i]:
            pass
        else:
            print ("WRONG")
            break

        print (key, end=' ')
        i+=1

    total_time =  time.time() -total_time
    time_sum = round(time_sum,4)
    data['total_tries']+=1

    print ('')

    if i>data['record']:
        data["record"] = i


        print (f'~new record~')



    if i!=0:
        average = time_sum/i
        data['total_average']=data['total_average']+average

    else:
        average= 0
    if average!=0:
        print(f"good job! \nyou know:{i} numbers!\nnext numbers:{pi[i:i + 3]}\n typing speed average:{round(average,3)} \n total time:{round(total_time,2)} \n")

    with open('statistic.json', 'w') as outfile:
        json.dump(data, outfile)


    total_average = data['total_average']/data['total_tries']
    if  average!=0:
        print (f"typing speed average of all time (per digits): {round(total_average,3)}\n your record is : {data['record']}")
