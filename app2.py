#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:00 2025

@author: yolanda
"""

import streamlit as st 
import pandas as pd

# Title of the app st.title("Researcher Profile Page") 
# Collect basic information 

st.image('IMG_0614.jpeg', width=200)##caption="Y")

name = "Dr. Yolanda Novokoza"
field = "Bioinformatics" 
institution = "University of South Africa" 
# Display basic profile information 

st.header("Researcher Overview") 
st.write(f"**Name:** {name}") 
st.write(f"**Field of Research:** {field}") 
st.write(f"**Institution:** {institution}") 

tab1, tab2, tab3 = st.tabs(["Biography", "Research Output", "Contact Details"])

with tab1:
    st.header("Biography")
    st.write("Dr. Yolanda Novokoza is a renowned Bioinformatician with a researech experience spanning 15 years.\nHer key insterests include Drug Discovery, Genomics and Enzymology.\n\nPS: This is a manifestation. Don't report me to officials!")
with tab2:
    st.header("Research Output")
    uploaded_file = './publications.csv'#st.file_uploader("Choose a csv file",type="csv")
    if uploaded_file: 
        publications = pd.read_csv(uploaded_file) 
        st.dataframe(publications) 
        # Add filtering for year or keyword 
        keyword = st.text_input("Filter by keyword", "") 
        if keyword: 
            filtered = publications[ 
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1) 
                ] 
            st.write(f"Filtered Results for '{keyword}':") 
            st.dataframe(filtered) 
        else: 
            st.write("Showing all publications") 
            
        # Add a section for visualizing publication trends 
        st.header("Publication Trends") 
        if uploaded_file: 
            if "Year" in publications.columns: 
                year_counts = publications["Year"].value_counts().sort_index() 
                st.bar_chart(year_counts) 
                
            else: 
                st.write("The CSV does not have a 'Year' column to visualize trends.") 
with tab3:
    st.header("Contact Details")
    email = "novoky@unisa.ac.za" 
    st.write(f"You can reach {name} at {email}.")  

