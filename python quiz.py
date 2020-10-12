import pandas as pd 

file_object= open('Holiday_Schedule_Ranking_2019.csv','r')

data= pd.read_csv(file_object, index_col=0).T

file_object.close()

file_object= open('Holiday_Schedule_Ranking_2019.csv', 'r')

schedule= pd.read_csv(file_object, index_col=0)

for c in schedule.columns:
    schedule[c].values[:]=0

#print(schedule) 


data["col_sum"]= data.apply(lambda x:x.sum(), axis=1)

#print(data)

data= data.sort_values (by="col_sum", ascending=False)

data= data.T

#print(data)

for date in data.columns:
    date_series= data[date].nsmallest(5,keep='all')
    slot_count= 0
    date.loc['11/27/2019'].sort_values(ascending=False)
    #pd.DataFrame.index()
    #data.sort_values(by='date')
    #data.iloc[3]
    #print(date)
    print(date_series)
    if data.append >=2 or date.append ==3:
        break

    #if date_series ==3: 
      #break

#schedule.replace(0,'',inplace= True)
#schedule.to_csv('final_schedule.csv')
#print('done')