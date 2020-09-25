# surfs_up
UTMCC DataViz Module 9
---

## Contents 
  * Overview
    - Purpose
    - Resources
  * Results
  * Summary
 

---  

## Overview 
  
  We are planning to open a new surf and ice cream shop in Oahu Hawaii, a "Surf and Shake Shop". The new business' primary investor, W. Avy, is requesting an analysis of the weather (precipitation and temperatures), on Oahu as part of the due diligence based on location to predict the probable success of the business. And if successful, to use the same approach and code when possibly expanding to other locations. W. Avy has provided weather data from the island from multiple locations, and includes temperatures and precipitation measurements for the dates from January 1, 2010 through August 23, 2017, and these will be used for the analysis. 

   ### Purpose
   To prepare an analysis of precipitation data over the past 12 months for Oahu Hawaii, in the months of June and December from 2010 through 2017, in order to assist in a business decision to open a "Surf & Shake Shop" on the island. The analysis will help with understanding and predicting a successful outcome for traffic at the shop, to determine if this business is sustainable year-round. The deliverables are: 
   - Deliverable 1: Determine the Summary Statistics for June
   - Deliverable 2: Determine the Summary Statistics for December
   - Deliverable 3: A written report for the statistical analysis (This Report). 
  
   

   ### Resources
  * Data sources: hawaii.sqlite file
  * Software: Windows10, Python 3.8.3, Pandas, SQLAlchemy, Jupyter Notebook, VS Code 1.49.1, SQLite database
  

--- 

## Results
  
  ### Deliverables 1 and 2:  - Determine the Summary Statistics of Precipitation for June and December
   
   | **Deliverable 1** | **Deliverable 2** |
   | :---:  | :---:  |
   | Summary Stats - June Temperatures <br> Represents Temperatures from June 1, 2010 to June 30, 2017 | Summary Stats - December Temperatures <br> Represents Temperatures from Dec 1, 2010 through Dec 31, 2016 |
   | ![June_Temps.png](https://github.com/larrydodson/surfs_up/blob/master/June_Temps.png) | ![December_Temps.png](https://github.com/larrydodson/surfs_up/blob/master/December_Temps.png) |



   #### Major Points of Analysis on the Statistics Summaries 
   1. For Temperatures from the months of June and December, the mean for June is 74.9°F and for Dec is 71.0°F, a difference of 3.9°F. 
   2. The quartiles and the interquartile ranges (IQR) within each month's range indicate spreads from 2 to 4 degrees.  
   3. The largest differences in temperatures within a month's range, and also between June vs. December are at the minimum Temps, with June's at 64°F and December's at 56°F.

   
.  

---


## Summary 

  * Temperatures are relatively consistent and linear in comparison with each other, with deltas of 2-5 °F when comparing the months of June and December over the multiple years, see Figure A below. Barring a few typical weather spikes, these spreads should be consistent during the other months of the year, and not be major factor to the success of the new business. 
  * To note, the largest change in temperature is at the minimums for both months, with December at 56°F and June at 64°F. It may be expected that there could be slower business at these lower temperatures, especially for ice cream sales. 


  **Additional queries**:
  1. **Rainfall** - With weather analysis, it is probable that precipitation is the larger factor versus Temperatures as a predictor factor of the business' success as a cause to customer traffic, Please see Figure B and C below. Precipitation has a wide range throughout the past year, 2016 to 2017, and a possible impact to business may be indicated on the days of heaviest rainfall. Further analysis of the precipitation data of previous years could be valuable information for evaluation.  
  2. **Rain and Temps** - Recommend that consideration be given for a combined analysis of the temperature data with the precipitaton data over the same time periods. See Figures A, B and C below. The statistics for precipitation show that the typical daily rainfall is very consistent, with a mean of 0.18 and the quartiles having significantly tight spreads of 0 to 0.13. The min to max is quite large in comparison, from 0 to 6.7, so it is the maximums that are very significant. Information from the data analysis that would show relationship between the amount of precipitation and the temperature, especially during the winter months could prove valuable to decisions for prediction of success.


 **Figure A: Comparison of Temperatures June and December, 2010 to 2017, Oahu** <br> 
 ![Temps-graph.png](https://github.com/larrydodson/surfs_up/blob/master/Temps-graph.png)



| **Figure B: <br> Summary Stats, Precipitation** | **Figure C: <br> Oahu Precipitation, Aug 2016 to Aug 2017** |
| :---: | :---: |
| ![precipitation_stats.png](https://github.com/larrydodson/surfs_up/blob/master/precipitation_stats.png) | ![precipitation_line.png](https://github.com/larrydodson/surfs_up/blob/master/precipitation_line.png) |


.

.end 
