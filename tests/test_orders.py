import pytest


from orders import process_order




def test_regular_customer_pays_no_discount():
    items = [{"price": 10.0, "qty": 2}]
    assert process_order("regular", items, "a@b.com") == pytest.approx(21.65)




def test_member_gets_ten_percent_off():
    items = [{"price": 10.0, "qty": 2}]
    assert process_order("member", items, "a@b.com") == pytest.approx(19.485)