#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from tkinter import messagebox
import datetime
import zipfile

class HospitalApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Database")
        
        # Login Frame
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(pady=20)
        
        self.lbl_username = tk.Label(self.login_frame, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)
        
        self.lbl_password = tk.Label(self.login_frame, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)
        
        self.btn_login = tk.Button(self.login_frame, text="Login", command=self.login)
        self.btn_login.grid(row=2, columnspan=2, padx=10, pady=5)
        
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        credentials = {
        "admin": "adminpass",
        "clinician": "clinicianpass",
        "nurse": "nursepass",
        "management": "managementpass"
    }
    
        if username in credentials and credentials[username] == password:
        # Valid credentials, determine user role and show appropriate thing
            user_role = determine_user_role(username)  # Implement this function to get user role
            self.show_menu(user_role)
        else:
            # Invalid credentials, show error message
            tk.messagebox.showerror("Error", "Invalid username or password")

    def determine_user_role(self, username):
        return "admin" # Placeholder for determining user role 

    def show_menu(self, user_role):
        # Implement logic to show appropriate menu based on user role
        # For simplicity, let's assume we have separate functions for each menu
        if user_role == "admin":
            self.add_patient_frame()
        elif user_role == "clinician":
            self.retrieve_patient_frame()
        elif user_role == "nurse":
            self.count_visits_frame()
        elif user_role == "management":
            self.generate_key_stats_frame()
            
    def add_patient_frame(self):
        self.add_patient_frame = tk.Frame(self.master)
        self.add_patient_frame.pack()
    
        # Labels and entry fields
        lbl_patient_id = tk.Label(self.add_patient_frame, text="Patient ID:")
        lbl_patient_id.grid(row=0, column=0, padx=10, pady=5)
        entry_patient_id = tk.Entry(self.add_patient_frame)
        entry_patient_id.grid(row=0, column=1, padx=10, pady=5)

        lbl_visit_time = tk.Label(self.add_patient_frame, text="Visit Time:")
        lbl_visit_time.grid(row=1, column=0, padx=10, pady=5)
        entry_visit_time = tk.Entry(self.add_patient_frame)
        entry_visit_time.grid(row=1, column=1, padx=10, pady=5)

        lbl_department = tk.Label(self.add_patient_frame, text="Department:")
        lbl_department.grid(row=2, column=0, padx=10, pady=5)
        entry_department = tk.Entry(self.add_patient_frame)
        entry_department.grid(row=2, column=1, padx=10, pady=5)

        # Button to add patients
        btn_add_patient = tk.Button(self.add_patient_frame, text="Add Patient", command=lambda: self.add_patient_record(entry_patient_id.get(), entry_visit_time.get(), entry_department.get()))
        btn_add_patient.grid(row=3, columnspan=2, padx=10, pady=5)
    
    def add_patient(self):
        # Retrieve patient information from entry fields
        patient_id = self.entry_patient_id.get()
        patient_name = self.entry_patient_name.get()

        # Implement functionality to add patient record
        if patient_id not in self.patient_records:
            self.patient_records[patient_id] = {'name': patient_name}
            tk.messagebox.showinfo("Success", f"Patient with ID {patient_id} has been added.")
        else:
            tk.messagebox.showerror("Error", f"Patient with ID {patient_id} already exists.")

    def delete_patient_frame(self):
        self.delete_patient_frame = tk.Frame(self.master)
        self.delete_patient_frame.pack()

         # Label and Entry field for entering Patient ID
        self.lbl_patient_id = tk.Label(self.delete_patient_frame, text="Patient ID:")
        self.lbl_patient_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_patient_id = tk.Entry(self.delete_patient_frame)
        self.entry_patient_id.grid(row=0, column=1, padx=10, pady=5)

        # Button to trigger deletion
        self.btn_delete = tk.Button(self.delete_patient_frame, text="Delete", command=self.delete_patient)
        self.btn_delete.grid(row=1, columnspan=2, padx=10, pady=5)
    
    def delete_patient(self):
        # Retrieve patient ID from entry field
        patient_id = self.entry_patient_id.get()

        # Implement functionality to delete patient record
        if patient_id in self.patient_records:
            del self.patient_records[patient_id]
            tk.messagebox.showinfo("Success", f"Patient with ID {patient_id} has been deleted.")
        else:
            tk.messagebox.showerror("Error", f"Patient with ID {patient_id} not found.")
            
    def display_patients_frame(self):
        self.display_patients_frame = tk.Frame(self.master)
        self.display_patients_frame.pack()

        # Text area to display patients
        txt_display = tk.Text(self.display_patients_frame, width=50, height=20)
        txt_display.pack(pady=10)

        # Button to display patients
        btn_display_patients = tk.Button(self.display_patients_frame, text="Display Patients", command=self.display_patients)
        btn_display_patients.pack(pady=5)
   
    def display_patients(self, text_area):
        patients_data = self.get_formatted_patient_data()
        if patients_data:
            text_area.delete('1.0', tk.END)  # Clear previous content
            text_area.insert(tk.END, patients_data)
        else:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, "No patients found.")
   
    def count_visits_frame(self):
        self.count_visits_frame = tk.Frame(self.master)
        self.count_visits_frame.pack()

        # Entry field for date
        lbl_date = tk.Label(self.count_visits_frame, text="Date (yyyy-mm-dd):")
        lbl_date.pack(pady=5)
        entry_date = tk.Entry(self.count_visits_frame)
        entry_date.pack(pady=5)

        # Button to count visits
        btn_count_visits = tk.Button(self.count_visits_frame, text="Count Visits", command=lambda: self.count_visits(entry_date.get()))
        btn_count_visits.pack(pady=5)
    
    def count_visits(self, date):
        visit_count = self.count_visits_by_date(date)
        if visit_count is not None:
            tk.messagebox.showinfo("Visit Count", f"Number of visits on {date}: {visit_count}")
        else:
            tk.messagebox.showerror("Error", "Invalid date format or no visits found for the date.")     

    def log_user_action(self, username, user_role, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}: User '{username}' ({user_role}) performed action: {action}\n"
        with open("user_actions.log", "a") as logfile:
            logfile.write(log_entry)
        
    def generate_key_stats_frame(self):
        self.generate_key_stats_frame = tk.Frame(self.master)
        self.generate_key_stats_frame.pack()

        # Text area to display key statistics
        self.txt_key_stats = tk.Text(self.generate_key_stats_frame, width=50, height=20)
        self.txt_key_stats.pack(pady=10)

        # Button to generate key statistics
        btn_generate_stats = tk.Button(self.generate_key_stats_frame, text="Generate Key Statistics", command=self.generate_key_statistics)
        btn_generate_stats.pack(pady=5)

        # Log user action when generating key statistics
        btn_generate_stats.bind("<Button-1>", lambda event: self.log_user_action(self.entry_username.get(), self.determine_user_role(self.entry_username.get()), "Generate Key Statistics"))
    
    def generate_key_statistics(self):
        total_patients = len(self.patient_records)
        # More statistics calculations can be added here
        # Display statistics in the text area
        self.txt_key_stats.delete('1.0', tk.END)
        self.txt_key_stats.insert(tk.END, f"Total patients: {total_patients}\n")

    def extract_zip(FinalProject.zip, extracted_folder):
        with zipfile.ZipFile(FinalProject.zip, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        print(f"Extracted {FinalProject.zip} to {extracted_folder}")
        extract_zip("FinalProject.zip", "extracted_folder")
    
def main():
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




