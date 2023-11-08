price = int(input())
paid = int(input())

while 1 <= price <= 100:
    change = price - paid
    if change < price:
        print (change)
        break
    
