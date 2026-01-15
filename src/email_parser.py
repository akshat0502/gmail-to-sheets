import base64

def _get_header(headers, name):
    for h in headers:
        if h["name"] == name:
            return h["value"]
    return ""

def _decode(body):
    data = body.get("data")
    if not data:
        return ""
    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

def parse_email(message):
    payload = message["payload"]
    headers = payload["headers"]

    sender = _get_header(headers, "From")
    subject = _get_header(headers, "Subject")
    date = _get_header(headers, "Date")

    body = ""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                body = _decode(part["body"])
                break
    else:
        body = _decode(payload.get("body", {}))

    return [sender, subject, date, body.strip()]
