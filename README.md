### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

To run the code in this project beside the standard libraries already included in the standard Anaconda installation (numpy, pandas, matplotlib, datetime, sklearn, time and seaborn) you need to install the pytrends library the according documentation can be found [here](https://pypi.org/project/pytrends/).

The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, I was interested in using [Google Trends](https://trends.google.de/trends/?geo=DE) data to make predictions. As an example I tried to predict the share price of the german stock index DAX. For that example I tried to answer the following questions:

1. How far in the future it might even be possible to make predictions for? 
2. Is it possible to make a good prediction based only on Google Trends data?
3. Does adding more search terms improve the prediction?

## File Descriptions <a name="files"></a>

The projects contains 3 files beside this readme.

- In the notebook Googletrends_prediction.ipynb everything happens. Here the data is read in and processed based on the CRISP-DM process. Moreover the model used for the prediction is trained in this file. Markdown cells were used to assist in walking through the thought process for individual steps.  
- The `.py` file "googletrends_prediction.py" contains a function to get data from a google trends using the [pytrends](https://pypi.org/project/pytrends/) library.
- In the folder input there is the data to the share price of the DAX. This file was exported from [Yahoo-Finance](https://de.finance.yahoo.com/quote/%5EGDAXI/history?period1=1072911600&period2=1573081200&interval=1d&filter=history&frequency=1d&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACShsAqOqe1xkvCmOQ1Lys6brcUKncbM7HVnTKVlFYflU_Ok7_idvh49h2pjxXrkXMu8EyT3LCSXSom7RGA45nUZQHrsqgQ6KajWjeTRBX9vWf2Wwt0kgwQMq1ZU7kFDhG479XC1G73h9zWbBhT1rt5o2Fa48j2NF9nEINwSUX2a).

## Results<a name="results"></a>

The analyses in the notebook show that it is possible to make quite good predictions with google trends data. In our example it is surprisingly not so important how far in the future the prediction should be made.

Since this is only a first analysis to check if predictions with google trend data even make sense, I want to note that there are a lot of possibilities to improve the predictions even more. 

- Until now it was not analyzed how relevant the chosen search terms are. So a next step could be to have a deeper look at the search terms and optimize the selection of them.
- Different types of models can be checked to see which type deliveres the best prediction.
- The prediction complexity could be reduced by transforming the value we want to predict to a discrete value (like trying only to predict if the stock price stayed the same or de-/increased only a little or a lot. 
- The model could be expanded to make based on google trend data of one day as input a prediction for every of the next 30 days instead of only predicting one value in the future.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The following sources I want to give credit to for providing the data

- [Google Trends](https://trends.google.de/trends/?geo=DE) More information regarding the use of google trends data you can find [here] (https://policies.google.com/terms?hl=de).
- [Yahoo-Finance](https://de.finance.yahoo.com/). More information regarding the use of yahoo finance data you can find [here](https://de.hilfe.yahoo.com/kb/finance-for-web/SLN2310.html?impressions=true).

I also want to give credit to the developers of the [pytrends](https://pypi.org/project/pytrends/) library.

If you decide to improve the model or if you have other feedback, I would be happy if you contact me over github. 
