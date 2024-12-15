costprice = int(input("Enter the cost price (cp): "))
sellingprice = int(input("Enter the selling price (sp): "))

if sellingprice > costprice:
    print("Profit")
    profit = sellingprice - costprice
    print("Profit amount:", profit)
elif sellingprice < costprice:
    print("Loss")
    loss = costprice - sellingprice
    print("Loss amount:", loss)
else:
    print("No profit, no loss")
