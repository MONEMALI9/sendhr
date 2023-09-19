import pandas as pd


df =  pd.read_csv('hremail.csv')  
list_email = df[df.columns[0]] 
list_email = list(list_email)   
         
# List of recipient email addresses
#recipient_emails = ['Ahmedbasouney8@gmail.com', 'monem921999@gmail.com'] 
recipient_emails = list(list_email)  
for i in range (0,len(recipient_emails)):
    print(i)
    print(recipient_emails[i])