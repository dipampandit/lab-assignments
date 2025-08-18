# Check if a person is eligible to vote (age ≥ 18).
def eligible_vote(age):
    return "Eligible" if age >= 18 else "Not Eligible"

print(eligible_vote(20))
