import decimal

context = decimal.getcontext() 
context.rounding = 'ROUND_HALF_UP' 

for i in range(1, 10):
    k = i + 0.5
    print(k, round(Decimal(k), 0))