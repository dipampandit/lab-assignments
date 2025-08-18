# Check whether a person is eligible to donate blood (age ≥18 and weight ≥50).
def eligible_blood(age, weight):
    return "Eligible" if age >= 18 and weight >= 50 else "Not Eligible"

print(eligible_blood(20, 55))
