import functions
import pandas as pd
import time
import numpy as np

n = input('Please enter number of times you want to take option chain data')
interval = input('Please enter time in seconds you want to take new data')
filename = input('Please enter the name of file in which you want to save data without extension')
filename = filename + '.xlsx'
dataToday = pd.DataFrame(columns=['EXP', 'STP', 'CALL OI', 'CALL COI', 'CALL LTP', 'CALL IV', 'PUT OI','PUT COI', 'PUT LTP', 'PUT IV', 'nifty50Cur'])
for i in range(int(n)):
    rawData = functions.updateData()
    optionChain = functions.dataframe(rawData[0])
    optionChain['ATM'] = np.full(optionChain.shape[0],optionChain.iloc[functions.STPATM(optionChain,rawData[1])][1])
    optionChain['nifty50Cur'] = np.full(optionChain.shape[0], rawData[1])
    dataToday=pd.concat([dataToday, optionChain], ignore_index=False)
    time.sleep(int(interval))
dataToday.to_excel(filename)
    
