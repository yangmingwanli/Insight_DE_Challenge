# Purchase-Analytics


1. Read order_products.csv and sum up number of orders and number of new orders by product id

for example 

from the order_products.csv below,

order_id,product_id,add_to_cart_order,reordered
2,33120,1,1
2,28985,2,1
2,9327,3,0
2,45918,4,1
3,17668,1,1
3,46667,2,1
3,17461,4,1
3,32665,3,1
4,46842,1,0

get

product_id,number_order,number_new_order
33120,1, 0
28985,1, 0
9327,1, 1
45918,1, 0
17668,1, 0
46667,1, 0
17461,1, 0
32665,1, 0
46842,1, 1

2. Read products.csv and get the look up table of which department a product belongs to, product_id -> department_id

for example

from the products.csv below,

product_id,product_name,aisle_id,department_id
9327,Garlic Powder,104,13
17461,Air Chilled Organic Boneless Skinless Chicken Breasts,35,12
17668,Unsweetened Chocolate Almond Breeze Almond Milk,91,16
28985,Michigan Organic Kale,83,4
32665,Organic Ezekiel 49 Bread Cinnamon Raisin,112,3
33120,Organic Egg Whites,86,16
45918,Coconut Butter,19,13
46667,Organic Ginger Root,83,4
46842,Plain Pre-Sliced Bagels,93,3

get

product_id,department_id
9327, 13
17461, 12
17668, 16
28985, 4
32665, 3
33120, 16
45918, 13
46667, 4
46842, 3
 
3. Using the outputs of step 1 and step 2, sum up the total number of orders and total number of new orders by department_id. 

get 

department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.5
4,2,0,0.0
12,1,0,0.0
13,2,1,0.5
16,2,0,0.0

Then divide the two order numbers to get percentage, sort by department_id and write to report.csv
