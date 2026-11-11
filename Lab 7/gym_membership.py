import math


def parse_plan(code):
    """Parse 'GOLD-12' -> ('GOLD', 12). Returns None for any invalid input."""
    if not isinstance(code, str):
        return None
    parts = code.split('-')
    if len(parts) != 2:
        return None
    plan, months = parts[0].strip(), parts[1].strip()
    if not plan.isalpha():          # rejects empty plan and digits/symbols
        return None
    try:
        months = int(months)
    except ValueError:
        return None
    if months <= 0:
        return None
    return plan.upper(), months


def calculate_bmi(data):
    """Parse 'weight,height' (kg,m) -> BMI rounded to 1 dp. None if invalid."""
    if not isinstance(data, str):
        return None
    parts = data.split(',')
    if len(parts) != 2:
        return None
    try:
        weight, height = float(parts[0]), float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(weight) and math.isfinite(height)):   # nan / inf
        return None
    if weight <= 0 or height <= 0:
        return None
    try:
        bmi = weight / (height ** 2)
    except (ZeroDivisionError, OverflowError):
        return None
    if not math.isfinite(bmi):
        return None
    return round(bmi, 1)


def average_workout(minutes):
    """Parse '45 60 30' -> integer average. None if invalid or empty."""
    if not isinstance(minutes, str):
        return None
    tokens = minutes.split()
    if not tokens:
        return None
    try:
        values = [int(t) for t in tokens]
    except ValueError:
        return None
    if any(v < 0 for v in values):
        return None
    return sum(values) // len(values)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result if result is not None else "Invalid input")

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result if result is not None else "Invalid input")

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
