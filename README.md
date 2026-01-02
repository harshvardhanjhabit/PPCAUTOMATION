# PPC Automation – MyGov Student Submission Bot

This project automates the submission of student data for the **“Student through Teacher”** form on the [MyGov PPC 2026 portal](https://innovateindia1.mygov.in/ppc-2026/student-through-teacher-form).  
It is built using **Python**, **Selenium**, and **Pandas**, and helps teachers save time by auto-filling student information from an Excel file.

---

## ⚡ Features

- **Automatic Form Filling**: Reads student details from `students.xlsx` and fills the online form automatically.  
- **Handles Optional Fields**: Supports optional fields like email and mobile number.  
- **Smart PM Question**:  
  - If a “question to the Prime Minister” is missing in Excel, the script inserts a **random study-related question**.  
  - Examples:  
    - "How can I improve my concentration during exams?"  
    - "What is the best way to manage study time efficiently?"  
    - "How can students deal with academic stress effectively?"  
- **Date of Birth Handling**: Converts Excel DOBs to the correct `DD-MM-YYYY` format.  
- **Gender and Class Selection**: Automatically selects gender.  
- **Alert Handling**: Detects confirmation alerts and safely accepts them.  
- **Robust Error Handling**: Stops the script on critical errors to prevent wrong submissions.  

---

## ⚠️ Important Note About Class

The **class field** is currently **hardcoded in the script**.  
- Default is: `12`  
- To submit for another class (6–12), **update the line** in `ppc_auto_submit.py`:

```python
# Change this line to your desired class
Select(driver.find_element(By.ID, "class")).select_by_visible_text("12")



Got it! Here’s a clean Excel template you can use as a starting point:

first_name	last_name	email	mobile	gender	dob	parent_name	question
							
							
							

Notes for the template:

Fill each row with one student’s details.

Leave question empty if you want the script to add a random studies-related question.

Keep column headers exactly as above.
