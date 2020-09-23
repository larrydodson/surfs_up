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
  
  We are planning to open a new surf and ice cream shop in Oahu Hawaii, a "Surf and Shake Shop". The new business' primary investor, W. Avy, is requesting an analysis of the weather (precipitation and temperatures), on Oahu as part of the due diligence based on location to predict the probable success of the business. And if successful, to use the same approach and code when possibly expanding to other locations. W. Avy has provided weather data from the island from multiple locations, and includes temperatures and precipitation measurements for the years 2010 through 2017, and this will be used for the analysis. 

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
   | Summary Stats - June Temperatures <br> Represents Temperatures from June 2010 to June 2017 | Summary Stats - December Temperatures <br> Represents Temperatures from Dec 2010 through Dec 2016 |
   | ![June_Temps.png](https://github.com/larrydodson/surfs_up/blob/master/June_Temps.png) | ![December_Temps.png](https://github.com/larrydodson/surfs_up/blob/master/December_Temps.png) |



   #### Major Points of Analysis on the Statistics Summaries 
   1. For Temperatures from the months of June and December, the mean for June is 74.9°F and for Dec is 71.0°F, a difference of 3.9°F. 
   2. The quartiles and the interquartile ranges (IQR) within each month's range indicate spreads from 2 to 4 degrees.  
   3. The largest differences in temperatures within a month's range, and also between June vs. December are at the minimum Temps, with June's at 64°F and December's at 56°F.

   
.  

---


## Summary 

  * Temperatures are relatively consistent with deltas of 2-5 °F when comparing the months of June and December over the multiple years, see Figure A below. Barring a few typical weather spikes, these spreads should be consistent during the other months of the year, and not be major factor to the success of the new business. 
  * To note, the largest change in temperature is at the minimums for both months, with December at 56 and June at 64. It may be expected that there could be a lower time of business at these lower temperatures, especially for ice cream sales. 


  **Additional queries**:
  1. abc
  2. cdef


 **Figure A: Comparison of Temperatures June and December, 2010 to 2017, Oahu** <br> 
 ![Temps-graph.png](https://github.com/larrydodson/surfs_up/blob/master/Temps-graph.png)



| **Figure B: <br> Summary Stats, Precipitation** | **Figure C: <br> Oahu Precipitation, Aug 2016 to Aug 2017** |
| :---: | :---: |
| ![precipitation_stats.png](https://github.com/larrydodson/surfs_up/blob/master/precipitation_stats.png) | ![precipitation_line.png](https://github.com/larrydodson/surfs_up/blob/master/precipitation_line.png) |


.

.end 
