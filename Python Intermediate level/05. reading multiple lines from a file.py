# with open('emails.txt', 'r') as emails:
#     print(emails.readlines())


# with open('emails.txt', 'r') as emails:
#     emails = emails.readlines()
    
# for email in emails:
#     print("Looking for a wp account")
#     if "wp" in email:
#         print(email)

with open('emails.txt', 'r') as emails:
    emails = emails.readlines()

for email in emails:
    if "gmail" in email:
        print(email)

with open('emails.txt', 'r') as emails:
    emails = emails.readlines()

for email in emails:
    if "gmail" in email:
        print(email.rstrip())