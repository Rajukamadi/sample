import json
import csv

datapointsData=[]
with open('datapoints.json') as f: # reading data from json file
        data=json.load(f)
sel_datapoints_data=0
Time_start_index=11
Time_end_index=19
for data_DpointsLabel,data_DpointsLabelVal in data.items():  # data is a dictionary
        if sel_datapoints_data!=0:
                for dpoints_arr in data_DpointsLabelVal:  # data_DpointsLabelVal is a list
                        sel_Time_min=0
                        dpointsTimeMinVal=[]
                        for data_TimeMin,data_TimeMinVal in dpoints_arr.items():  # dpoints_arr is a dictionary which has Time-stamp, Minimum and Unit values
                                if sel_Time_min!=2:  # It allows only Time-stamps and minimum values
                                        if sel_Time_min==0: # It segregates Time-stamp and Minimum values
                                                # print(data_TimeMinVal[Time_start_index:Time_end_index])
                                                dpointsTimeMinVal.append(data_TimeMinVal[Time_start_index:Time_end_index]) #Time-stamps are appended to dpointsTimeMinVal list
                                        else:
                                                # print(data_TimeMinVal)
                                                dpointsTimeMinVal.append(data_TimeMinVal) #Minimum values are appended to dpointsTimeMinVal list
                                else:
                                        datapointsData.append(dpointsTimeMinVal) # dpointsTimeMinVal list is appended to datapointsData list
                                        sel_Time_min=0
                                        print(dpointsTimeMinVal)
                                sel_Time_min=sel_Time_min+1
        sel_datapoints_data=sel_datapoints_data+1
# this is added line



