#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import zipfile

class PatientDatabase:

    def __init__(self, credentials_file, patients_file):
        self.credentials_file = credentials_file
        self.patients_file = patients_file
        self.patient_records = {}
        self.load_patient()
        
    def load_patients(self): # Load patient data
        with open(self.patients_file, 'r') as file:
            reader = csv.DictReader(file)
        for row in reader:
            patient = Patients(**row)
            self.patient_records[patient.patient_id] = patient
        with open(self.credentials_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password, role = row
                
    def authenticate_user(self, username, password):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return row[2]  # Return role if username/password are valid
        return None  # Return none if invalid

    def add_patient_record(self, patient_data):
        # Adds in record of new patients.
        # If they do not exist in system, they will be added as a new patient.
        if user_role in ["admin", "clinician", "nurse"]:
            if patient_data.ID not in self.patient_records:
                self.patient_records[patient_data.ID] = patient_data
                print("Patient record successfully added.")
            else:
                print("Patient ID already exists.")
        else:
            print("Unauthorized to add patient records.")

    def delete_patient_record(self, patient_id):
        # Deletes patient record by patient ID.
        if user_role in ["admin", "clinician", "nurse"]:
            if patient_id in self.patient_records:
                del self.patient_records[patient_id]
                print("Patient record is successfully deleted.")
            else:
                print("Patient ID not found.")
        else:
            print("Unauthorized to delete patient records.")
    
    def display_patients(self, user_role): 
        # Display patients based on user's role
        if user_role in ["admin", "clinician", "nurse"]:
            for patient in self.patient_records.values():
                print(patient)
        else:
            print("Unauthorized to view patient records.")

    def count_visits(self, user_role):
        # Count visits action based on user's role
        if user_role == "admin":
            print("You have accessed count_visits action.")
            # Implement count_visits functionality here
        else:
            print("Unauthorized to access count_visits.")
    
    def retrieve_patient_record(self, patient_id):
        # Retrieves patient record through ID number.
        if patient_id in self.patient_records:
            return self.patient_records[patient_id]
        else:
            return "Patient ID not found."
        pass

    def retrieve_patient_age(self, age):
        patients_age = []
        for patient_id, data in self.patient_records.items():
            if data.get("age") == age:
                patients_age.append((patient_id, data))
        return patients_age
        # Retrieves age of patient in database.
        pass

    def retrieve_patient_gender(self, gender):
        patients_gender = []
        for patient_id, data in self.patient_records.items():
            if data.get("gender") == gender:
                patients_gender.append((patient_id, data))
        return patients_gender
        pass

    def retrieve_patient_by_race_ethnicity(self, race, ethnicity):
        # Retrieves race and ethnicity of patient.
        patients_race_ethnicity = []
        for patient_id, data in self.patient_records.items():
            if data.get("race") == race and data.get("ethnicity") == ethnicity:
                patients_race_ethnicity.append((patient_id, data))
        return patients_race_ethnicity
        pass

    def retrieve_patient_by_insurance(self, insurance):
        # Retrieves insurance of patient.
        patients_insurance = []
        for patient_id, data in self.patient_records.items():
            if data.get("insurance") == insurance:
                patients_insurance.append((patient_id, data))
        return patients_insurance
        pass

    def retrieve_patient_by_department(self, department):
        # Retrieves department patient is in
        patients_department = []
        for patient_id, data in self.patient_records.items():
            if data.get("department") == department:
                patients_department.append((patient_id, data))
        return patients_department
        pass

    def retrieve_patient_visits_by_department(self, patient_id, department):
        # Retrieves patient based on the department that they are in.
        visits_based_on_department = []
        for patient_id, data in self.patient_records.items():
            if department in data.get("visits"):
                visits_based_on_department.append((patient_id, data))
        return visits_based_on_department
        pass

    def retrieve_frequent_visitor(self, department, zip_code):
        retrieve_frequent_visitor = [] 
        for patient_id, data in self.patient_records.items():
            if department in data.get("visits") and data.get("zip_code") == zip_code:
                frequent_visitors.append((patient_id, data))
        return frequent_visitors
        pass
    
    def display_patients(self): 
        for patient in self.patient_records.values():
            print(patient)
    
    def generate_key_statistics(self):
        print("Generating report...")
        patients_by_age = {}
        patients_by_gender = {}
        
        for patient in self.patient_records.values():
            if patient.age in patients_by_age:
                patients_by_age[patient.age] += 1
            else:
                patients_by_age[patient.age] = 1
                
            if patient.gender in patients_by_gender:
                patients_by_gender[patient.gender] += 1
            else:
                patients_by_gender[patient.gender] = 1
        print("Number of patients who visited the hospital by age:")
        for age, count in patients_by_age.items():
            print(f"Age {age}: {count} patients")
            
        print("Number of patients who visited the hospital by gender:")
        for age, count in patients_by_gender.items():
            print(f"Gender {gender}: {count} patients")
            
    def extract_zip(FinalProject.zip, extracted_folder):
        with zipfile.ZipFile(FinalProject.zip, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        print(f"Extracted {FinalProject.zip} to {extracted_folder}")
    extract_zip("FinalProject.zip", "extracted_folder")


# In[ ]:




