# Name in Reverse Order:
# Prabhakarna Sripalawardhana Atapattu Jayasuriya Laxmansriramkrishna 
# Shivavenkata Rajasekara Sriniwasana Trichipalli Yekya Parampeel 
# Parambatur Chinnaswami Muthuswami Venugopal Iyer

name = """Prabhakarna Sripalawardhana Atapattu Jayasuriya Laxmansriramkrishna 
Shivavenkata Rajasekara Sriniwasana Trichipalli Yekya Parampeel 
Parambatur Chinnaswami Muthuswami Venugopal Iyer"""

words = name.split()

for i in range(1, len(words) + 1):
    print(" ".join(words[-i:]))