"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return day_cost


def cost_per_credit(annual_cost, credits):
    credit_cost = annual_cost / SEMESTERS_PER_YEAR / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    class_cost = cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


def cost_of_arriving_late(annual_cost):
    late_cost = cost_per_class(annual_cost, CS1430_CREDITS) * 0.1
    return late_cost

# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: "))
    credits = float(input("Enter the number of credits taken this semester: "))

    while True:
        print("\nMenu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost of arriving 5 min late to class")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: {cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: {cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per day: {cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: {cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: {cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            print(f"Cost of arriving 5 min late to class: {cost_of_arriving_late(annual_cost):.2f}")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
