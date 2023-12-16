import requests
import pandas as pd

class fetch:
    def __ini__(self):
        start = "ram"
    def updateData():
        ''' This function is used to get the raw-data in JSON format from NSE NIFTY50 Options using it's API and storing it '''
        
        url='https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        headers={
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "accept-encoding" : "gzip, deflate, br",
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        session=requests.Session()
        request=session.get(url,headers=headers)
        cookies=dict(request.cookies)
        response=session.get(url,headers=headers,cookies=cookies).json()
        rawdata=pd.DataFrame(response)
        # The rawdata would have the present day's record as well as future dateabss
        rawop=pd.DataFrame(rawdata['records']['data']).fillna(0)
        nifty50cur=rawdata['records']['underlyingValue']
        # Taking only the present day's data, and returning it
        return rawop,nifty50cur
    
    
    def dataframe(rawop):
        data=[]
        for i in range(0,len(rawop)):
            calloi=callcoi=putoi=putcoi=calliv=putiv=cltp=pltp=0
            stp=rawop['strikePrice'][i]
            exp=rawop["expiryDate"][i]
            if(rawop['CE'][i]==0):
                calloi=callcoi=0
            else:
                calloi=rawop['CE'][i]['openInterest']
                callcoi=rawop['CE'][i]['changeinOpenInterest']            
                cltp=rawop['CE'][i]['lastPrice']
                calliv=rawop['CE'][i]['impliedVolatility']
            if(rawop['PE'][i]==0):
                putoi=putcoi=0
            else:
                putoi=rawop['PE'][i]['openInterest']
                putcoi=rawop['PE'][i]['changeinOpenInterest']            
                pltp=rawop['PE'][i]['lastPrice']
                putiv=rawop['PE'][i]['impliedVolatility']
            opdata = {
                'EXP': exp,
                'STP': stp,
                'CALL OI': calloi, 'CALL COI':callcoi, 'CALL LTP':cltp, 'CALL IV':calliv,
                'PUT OI': putoi, 'PUT COI':putcoi, 'PUT LTP':pltp, 'PUT IV':putiv,
            }              
            data.append(opdata)
        optionchain=pd.DataFrame(data)
        return optionchain
    

    def STPATM(optionchain,nifty50cur):
        for i in range(0,optionchain.shape[0]):
            if(optionchain.iloc[i][1]<nifty50cur and optionchain.iloc[i+1][1]>nifty50cur):
                if(abs(optionchain.iloc[i][1]-nifty50cur)>abs(optionchain.iloc[i+1][1]-nifty50cur)):
                    return i+1
                else:
                    return i