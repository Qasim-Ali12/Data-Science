import pywhatkit as kit
import pandas as pd
import time

# Load Excel File
df = pd.read_excel("Book3.xlsx")  # Ensure contacts.xlsx has a column 'Phone_number'




# Loop through each phone number and send the message
for index, row in df.iterrows():
    phone_number = f"+{row['phone_number']}"  # Ensure phone numbers are in international format (e.g., +923001234567)



    try:
        kit.sendwhats_image(phone_number,  "eid.png") # Image sent sentex
        print(f"Message sent to {phone_number}")
        time.sleep(5)  # Add delay to avoid being flagged as spam
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")