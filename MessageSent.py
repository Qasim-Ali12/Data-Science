import pywhatkit as kit
import pandas as pd
import time

# Load Excel File
df = pd.read_excel("Book3.xlsx")  # Ensure contacts.xlsx has a column 'Phone_number'

# WhatsApp Group Invite Link
group_invite_link = "https://chat.whatsapp.com/JJULI8qF7KyJesuxuYL1vH"



# Loop through each phone number and send the message
for index, row in df.iterrows():
    phone_number = f"+{row['phone_number']}"  # Ensure phone numbers are in international format (e.g., +923001234567)
    message = f"""📢📢 Welcome to Your Official Batch Group! 
""" # Write your message you want to send them


    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
        
        print(f"Message sent to {phone_number}")
        time.sleep(5)  # Add delay to avoid being flagged as spam
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")