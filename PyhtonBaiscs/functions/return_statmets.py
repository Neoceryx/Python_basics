
def value_added_tax(amount):

    ''' Similar to c# or Java, you can return, single value '''

    # amount that you will need to pay
    tax = amount * 0.25
    total_amount = amount * 1.25

    # return tax # return single value
    # return amount, tax, total_amount  # return a tuple by default
    return [amount, tax, total_amount]  # return a list [] or set {}


price = value_added_tax(100)
print(price[1], type(price))

