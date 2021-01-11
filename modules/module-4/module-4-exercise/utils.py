import pandas as pd

def q1_test():
    df = get_campaign_spending_data()
    print(df)
    
    if df.iloc[1,2] == 1516021 and df.iloc[18,2] == 10464068 and df.iloc[14,3] == 813158 and round(df.iloc[28,3], 3) == 6276319.438:
        return True
    else:
        return False

    year = 2018
    for i in range(34):
        if i == 17:
            year = 2018
            
        if i < 17:
            if df.iloc[i,1] != "House":
                return False
        else:
            if df.iloc[i,1] != "Senate":
                return False
            
        if df.iloc[i,0] != year:
            return False
        year -= 2