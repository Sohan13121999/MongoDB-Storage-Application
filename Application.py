from email.header import Header
from gridfs import Database
from matplotlib.collections import Collection
from pymongo import MongoClient
import urllib
import csv
import json
import pprint
import pandas as pd
import streamlit as st
from PIL import Image
import urllib

def CredentialsConnect():
    username=st.text_input("Enter Your Cluster UserName",key=1)
    password=st.text_input("Enter Your Cluster Password",key=2)
    database=st.text_input("Enter your Cluster Name")
    ConnectionURL=st.text_input("Enter your Connection URL(replace the <password> with your own password)",key=3)
    


    
    
    if len(ConnectionURL)>10:
        username=urllib.parse.quote_plus(username)
        password=urllib.parse.quote_plus(password)
        hello=""
        ind=ConnectionURL.find("@")
        last=len(ConnectionURL)
        for i in range(ind,last):
            hello=hello+ConnectionURL[i]
        
        client=MongoClient("mongodb+srv://"+username+":"+password+hello)
        st.write(client.database)
        Sample_Database=client.Sample_Database
        Collection=Sample_Database.Collection
        
        return Collection



    
    
                
                





if __name__ == '__main__':
    image=Image.open("logo.png")
    st.image(image,width=100)
    st.title("InfoSearcher")
    st.subheader("Mongodb Based Real Time Data Storage and Data Finder Application")

    agree=st.checkbox("Connect to your Mongo-Db Cluster")
 
    if agree:
        coll=CredentialsConnect()
        if coll is not None:
            uploadfile=st.file_uploader("Please upload your CSV File")
            if uploadfile is not None:
                da=pd.read_csv(uploadfile)
                header=da.columns
                st.write(header)
                reader=da.to_dict('records')
                for i in reader:
                    coll.insert_one(i)
            
        pprint.pprint(coll.find_one({"Year":"2013"}))
                
            
        


            
                
                
                    
            
            
                        

                    
            
                

                    
            
        
    
        
    
        




