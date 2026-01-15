import json
import os
from src.gmail_service import get_gmail_service, fetch_unread_messages, mark_message_as_read
from src.sheets_service import get_sheets_service, append_row
from src.email_parser import parse_email
from config import SPREADSHEET_ID, STATE_FILE

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"processed_ids": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main():
    gmail_service = get_gmail_service()
    sheets_service = get_sheets_service()
    state = load_state()

    messages = fetch_unread_messages(gmail_service)

    for msg in messages:
        if msg["id"] in state["processed_ids"]:
            continue

        full_msg = gmail_service.users().messages().get(
            userId="me", id=msg["id"], format="full"
        ).execute()

        row = parse_email(full_msg)
        append_row(sheets_service, SPREADSHEET_ID, row)
        mark_message_as_read(gmail_service, msg["id"])

        state["processed_ids"].append(msg["id"])

    save_state(state)
    print("✔ Emails processed successfully")

if __name__ == "__main__":
    main()
