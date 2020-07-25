#!/usr/bin/python
import boto3 #importing boto3 module
myregion='us-east-1' #Specifying Glue region
myaccountid='xxx' #Specifying AWS Account ID
mydatabase='newglue' #Specifying  Glue Database

glue_client = boto3.client('glue', region_name= myregion ) #Instatiating Glue client
response = glue_client.get_tables( CatalogId = myaccountid , DatabaseName= mydatabase, MaxResults = 1000) #Getting Glue tables in batches of 100

#The try catch block checks whether token is there or not.
try:
    token=response['NextToken'] #Getting the next token to retrive the next 100 Glue tables
except:
    print "Number of Glue table is less than 100"

tablelist = [] #Creating a list of Glue tables.

#Function to list the Glue table and appending it to the tablelist array.
def listtable():
    for a in response['TableList']:
        b=a['Name']
        print b
        tablelist.append(b)

listtable() #Calling the listtable function

# Using try catch block to retrive the list of Glue tables in blocks of 100.

try:
    while token is not None:
        response = glue_client.get_tables( CatalogId = myaccountid , DatabaseName= mydatabase, MaxResults = 1000, NextToken=token )
        print token
        listtable()
        token=response['NextToken']
except:
    print "No Token left"

#Running while loop to delete Glue table in blocks of 50.
    i=0
    while i < len(tablelist):
        j=i+50 #Left side of the range
        k=tablelist[i:j] #List of 50 tables.
        print k #Printing the 50 tables on screen
        delete = glue_client.batch_delete_table(
        CatalogId=myaccountid,
        DatabaseName=mydatabase,
        TablesToDelete=k
        )      #Calling the Glue batch table delete API.
        i=i+50 #Right side of the range
