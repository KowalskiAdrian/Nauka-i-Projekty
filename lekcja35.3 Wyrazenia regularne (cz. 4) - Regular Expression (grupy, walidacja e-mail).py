import re


if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", "b.a@p.pl"):
    print("Dopasowano!")                # dopasowano email
else:
    print("Nie dopasowano!")                          