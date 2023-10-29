from twilio.rest import Client


account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

def phone(number, code):
    message = client.messages.create(to=f"+82{number}", from_="",body=f"인증코드 {code}")
    return "ok"
