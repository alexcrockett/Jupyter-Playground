# Notes
We can see that the data has some very interesting features from the initial analysis and there are one or two areas that it will be interesting to explore further before any kind of deeper analysis.

## Descriptive Statistics (observations)
- The mean and the median have some distance between them. The mean is higher by double across all values (Open, Close, High, Low and Volume).

### Skewness
- mean open: 140.07
- min open: 1.05
- max open: 6490.26
- Range: 6489.21
- standard deviation: 275.4 (twice the mean)
 
In other words the data is postively skewed. This will need to be remembered for later analysis. An interesting line of further investigation would therefore be to see which of the following is infuencing this skew:

- Is a particular stock responsible?
- Is a particular period of time responsible?

It will therefore be useful to group the data by company to compare some of their statistics, as well as by year. 

### Low Volatility
Another interesting factor are the results for the standard deviations for all scores. 

**The stanrd deviation**
$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}$

