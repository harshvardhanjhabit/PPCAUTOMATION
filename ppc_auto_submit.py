import pandas as pd
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# ==============================
# READ EXCEL
# ==============================
students = pd.read_excel("students.xlsx")

# FIX DOB: convert to DD-MM-YYYY string
students['dob'] = pd.to_datetime(
    students['dob'], dayfirst=True, errors='coerce'
).dt.strftime('%d-%m-%Y')

# REMOVE accidental spaces from column names
students.columns = students.columns.str.strip()

# ==============================
# RANDOM QUESTIONS LIST
# ==============================
random_questions = [
    "How can I improve my focus while studying?",
    "What is the best way to prepare for exams effectively?",
    "How can I manage stress during school exams?",
    "What study habits help retain information longer?",
    "How can I balance school and extracurricular activities?",
    "How to choose the right career path after school?",
    "How can technology help in better learning?",
    "What are tips for effective time management for students?",
    "How to stay motivated throughout the school year?",
    "How can I improve my problem-solving skills in studies?"
]

# ==============================
# START BROWSER (AUTO DRIVER)
# ==============================
driver = webdriver.Chrome()
driver.get("https://innovateindia1.mygov.in/ppc-2026/student-through-teacher-form/?lang=en")

print("🔐 Please LOGIN manually to MyGov if not logged in.")
input("👉 After login & student form is visible, press ENTER here...")

time.sleep(3)

# ==============================
# LOOP THROUGH STUDENTS
# ==============================
for i, s in students.iterrows():
    try:
        print(f"➡️ Submitting: {s['first_name']} {s['last_name']}")

        # First Name
        fn = driver.find_element(By.ID, "student_first_name")
        fn.clear()
        fn.send_keys(str(s['first_name']))

        # Last Name
        ln = driver.find_element(By.ID, "student_last_name")
        ln.clear()
        ln.send_keys(str(s['last_name']))

        # Email
        email = driver.find_element(By.ID, "user_mail")
        email.clear()
        email.send_keys(str(s.get('email', '')))

        # Mobile
        mobile = driver.find_element(By.ID, "user_mobile")
        mobile.clear()
        mobile.send_keys(str(s.get('mobile', '')))

        # Gender
        Select(driver.find_element(By.ID, "gender")).select_by_visible_text(
            str(s.get('gender', 'Male')).capitalize()
        )

        # DOB (remove readonly)
        driver.execute_script(
            "document.getElementById('dob').removeAttribute('readonly');"
        )
        dob = driver.find_element(By.ID, "dob")
        dob.clear()
        dob.send_keys(s['dob'])  # DD-MM-YYYY

        # Class = 12
        Select(driver.find_element(By.ID, "class")).select_by_visible_text("12")

        # Parent Name
        parent = driver.find_element(By.ID, "parent_name")
        parent.clear()
        parent.send_keys(str(s['parent_name']))

        # Question to PM
        q = driver.find_element(By.ID, "question_to_pm")
        q.clear()
        question_text = str(s.get('question', '')).strip()
        if not question_text or question_text.lower() == 'nan':
            question_text = random.choice(random_questions)
        q.send_keys(question_text[:500])

        # Submit
        driver.find_element(By.ID, "submit_form_btn").click()

        # ==============================
        # HANDLE ALERT
        # ==============================
        try:
            alert = driver.switch_to.alert
            print("⚠️ Alert detected: ", alert.text)
            alert.accept()
            print("✅ Alert accepted, submission confirmed")
        except:
            print("No alert appeared")

        print("✅ Submitted successfully")

        # Reload page for next student
        time.sleep(4)
        driver.get("https://innovateindia1.mygov.in/ppc-2026/student-through-teacher-form/?lang=en")
        time.sleep(3)

    except Exception as e:
        print("❌ ERROR occurred:", e)
        print("⛔ Stopping script to avoid wrong submissions")
        break

print("🎉 PROCESS COMPLETED")
driver.quit()
