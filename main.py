from forex_python.converter import CurrencyRates
c = CurrencyRates()

amount = int(input("Enter amount to convert: "))
from_currency = input("From which currency?: ").upper()
to_currency = input("To which currency?: ").upper()

print(f"You are about to convert", from_currency, amount, " to ", to_currency)
result = c.convert(from_currency, to_currency, amount)
print(result)
