# Sending whatsapp alert to given number

from twilio.rest import Client 
 
account_sid = 'your account_sid' 
auth_token = 'your auth_token' 
client = Client(account_sid, auth_token) 

def alert(result): 
    print(result)
    send_message = ""
    for i, j in result.items():
        send_message += f"{i}: {j}\n"
    print(send_message)

    message = client.messages.create( 
                            from_='whatsapp:+your twilio no.',  
                            body=send_message,   
                            to='whatsapp:+your whatsapp no.'    
                        ) 
    #print(message.sid)
    return message

