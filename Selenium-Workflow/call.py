from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC456d58d8a126e03030ba7dac3dc3930f'
auth_token = 'cebfde1985621293eee0bd214e326482'

# Create a Twilio client object
client = Client(account_sid, auth_token)

# # Make a phone call
call = client.calls.create(
    to='+916305520922',  # The phone number you want to call
    from_='+16073576154',  # Your Twilio phone number
    twiml='<Response><Say>SRH vs RCB Tickets are now available</Say></Response>' # A URL to TwiML instructions for the call
)

print(client.balance.fetch().balance)

# print(call.sid)  # Print the call SID

