## **ORDERS TABLE**



1. change the datatypes of dates
2. check for nulls -> find out all the nulls are actually information not garbage which need to be removed





### **Customers Table**

1. there is no null value in the customer table
2. there are two types of customer id's :-

&#x20;  i. one is customer\_id

&#x20;  ii. second one is customer\_unique\_id

3\. there is customer\_id which is primary key in customer table is unique in the customer table where's customer\_unique is actually define one unique customer my observation says.

&#x20;  it is because of privacy reason so that in orders table no one can see customer's order history so in order table : one unique order\_id -> one unique customer\_id -> associated with only

&#x20;  one **unique customer** in customer table




### **ORDER ITEMS TABLE**



1. no null values found, zero duplicates

2\. converted shipping\_limit\_date from object to datetime64

3\. order\_item\_id is not a unique row identifier — it represents the item sequence within an order. one order can have multiple items, so when calculating order-level revenue groupby order\_id and sum



### **PAYMENTS TABLE**



1. no null values found, zero duplicates

2\. found 3 rows with payment\_type = 'not\_defined' and payment\_value = 0.0 — completely meaningless rows, dropped them using filter

3\. payment\_sequential works similar to order\_item\_id — one order can be paid via multiple payment methods, each gets its own sequential number. when calculating total order revenue use groupby order\_id and sum payment\_value



### **REVIEWS TABLE**



1. zero duplicates

2\. converted review\_creation\_date and review\_answer\_timestamp from object to datetime64

3\. review\_comment\_title has 87,656 nulls (88%) and review\_comment\_message has 58,247 nulls (59%) — these are not errors, most customers only give a star rating and skip writing a comment

4\. left both comment columns as NaN — pandas handles NaN naturally in aggregations, and during EDA we'll filter using .notna() when needed



### **PRODUCTS TABLE**



1. zero duplicates

2\. found two typos in column names — product\_name\_lenght and product\_description\_lenght, fixed to product\_name\_length and product\_description\_length

3\. 610 rows had nulls in product\_category\_name, product\_name\_length, product\_description\_length, product\_photos\_qty — these are real products that were sold but had incomplete listings, filled product\_category\_name with 'unknown' and remaining metadata columns with 0

4\. 2 rows had nulls in physical dimension columns (weight, length, height, width) — filled with median instead of mean because product dimensions are heavily right skewed due to occasional extreme values like furniture or industrial equipment



### **SELLERS TABLE**



1. no null values found, zero duplicates

2\. no action needed — already clean



### **CATEGORY TRANSLATION TABLE**



1. no null values found, zero duplicates

2\. no action needed — already clean



### **GEOLOCATION TABLE**



1. no null values found

2\. found 261,831 duplicate rows out of 1,000,163 — dropped duplicates using subset=\['geolocation\_zip\_code\_prefix'] keeping first occurrence, because we only need one lat/lng coordinate per unique zip code for the geo map in Phase 4

3\. rows reduced from 1,000,163 to 19,015 unique zip codes







