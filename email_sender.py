import smtplib
import pandas


my_email = "YOUR EMAIL"
password = "YOUR APP PASSWORD"

data = pandas.read_csv("CSV FILE")#ADD CSV FILE
data = data.to_dict(orient="records")
for i in data:
    name = i["First Name"] #TAKES FIRST NAME FOR HEADER
    email = i["Email"] #RECIEVER EMAIL
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Are you looking for Data Entry Specialist? or Virtual Assistance\n\n"#Subject
                                f"Hello {name},\n"#Header
f"""
BODY PARAGRAPH
"""
                            )
