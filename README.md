# Gmail to Google Sheets Automation

**Author:** Akshat Seth  
**Project Type:** Python Automation (Intern Assignment)

---

## 📖 Project Overview

This project is a Python automation system that connects to the **Gmail API** and **Google Sheets API** using **OAuth 2.0 authentication**.

The script reads real incoming **unread emails from Gmail Inbox** and logs them into a **Google Sheet**. Each email is processed only once, ensuring **no duplicate entries**, and is marked as **read** after successful processing.

---

## 🎯 Objective

Each qualifying email is appended as a new row in Google Sheets with the following fields:

| Column | Description |
|------|-------------|
| From | Sender email address |
| Subject | Email subject |
| Date | Date & time received |
| Content | Email body (plain text) |

---

## 🧠 High-Level Architecture Diagram




Gmail Inbox (Unread Emails)
|
| Gmail API (OAuth 2.0)
v
Python Application

Gmail Service

Email Parser

State Manager
|
| Google Sheets API (OAuth 2.0)
v
Google Sheet (Append Rows)



---

## 🛠️ Tech Stack

- **Language:** Python 3
- **APIs:** Gmail API, Google Sheets API
- **Authentication:** OAuth 2.0 (Desktop App Flow)
- **Libraries:**
  - google-api-python-client
  - google-auth
  - google-auth-oauthlib

---

## 📂 Project Structure

state.json


### Why this approach:
- Simple and lightweight
- No external database needed
- Easy to debug
- Suitable for small to medium inbox sizes

---

## ⚙️ How to Run the Project

### 1️⃣ Install dependencies
pip install -r requirements.txt


2️⃣ Add Google OAuth credentials

Place credentials.json inside:

credentials/credentials.json

3️⃣ Configure Google Sheet

Update SPREADSHEET_ID in config.py.

4️⃣ Run the script
python -m src.main
