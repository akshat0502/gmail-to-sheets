# Gmail to Google Sheets Automation

**Author:** Akshat Saxena  
**Project Type:** Python Automation (Intern Assignment)

---

## 📖 Project Overview

This project is a Python automation system that connects to the **Gmail API** and **Google Sheets API** using **OAuth 2.0 (Desktop Application Flow)**.

The script reads **real incoming unread emails** from the Gmail Inbox and logs them into a Google Sheet. Each email is processed **only once** to prevent duplicate entries and is marked as **read** after successful processing.

---

## 🎯 Objective

Each qualifying email is appended as a new row in Google Sheets with the following fields:

| Column  | Description |
|-------|------------|
| From  | Sender email address |
| Subject | Email subject |
| Date | Date & time received |
| Content | Email body (plain text) |

---

## 🧠 High-Level Architecture Diagram

+----------------------+
| Gmail Inbox |
| (Unread Emails) |
+----------+-----------+
|
| Gmail API (OAuth 2.0)
v
+----------------------+
| Python Application |
| - Gmail Service |
| - Email Parser |
| - State Manager |
+----------+-----------+
|
| Google Sheets API (OAuth 2.0)
v
+----------------------+
| Google Sheet |
| (Append New Rows) |
+----------------------+

yaml
Copy code

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **APIs Used:** Gmail API, Google Sheets API
- **Authentication:** OAuth 2.0 (Desktop App Flow)
- **Libraries:**
  - google-api-python-client
  - google-auth
  - google-auth-oauthlib

---

## 📂 Project Structure

gmail-to-sheets/
│
├── src/
│ ├── gmail_service.py
│ ├── sheets_service.py
│ ├── email_parser.py
│ └── main.py
│
├── credentials/
│ └── credentials.json (DO NOT COMMIT)
│
├── proof/
│ ├── gmail_unread/
│ ├── google_sheet_rows/
│ └── oauth_consent/
│
├── config.py
├── requirements.txt
├── state.json (Auto-generated, ignored)
├── token.json (Auto-generated, ignored)
├── .gitignore
└── README.md

yaml
Copy code

---

## 🔐 OAuth Flow Explanation

This project uses **OAuth 2.0 Desktop Application Flow**.

- On the first run, a browser window opens
- The user logs in with their Gmail account
- Permissions for **Gmail** and **Google Sheets** are granted
- Google generates an access token stored in `token.json`
- Subsequent runs reuse the token without re-login

The application runs in **testing mode**, and the Gmail account is added as a **test user**, so Google verification is not required.

---

## 🔁 Duplicate Prevention Logic

Duplicate email processing is prevented using **state persistence**.

- Each processed Gmail **message ID** is stored in `state.json`
- Before processing an email, the script checks if the ID already exists
- If present, the email is skipped

This ensures:
- No duplicate rows in Google Sheets
- Safe re-execution of the script

---

## 🧾 State Persistence Method

State is stored locally in a file named:

state.json

yaml
Copy code

### Why this approach was chosen:
- Simple and lightweight
- No external database required
- Easy to debug and maintain
- Suitable for small to medium inbox sizes

---

## ⚙️ Step-by-Step Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Add Google OAuth credentials
Place credentials.json inside:

bash
Copy code
credentials/credentials.json
3️⃣ Configure Google Sheet
Update SPREADSHEET_ID in config.py.

4️⃣ Run the script
bash
Copy code
python -m src.main
📸 Proof of Execution
The /proof/ folder contains:

Gmail inbox screenshots showing unread emails

Google Sheet screenshots with at least 5 rows populated

OAuth 2.0 consent screen screenshots

A 2–3 minute demo video explaining:

Project flow

Gmail → Sheets data movement

Duplicate prevention

Script re-run behavior

🚧 Challenges Faced & Solution
Challenge:
OAuth token initially lacked Google Sheets permission, resulting in a 403 error.

Solution:
Unified Gmail and Sheets scopes into a single OAuth flow and regenerated the OAuth token.

🚫 Limitations
Processes only unread inbox emails

Uses local file-based state storage

Not optimized for very large inboxes

Requires manual OAuth consent on first run

🔄 Post-Submission Modification Readiness
The modular design allows easy changes such as:

Processing only emails from the last 24 hours

Adding email labels as a new column

Excluding automated or no-reply emails

✅ Conclusion
This project demonstrates secure OAuth handling, real-world API integration, clean Python architecture, and reliable state management, fully satisfying the assignment requirements.

yaml
Copy code

---

## ✅ NEXT STEP (VERY IMPORTANT)

After pasting this file:

```bash
git add README.md
git commit -m "Update README to match assignment rubric"
git push
