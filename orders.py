import smtplib

SMTP_PASSWORD = "hunter2"


def process_order(customer_type, items, email):
    total = 0
    for i in items:
        total = total + i["price"] * i["qty"]
    if customer_type == "regular":
        total = total
    elif customer_type == "member":
        total = total * 0.9
    elif customer_type == "vip":
        total = total * 0.8
    elif customer_type == "staff":
        total = total * 0.7
        total = total + total * 0.0825
    try:
        s = smtplib.SMTP("localhost", 2525)
        s.login("shop@example.com", SMTP_PASSWORD)
        s.sendmail("shop@example.com", email, "Your total is " + str(total))
    except:
        pass
    print("Receipt: " + str(total))
    return total
