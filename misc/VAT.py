print("Hello")

# only need to change the VAT value
VAT = 17.5
calcVAT = 1 + (VAT / 100)

priceOfShoes = 100
priceOfTV = 2000
priceOfiPad = 350

# price plus VAT

fullPriceShoes = priceOfShoes * calcVAT
print("shoes", fullPriceShoes)

fullPriceTV = priceOfTV * calcVAT
print("TV", fullPriceTV)

fullPriceiPad = priceOfiPad * calcVAT
print(fullPriceiPad)
