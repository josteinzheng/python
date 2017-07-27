from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc4a132b6e8169e5738566d0f7933fba6"
# Your Auth Token from twilio.com/console
auth_token  = "f60af563234bc37ab67a9b836c99c888"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8615001361862", 
    from_="+14159808638",
    body="代冬寒，猜猜我是谁!")

print(message.sid)
