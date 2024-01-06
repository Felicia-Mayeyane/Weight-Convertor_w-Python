#weight conversion project

Weight = float(input("Enter your weight:"))
Unit = input("Weight in Kilograms or Pound? (K or L):")

if Unit == "K":
    Weight = Weight * 2.205
    Unit = "Lbs."
    print(f"Your new weight is: {round(Weight, 1)}{Unit}")
elif Unit == "L":
    Weight = Weight / 2.205
    Unit = "Kgs."
    print(f"Your new weight is: {round(Weight, 1)}{Unit}")
else:
    print(f"{Unit} was invalid")

print(f"Your new weight is: {round(Weight,1)}{Unit}")