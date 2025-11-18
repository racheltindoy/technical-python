#Goal: Practice iterating over key-value pairs (.items()) and performing a calculation.
"""
Task: Write a function calculate_total_value(inventory) that iterates through 
a dictionary where keys are product names and values are tuples of (price, quantity). 
The function should return the total dollar value of all inventory items.
"""

coffee_inventory = {
    "Ethiopian Yirgacheffe": (18.50, 80),    # Price: $18.50, Stock: 80 bags
    "Signature Espresso Blend": (14.00, 150), # Price: $14.00, Stock: 150 bags
    "Decaf Colombian": (16.95, 45),          # Price: $16.95, Stock: 45 bags
    "Seasonal Single Origin": (22.00, 20),   # Price: $22.00, Stock: 20 bags
    "Sumatran Mandheling": (17.50, 65)       # Added a fifth item
}

def calculate_total_value(inventory):
	total = 0
	for coffee, item_data in inventory.items():
		price, quantity = item_data
		total += price * quantity
	return total

final_value = calculate_total_value(coffee_inventory)
print(f'The total inventory value is: ${final_value}')