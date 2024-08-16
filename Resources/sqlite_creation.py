import sqlite3
import pandas as pd

from pathlib import Path

database_path = "./Resources/alzheimer_db.sqlite"
Path(database_path).touch()

conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('''CREATE TABLE al_info (id int PRIMARY KEY, PatientID int, Age int, Gender int, Ethnicity int, EducationLevel int,
          BMI float, smoking int, AlcoholConsumption float, PhysicalActivity float, DietQuality float, SleepQuality int, FamilyHistoryAlzheimers int,
          CardiovascularDisease int, Diabetes int, Depression int, HeadInjury int, Hypertension int, SystolicBP int, DiastolicBP int, CholesterolTotal float,
          CholesterolLDL float, CholesterolHDL float, CholesterolTriglycerides float, MMSE float, FunctionalAssessment float, 
          MemoryComplaints int, BehavioralProblems int, ADL float, Confusion int, Disorientation int, PersonalityChanges int, 
          DifficultyCompletingTasks int, Forgetfulness int, Diagnosis int)''')

csv_al = pd.read_csv("alzheimer_clean.csv")
csv_al.to_sql("al_info", conn, if_exists='append', index=False)