import os
import smtplib

SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")

STAFF_DISCOUNT_RATE = 0.3

DISCOUNT_RATES = {
    "regular": 0.0,
    "member": 0.1,
    "vip": 0.2,
    "staff": STAFF_DISCOUNT_RATE,
}


def process_order(customer_type, items, email):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    discount = DISCOUNT_RATES.get(customer_type, 0.0)
    total = subtotal * (1 - discount)
    total = total + total * 0.0825
    try:
        s = smtplib.SMTP("localhost", 2525)
        s.login("shop@example.com", SMTP_PASSWORD)
        s.sendmail("shop@example.com", email, "Your total is " + str(total))
    except Exception as e:
        print("Email failed: " + str(e))
    print("Receipt: " + str(total))
    return total
