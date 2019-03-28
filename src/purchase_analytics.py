#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import csv from standard Python library
import csv


# In[2]:


# read products_fn csv to dictionary (catlog) of {product_id:department_id} as look up table for later use.
def read_catlog(products_fn):
    reader = csv.DictReader(open(products_fn))
    catlog = {}
    for row in reader:
        catlog[int(row['product_id'])] = int(row['department_id'])
    return catlog


# In[3]:


# read order_products.csv to dictionary (sale) of {product_id:[number_of_orders,number_of_first_orders]}
def read_sales_record(order_products_fn):
    reader = csv.DictReader(open(order_products_fn))
    sale = {}
    for row in reader:
        # each row is a sale record with two relevant info, namely product_id and reordered.
        # get current number_of_orders,number_of_first_orders for the product_id.
        # initilize to zeros if product_id is a new key (first encounter of this product_id).
        # pts stands for product total sales, pns stands for product new sales.
        pts,pns = sale.get(row['product_id'], [0,0])
        # increment number_of_orders by +1
        # increment number_of_first_orders by +1 if it's a first order (reordered==0).
        if row['reordered'] == '0':
            sale[int(row['product_id'])] = [pts + 1,pns+1]
        else:
            sale[int(row['product_id'])] = [pts + 1,pns]
    return sale


# In[4]:


# combine catlog and sale record to dictionary (result) of {department_id:[number_of_orders,number_of_first_orders]}
# sum up number_of_orders,number_of_first_orders for all product_id belonging to each department_id.
def combine_results(catlog,sale):
    result={}
    for pid,did in catlog.items():
        # pid stands for product_id, did stands for department_id
        # dts stands for department total sales, dns stands for department new sales.
        # pts stands for product total sales, pns stands for product new sales.
        dts,dns = result.get(did, [0,0])
        pts,pns = sale.get(pid, [0,0])
        result[did]=[dts+pts,dns+pns]
    return result


# In[5]:


catlog = read_catlog('products.csv')
sale = read_sales_record('order_products.csv')
result = combine_results(catlog,sale)

# write to report.csv file.
header = ['department_id','number_of_orders','number_of_first_orders','percentage']
with open('report.csv','w+') as f:
    writer = csv.writer(f)
    # write the header row first
    writer.writerow(header)
    # write result to csv in sorted key (department_id) order, add the percentage column rounded to 2 decimal.
    for key in sorted(result.keys()):
        writer.writerow([key, result[key][0],result[key][1],round(result[key][1]/result[key][0],2)])


# In[ ]:
