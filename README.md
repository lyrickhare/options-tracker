# options tracker
 
Webscrapping the live market data (nifty50 option chain) and plotting various parameters(eg: IV,OpenInterest etc) to indicate the market sentiment 
Parallely creating a database by manually labelling market directions and then training it on ML to design an autonomous system

Jupyter notebook has all the codebase and .txt files have segregated code

## Deploying Locally with frontend

### Using Backend to generate and export the processed data

#pseudo code for main function of python script <br />
opencsv_(oldOptionData.csv) <br />
rawop,nifty50cur = updateData() #(custom function defined in .ipynb file to import data from nseindia.com/option-chain) <br />
optionchain = dataframe(rawop) #(custom function to filter and reshape the raw data) <br />
optionchain = appendpcrOI(optionchain) <br />
optionchain = appendpcrCOI(optionchain) <br />
[(totPut/totCall),totPut,totCall] = totPCR(optionchain) <br />
STPATM = optionchain[STPATM(optionchain)][1] # (at the money price) <br />
stp_range = STP_range(optionchain, 5, nifty50cur) #(optimized range used for generating plots) <br />

Now you can use any plot function given in the jupyter notebook and save it in the folder git@github.com:lyrickhare/lyrickhare.github.io.git/opdata/assets with appropriate name to display on the web dashboard. <br />

Static page as dynamic page : <br />
  Taking advantage of small rate of change of option data parameters, we have used github pages (static) to develop our dynamic system. <br />
  Data update frequency is 15min, so just run a python loop with delay of 15 min with bash commands for git update with unsyncable (exception function)
  
  
