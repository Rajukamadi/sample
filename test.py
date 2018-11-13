import json
import csv
datapointsData=[]
with open('datapoints.json') as f: # reading data from json file
        data=json.load(f)
        
data_DpointsVal=data['Datapoints']
for dpoints_arr in data_DpointsVal:  # data_DpointsLabelVal is a list
        dpointsTimeMinVal=[]
        for data_TimeMin,data_TimeMinVal in dpoints_arr.items():  # dpoints_arr is a dictionary which has Time-stamp, Minimum and Unit values
                if data_TimeMin!='Unit':  # It allows only Time-stamps and minimum values
                        if data_TimeMin=='Timestamp': # It segregates Time-stamp and Minimum values
                                dpointsTimeMinVal.append(data_TimeMinVal[data_TimeMinVal.find('T'):data_TimeMinVal.find('Z')]) #Time-stamps are appended to dpointsTimeMinVal list
                        else:
                                dpointsTimeMinVal.append(data_TimeMinVal) #Minimum values are appended to dpointsTimeMinVal list
                else:
                        datapointsData.append(dpointsTimeMinVal) # dpointsTimeMinVal list is appended to datapointsData list
                        print(dpointsTimeMinVal)



