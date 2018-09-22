import os
import csv

with open("WWE-Data-2016.csv", 'r') as csvfile:
   csvreader = csv.reader(csvfile,delimiter =',') 
   nameToCheck = input ("what wrestler do you want to look for?")
   for row in csvreader:
       if(nameToCheck == row[0]):
           get percentages(row)



