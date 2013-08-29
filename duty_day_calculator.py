import pandas as pd
from datetime import datetime

def main():
    tr = pd.read_csv('Forest Service Report.csv',index_col='Tour Date',parse_dates=True)
    tr = tr.sort()
    enddate = datetime.now()
    tr = tr[startdate:enddate]
    tour_participants = tr['Patroller Names']
    tour_participants = tour_participants.str.split(", ")
    duty_days = {}
    for i in tour_participants:
        for j in i:
            if j in duty_days.keys():
                duty_days[j] = duty_days[j] + 1
            else:
                duty_days[j] = 1
    del duty_days['Other']
    duty_days_lst = duty_days.items()
    last_names = [i[0].split()[1] for i in duty_days_lst]
    first_names = [i[0].split()[0] for i in duty_days_lst]
    duty_days = [i[1] for i in duty_days_lst]
    duty_days_pd = pd.DataFrame({'Duty Days':duty_days,'First Name':first_names,'Last Name':last_names}).reindex(columns=['Last Name','First Name','Duty Days'])
    duty_days_pd.to_csv('duty_days.csv',index=False)
	
	
if __name__ == "__main__":
    try:
        year = raw_input("Enter starting year of the current season (i.e. for the 2012-2013 season enter 2012): ")
    except:
        year = 2012
    startdate = datetime(int(year),9,1,0,0)
    main()