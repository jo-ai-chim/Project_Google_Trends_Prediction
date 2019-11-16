from pytrends.request import TrendReq
from time import sleep
import numpy as np
import pandas as pd
import datetime


def create_google_trend_df(kw_list, start_year = 2004):
    '''
    INPUT:
    kw_list - a list of search terms 
    start_year - the year (as integer) from where on the google trend results should be exported

    OUTPUT:
    google_trends_df - dataframe with one column for each term in the kw_list and all one line for every date in one if the terms has a value in google trends
   
    This function calls google trends several times to extract and merges the results to one dataframe
    '''
    # Login to Google. Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,25), retries=2, backoff_factor=0.1)
    
    #Loop to add each word to the dataframe used for the model 
    year = datetime.date.today().year
    counter = year - start_year
    creation_counter_word = 0
    for word in kw_list:
        #loop to iterate over time within so that we get an value for every day
        creation_counter_date = 0
        for i in range(counter + 1):
            #create the strings for the two timeslots
            time_slot_1 = str(start_year + i) + '-01-01 ' + str(start_year + i) + '-06-30'
            time_slot_2 = str(start_year + i) + '-07-01 ' + str(start_year + i) + '-12-31'
            
            #Avoid Error Code 429
            sleep(1)
            
            # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
            pytrend.build_payload([word], cat=0, timeframe=time_slot_1,geo='',gprop='')

            # Interest Over Time
            interest_over_time_df = pytrend.interest_over_time()
            
            #create the goal dataframe or append it to the goal dataframe
            if creation_counter_date == 0:
                input_df_temp = interest_over_time_df
            else:
                input_df_temp = input_df_temp.append(interest_over_time_df)
            creation_counter_date += 1
            
            # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
            pytrend.build_payload([word], cat=0, timeframe=time_slot_2,geo='',gprop='')

            # Interest Over Time
            interest_over_time_df = pytrend.interest_over_time()
            
            #create the goal dataframe or append it to the goal dataframe
            if creation_counter_date == 0:
                input_df_temp = interest_over_time_df
            else:
                input_df_temp = input_df_temp.append(interest_over_time_df)
            creation_counter_date += 1
        
        #Drop isPartial column and merge the dataframe with to the goal data fram
        input_df_temp = input_df_temp.drop(['isPartial'], axis=1)
        
        #create goal dataframe or merge the result for the current word to it if it already exists
        if creation_counter_word == 0:
            input_df = input_df_temp
        else:
            input_df = input_df.merge(input_df_temp, left_on='date', right_on='date', how='outer')
        creation_counter_word += 1

    return input_df