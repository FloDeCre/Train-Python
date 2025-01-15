orders = [
    {"name": "Laptop", "price": 899.99, "quantity": 1},
    {"name": "Mouse", "price": 19.99, "quantity": 2},
    {"name": "Keyboard", "price": 49.99, "quantity": 1},
]  

discount_list = [
    {"name":"More 1000","amount":0.1},
    {"name":"Less 1000, More 500","amount":0.05},
]

def calculate_total(orders):
    total = 0
    for order in orders :
       total += order["price"]*order["quantity"]
    return total 

def apply_discount(total,discount = 0):
    totalAfterDiscount = 0
    firstDiscount = discount_list[0]["amount"]
    secondDiscount = discount_list[1]["amount"]
    otherDiscountPercent = discount/100
    if discount != 0 :
        totalAfterDiscount = total*otherDiscountPercent
        return {"total" : total - totalAfterDiscount, "discount": otherDiscountPercent*100} 
    elif discount < 0 :
        return {"total" : total, "discount": 0}
    else :
        if total > 1000 :
            return {"total" :total - (total*firstDiscount), "discount": firstDiscount*100}
        elif total > 500 and total < 1000 :
            return {"total" : total - (total*secondDiscount), "discount": secondDiscount*100}
        else :
            return {"total" : total, "discount": 0}
        
def invoice_orders(orders,discount = 0):
    amountTotal = calculate_total(orders)
    afterDiscount = apply_discount(amountTotal,discount)
    amountDiscount = amountTotal - afterDiscount["total"]
    print("---- Invoice ----")
    for order in orders :
       print(f"Name:{order["name"]}, Quantity : {order["quantity"]}, Total : {order["price"]*order["quantity"]}") 
    print(f"Total Amount: {amountTotal:.2f}")
    print (f"Discount : {afterDiscount["discount"]}% (- {amountDiscount:.2f} €)")
    print(f"Total Amount after discount : {afterDiscount["total"]:.2f}")

print(invoice_orders(orders))

print(invoice_orders(orders,30))