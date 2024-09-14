def make_bread():
    # Input for budget and price of 1 kg flour
    budget = float(input())
    flour_price_per_kg = float(input())

    # Calculate prices for other ingredients
    egg_price = 0.75 * flour_price_per_kg
    milk_price_per_l = 1.25 * flour_price_per_kg
    milk_price_per_250ml = milk_price_per_l / 4

    # Calculate the total cost for one loaf
    loaf_cost = flour_price_per_kg + egg_price + milk_price_per_250ml

    # Initialize variables
    loaves_made = 0
    colored_eggs = 0

    # Keep making loaves while we have enough budget
    while budget >= loaf_cost:
        loaves_made += 1
        colored_eggs += 3  # 3 colored eggs for each loaf

        # For every 3rd loaf, lose eggs as per the rule
        if loaves_made % 3 == 0:
            colored_eggs -= (loaves_made - 2)

        # Subtract the cost of one loaf from the budget
        budget -= loaf_cost

    # Print the results
    print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

make_bread()
