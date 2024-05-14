#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import zipfile
import os

class Patients:
    def __init__(self, name, ID, visit_date, visit_department, gender, race, age, ethnicity, 
                 insurance, zip_code, chief_complaint, note_id, note_type):
        self.name = name 
        self.ID = ID
        self.visit_date = visit_date
        self.visit_department = visit_department
        self.gender = gender
        self.race = race
        self.age = age
        self.ethnicity = ethnicity
        self.insurance = insurance
        self.zip_code = zip_code
        self.chief_complaint = chief_complain
        self.note_ID = note_ID
        self.note_type = note_type
            
    def __str__(self):
        return f"Patient Name: {self.name}, ID:{self.ID}, Visit Date: {self.visit_date}, Department: {self.visit_department},"
        f"Gender: {self.gender}, Race: {self.race}, Age: {self.age},"
        f"Ethnicity: {self.ethnicity}, Insurance: {self.insurance},"
        f"Zip Code: {self.zip_code}, Chief Complaint: {self.chief_complaint}, Note ID: {self.note_id},"
        f"Note Type: {self.note_type}"
        
    def extract_zip(FinalProject.zip, extracted_folder):
        with zipfile.ZipFile(FinalProject.zip, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        print(f"Extracted {FinalProject.zip} to {extracted_folder}")
    extract_zip("FinalProject.zip", "extracted_folder")


# In[ ]:




