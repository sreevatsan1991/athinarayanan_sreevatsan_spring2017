
<h1> ANALYSIS OF YELP AND ZOMATO DATA

  <img src="Images\yelpzomato.jpg">

<h3>Introduction</h3><br>
Being a great cook myself, I thought analyzing yelp and zomato data would be great to understand food preferences in various cities. This analysis focusses on combining **yelp and zomato data**, getting specific user input to suggest good restaurants for him in his locality and analyzing zomato reviews.

<h3>Data sources</h3>
* Yelp Data Source -   https://www.yelp.com/developers   File Format : JSON
* Zomato Data Source - https://developers.zomato.com/api File Format : JSON

<h2> DATA COLLECTION </h2>

The city and country name of the user is fetched using 'input'. These inputs are passed further for data collection

<h3>Yelp Data Collection - Steps</h3>
* The client id and keys are obtained for Yelp data
* A request is made to the yelp data to obtain the access token which needs to be passed in the header when making the request to the yelp API 
* Data that is collected from the yelp API is stored in a folder structure<br><br>
<b>Folder structure</b><br><br>
<font size=4>Data-->Yelp Data --> Country --> Country State --> City --> Restaurants --> File.json</font><br><br>
Yelp Data Location : <a href="Data/Yelp Data"> Yelp Data </a>
<h4>Reviews Data</h4>
* Based on the data collected from yelp APi, the id of each restaurant is stored and passed to the reviews API to get reviews about these restaurants. Each restaurant gets 3 reviews (API limit)

 <font size=4>Data-->Yelp Data Reviews --> Country --> Country State --> City --> Restaurant id --> Reviews.json</font><br><br>
 Yelp Data Reviews Location : <a href="Data/Yelp Data Reviews"> Yelp Data Reviews </a>

<h3>Zomato Data Collection - Steps</h3>

* The city name of the user is sent to zomato API to obtain the city id (This is used to get restaurant details for a city)
* The restaurant names of the data collected in Yelp API is passed to the zomato API with the city id to fetch data <br><br>
<b>Folder structure</b><br><br>
<font size=4>Data-->Zomato Data --> Country --> City --> Zipcode --> Price Range--> File.json</font><br><br>
Zomato Data : <a href="Data/Zomato Data"/>Zomato Data</a>

<h2> DATA STORAGE </h2>

* The data collected using API is stored in a folder structure
* Now the data that is collected as JSON needs to be converted to CSV to be processed in pandas dataframe.

 <b>CSV Data Storage<br></b>
- Restaurant details for Yelp and Zomato  
- Restaurant Open Hours 
- Restaurant Cuisines 
- Restaurant Reviews

The processed data can be accessed <a href="Other Files">here</a>

## ANALYSIS - 1 <img align="right" style="width:350px;height:125px;margin-top:0px;padding-top:0px;" src="Images/cloud-pricing.png"/>
## COMPARISON OF YELP AND ZOMATO DATA

#### Criteria for Analysis
* The yelp data and zomato data is read into a pandas dataframe
* The rating of reach restaurant in Zomato and Yelp is compared
* The relationship between review counts, price and restaurant ratings are compared
* The best overall restaurant is identified by normalizing restaurant rating, review count and price


### Part 1
The rating of reach restaurant in Zomato and Yelp is compared <br>
* After joining the yelp and zomato data, for every city, the rating of restaurants in yelp and zomato is analyzed (by using group by and mean).


<img src="Readme images/Analysis1-yelpzomato.PNG">

### Graph Output

<img src="Output/Analysis 1/Analysis1-Rating.jpg">

## The relationship between review counts, price and restaurant ratings are compared

Yelp Data Plots<br>
<img src="Output/Analysis 1/yelp1.jpg">

Zomato Data Plots
<img src="Output/Analysis 1/zomato1.jpg">

## Inferences

* From the above graphs I infer that for Yelp, review count and price of a restaurant dont have much of a correlation.
* For Zomato though, I find that for most of the countries, votes increase if the restaurant is more expensive
* Another inference for yelp is that the restaurants rating increases when its less expensive. For Zomato, different behavior is observed in each country.


## ANALYSIS - 2 <img align="right" style="width:350px;height:125px;margin-top:0px;padding-top:0px;" src="Readme images/analysis2cui.jpg"/>
## CUISINE ANALYSIS OF RESTAURANTS

### Criteria

* The cuisine details of restaurants are loaded to a dataframe
* The top cuisines in each city is calculated
* User input is fetched to find his city name
* The top cuisines in his city is displayed
* The user is asked for his favourite cuisine
* The top restaurant in this cuisine and city is displayed

Top Cuisines
<img src="Readme images/analysis2.PNG">


Graph - Displayed after fetching user input about which city he resides in<br>
  <img src="Output/Analysis 2/cuisine.PNG">

Once the user enters his favourite cuisine, two iamges are displayed
- The image is dynamically fetched from the url link available in the data
- The restaurant timing data are processed and stored in csv. This data is displayed by dynamically loading and reading the csv

## RESULTS

<img src="Output/Analysis 2/topres.PNG">

<img src="Output/Analysis 2/cheapres.PNG">

## ANALYSIS - 3 <img align="right" style="width:350px;height:125px;margin-top:0px;padding-top:0px;" src="Readme images/rateit.jpg"/>
## ANALYSIS OF REVIEWS

## Criteria
* Sentiment Analysis of reviews (Naive Bayes Classifier)
* Map plot of restaurant data

Note: This analysis needs Basemap package to be installed in the system

## Sentiment Analysis Results
<img src= "Output/Analysis 3/sentiment.PNG">

## Graph
Correlation between review sentiment and restaurant rating
   <img src= "Output/Analysis 3/graph.PNG">

### Inference
* I conclude from the above graph that there is no relation between rating given and the sentiment of reviews

##  Map Plot of restaurants for Boston City

<img src="Output/Analysis 3/mapplot.PNG">


```python

```
