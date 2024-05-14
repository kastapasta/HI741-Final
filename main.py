#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import zipfile
from patient import Patients
from administrator import PatientDatabase
from tkinterfile import hospital app

class PatientDatabase:

    def __init__(self, credentials_file, patients_file):
        self.credentials_file = credentials_file
        self.patients_file = patients_file
        self.patient_records = {}
        self.load_patients()
        
def main(file_path):
    print("Patient Database")
    
    # extract zipfile
    zip_path = os.path.join(file_path, "FinalProject.zip")
    extract_to = os.path.join(file_path, "FinalProject_extracted")
    extract_zip(zip_path, extract_to)
    csv_file = os.path.join(extract_to, "Project_credentials.csv")
    csv_file = os.path.join(extract_to, "Project_patient_information.csv")
    database = PatientDatabase(credentials_file, patients_file)
    
     # Authentication
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_role = database.authenticate_user(username, password)
        if user_role:
            print(f"Welcome, {username}! You are logged in as {user_role}.")
            break
        else:
            print("Invalid credentials. Please try again.")
    
    # Role-based control
    while True:
        action = input("Choose an action (add_patient, remove_patient, display_patients, Stop): ")
        if action == "Stop":
            break
        elif action == "add_patient":
            name = input("Enter patient name: ")
            ID = input("Enter patient ID: ")
            visit_date = input("Enter visit date: ")
            chief_complaint = input("Enter chief complaint: ")
            note_ID = input("Enter note ID: ")
            note_type = input("Enter note type: ")
            new_patient = Patients(name, ID, visit_date, chief_complaint, note_ID, note_type)
            database.add_patient_record(new_patient)
        elif action == "remove_patient":
            ID = input("Enter ID to remove:")
            database.delete_patient_record(ID)
        elif action == "display_patients:":
            database.display_patients()
        else:
            print("Invalid action, please try again.")
    
if __name__ == '__main__':
    import sys
    if len(sys.argv)!=2:
        print("Usage: python script.py input_path")
    else:
        input_path = sys.argv[1]
        main(input_path)


# In[ ]:




