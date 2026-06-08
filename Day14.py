'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
'''
friends = int(input("Enter the bill,Gst,Service Charge:")) 
Gst = friends+125
servicecharge = Gst+250
finalBIll = servicecharge
eachperson = servicecharge/4
print(finalBIll)
print(eachperson)
