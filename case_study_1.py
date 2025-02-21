print("\t\t\t\t\tWELCOME TO GROCERY STORE ")
 print("")
 items = []
 prices = []
 quantities = []
 total = 0
 while True:
 item = input("Enter item name (or 'done' to finish): ")
 if item.lower() == 'done':
 break
 price = float(input(f"Enter price of {item}: ₹"))
 quantity = float(input(f"Enter quantity of {item}: "))
 items.append(item)
 prices.append(price)
 quantities.append(quantity)
 total += price * quantity
 discount = total * 0.1 if total > 1000 else 0
 final_total = total - discount
 print("\n===== BILL =====")
 print("ITEMS\tAMOUNT  QUANTITY TOTAL")
 for i in range(len(items)):
 print(f"{items[i]}:₹{prices[i]} x {quantities[i]} = ₹{prices[i] * 
quantities[i]}")
 print("================")
 print(f"Total: ₹{total:.2f}")
 if discount:
 print(f"Discount: ₹{discount:.2f}")
 print(f"Final Amount: ₹{final_total:.2f}")
 print("================\n")
