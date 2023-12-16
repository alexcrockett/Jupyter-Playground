# Observations

The notes on this page provide an analysis of data computed in **yfin_group_range_desc.ipynb**, results for which are also copied at the bottom of this page. 

There is a lot going on in the data so we will work through each point and develop next steps one-by-one. First we will go over what was already documented after looking at median values, then we will look at the range statistics more closely.

## Medians and quartiles

- We saw Lowest score in the 1st quartile and highest scores in the 4th quartile range from 2.10 to 4369.58
- We also saw that in either direction this is a large departule from the mean
- However, the departure in the upward direction was significantly greater (qualitatively speaking)
- We saw that looking at the highest score in the 1st and lowest in the 4th validates this

In other words the data seem to corrborate the idea that there is both a lot of variability in the data and that there are outlier.  

## Range statistics

To explore this a little more fully we took an unconventional approach; we defined a column for daily range, grouped this data by company and then computed mean, min, max and standard deviation in order to explore how individual companies might be contributing to the data's shape. The results confirm the idea that some companies contribute to the variability significantly more than others. 

### Differences in range

First, let us observe that the mean range scores vary from between 0.04 to 119.99, that companies std. deviations for the range also vary (0.01 to 58.82) and that we have a highest maximum range of 657 and a lowest minimum of 0.04). These values suggest that while some companies values remain consistent over time, there are companies on the other end of the spectrum that can be classified differently. 

### Volatility and stability

Based on these observations, we can conclude that there are at least two classifications to consider as entry points for further analysis, those that are volatile and those that have long-term stability. This classification may be a rationale for a number of apporaches to the data, especially for tests that assume normality.  

### Contextual and/or dynamic factors

One consideration coming from the results is the role of either contextual factors (not in the data set themselves) having an influence as well as dynamic factors that might be inferred from the right kind of analysis. 

With respect to the former, LYG (Lloyd's Group) shows little variation and is a well established bank. NVR specializes in housing and finance and seems to have risen in value by a very large amount in the last five years, possibly connected to the housing market or developments in the states it is present. 

With respect to dynamics, we might find patterns such as patterns of change, changes that are predictive of other changes or some other structural features not yet evident in the analysis. 

## Further analysis

The approach taken here provides its own opportunities for analysis. first we will discuss these and then analyses we will drive towards as we progress with the data.

### Analysis on quartiles and ranges

To begin, reassessing mean and median scores after removing outliers will help use methods that assume a normal distribution. It will be interesting to see if the removed companies share any characteristics. 

It will also be interesting to remove data with significantly extreme ranges of values. This data may itself create a risk of type 2 error.  

Finally, creating a data-frame with the outputs of the analysis discussed here and starting a new analysis could be fruitful. This may not only reveal patterns otherwise not identified. In particular, it will be interesting to use the data on range to see how this relates to price behavior. 

### Further analysis in general

#### Correlation
- Correlations to see how data on range correlates with price
- Correlations to see how Open and Close prices compare, especially with range as it is defined here
- Correlation to see how range correlates with the mean value of a company over time

#### Structure 
- Factor Analysis or Principal Component Analysis 
- Structural Equation Modeling 

## Data

### First and last quartiles

#### Companies in the first quartile:
Company
ABEV     2.947499

BAC     30.790636
BBD      4.368681
BBVA     4.879372
BCE     40.470195
          ...    
WFC     39.525165
WIT      5.356330
WMB     23.720061
WPM     36.569403
WY      28.026198
Name: Average, Length: 123, dtype: float64

#### Companies in the fourth quartile:
Company
ACN     249.476417
ADBE    417.060667
ADP     184.081445
ADSK    215.628537
AMGN    212.491112
           ...    
VRTX    247.068470
WDAY    202.697743
WST     270.453652
WTW     204.263422
ZM      173.939238
Name: Average, Length: 123, dtype: float64

#### Lowest company in the first quartile:
Company
LYG    2.102133
Name: Average, dtype: float64

#### Highest in the first quartile
Company
BK    42.263321
Name: Average, dtype: float64

#### Lowest company in the fourth quartile:
Company
VMC    155.851637
Name: Average, dtype: float64

#### Highest company in the fourth quartile:
Company
NVR    4369.584363
Name: Average, dtype: float64



### Range Statistics

#### Mean Range
Company
A       2.481682
AAPL    2.666117
ABBV    2.109405
ABEV    0.082863
ABNB    6.198645
          ...   
YUM     1.918100
ZBH     2.892501
ZM      8.445569
ZS      6.485945
ZTS     3.299444
Name: Range, Length: 491, dtype: float64

#### Min Range
Company
A       0.435815
AAPL    0.281952
ABBV    0.446642
ABEV    0.026536
ABNB    1.400002
          ...   
YUM     0.486592
ZBH     0.889999
ZM      0.883999
ZS      0.619999
ZTS     0.670361
Name: Range, Length: 491, dtype: float64

#### Max Range
Company
A       11.565640
AAPL    12.566008
ABBV    14.103725
ABEV     0.610324
ABNB    30.500000
          ...    
YUM     10.221042
ZBH     15.164343
ZM      68.179993
ZS      59.039978
ZTS     15.160277
Name: Range, Length: 491, dtype: float64

#### Standard Deviation of Range
Company
A       1.389413
AAPL    1.697801
ABBV    1.178597
ABEV    0.038495
ABNB    3.923734
          ...   
YUM     1.028575
ZBH     1.561640
ZM      8.151012
ZS      4.900544
ZTS     1.808373
Name: Range, Length: 491, dtype: float64

#### Company with Highest Mean Range
Company
NVR    119.994398
Name: Range, dtype: float64

#### Company with Lowest Mean Range
Company
LYG    0.044054
Name: Range, dtype: float64

#### Company with Highest Min Range
Company
NVR    25.780029
Name: Range, dtype: float64

#### Company with Lowest Min Range
Company
CARR    0.0
Name: Range, dtype: float64

#### Company with Highest Max Range
Company
NVR    657.209961
Name: Range, dtype: float64

#### Company with Lowest Max Range
Company
LYG    0.175404
Name: Range, dtype: float64

#### Company with Highest Std Range
Company
NVR    58.824867
Name: Range, dtype: float64

#### Company with Lowest Std Range
Company
LYG    0.019514
Name: Range, dtype: float64

