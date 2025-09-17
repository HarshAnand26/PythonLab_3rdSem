# Student Name : [Harsh Anand]
# Roll Number  : [2024UG4015]
# Course       : CS-2101 / CD-2101 - Python Programming Lab

# Task - 1 :- Create a Python program that asks the user for their age.Implement conditional statements to check the following: If the user is below 18, print "You are a minor." If the user is between 18 and 65, print "You are an adult." If the user is above 65, print "You are a senior." Add a check for invalid input (e.g., user enters a non-numeric value).

while True :
    try :
        age = int(input("Enter your age: "))
        if age <= 0 :
            print("Please enter a valid age!!")
            continue
    
    except ValueError :
        print("Please enter a valid age!!")

    else :
        break

if age < 18 :
    print("You are a minor!!")

elif age >= 18 and age <= 65 :
    print("You are an adult!!")

else:
    print("You are a senior citizen!!")


# Task - 2 :- Print Multiplication Table from 1 to 12 .

print("    " , end = "")

for col in range(1 , 13):
    print(f"{col:4}" , end = "")
print()

print("    " + "-" * 50)

for row in range(1 , 13):
    print(f"{row:2} |" , end = "")
    for col in range(1 , 13):
        print(f"{row*col:4}" , end = "")
    print()


# Task - 3 :- Write a program to validate a password based on the following criteria:
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least one special character (e.g., @, #, !, etc.)



def Validate_Password(Password):

    if len(Password) < 8:
        return "Password must be atleast 8 characters long!!"
    
    if not any(ch.islower() for ch in Password):
        return "Password must contain atleast one lowercase letter!!"
    
    if not any(ch.isupper() for ch in Password):
        return "Password must contain atleast one uppercase letter!!"
    
    if not any(ch.isdigit() for ch in Password):
        return "Password must contain atleast one number!!"
    
    if not any(ch in "~!@#$%^&*()_/|+=><[]?" for ch in Password):
        return "Password must contain atleast one special character!!"
    
    return "Password is valid!!"


while True :
    pwd = input("Enter a password: ")
    result = Validate_Password(pwd)
    print(result)
    if result == "Password is valid!!" :
        break



# Task 4:- Nested Dictionary + Search Assistant Professor

# Nested dictionary for IIIT Ranchi's organizational structure (sample)
iiit_structure = {
    "Administration": {
        "Director": "Prof. Rajeev Srivastava",
        "Registrar": "Registrar (In-Charge)"
    },

    "Computer Science & Engineering": {
        "HoD": "Dr. Kirti Kumari",
        "Faculty": {
            "Professors": ["Prof. Rajeev Srivastava"],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Dhananjoy Bhakta",
                "Dr. Jayadeep Pati",
                "Dr. Roshan Singh",
                "Dr. Rashmi Panda",
                "Dr. Bharat Singh",
                "Dr. Priyank Khare",
                "Dr. Kirti Kumari",
                "Dr. Tarun Biswas",
                "Dr. Ranjan Kumar Behera",
                "Dr. Gaurav Sundaram",
                "Dr. Akash Srivastava"
            ]
        }
    },

    "Electronics & Communication Engineering": {
        "HoD": "Dr. Santosh Kumar Mahto",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Santosh Kumar Mahto",
                "Dr. Shashi Kant Sharma",
                "Dr. Jitendra Kumar Mishra",
                "Dr. Rajiv Kumar",
                "Dr. Priyabrat Garanayak",
                "Dr. Nishit Malviya"
            ]
        }
    },

    "Sciences": {
        "HoD": "Dr. Sandhir Kumar Singh",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Sandhir Kumar Singh",
                "Dr. Puja Ghosh",
                "Dr. Rohit Kandulna",
                "Dr. Rishikesh Dutta Tiwary",
                "Dr. Shashi Kant"   # (Mathematics)
            ]
        }
    },

    "Humanities & Management": {
        "HoD": "Dr. Sandhir Kumar Singh",
        "Faculty": {
            "Professors": [],
            "Associate Professors": [],
            "Assistant Professors": [
                "Dr. Noopur"
            ]
        }
    }
}


def find_professor_department(structure, name):
    """
    Search for an Assistant Professor in the nested dictionary.
    Return the department if found, else None.
    """
    for dept, info in structure.items():
        faculty = info.get("Faculty", {})
        aps = faculty.get("Assistant Professors", [])
        if name in aps:
            return dept
    return None


# Main Program
def main():
    name = input("Enter the name of an Assistant Professor: ").strip()
    dept = find_professor_department(iiit_structure, name)

    if dept:
        print(f"✅ {name} belongs to the Department of {dept}.")
    else:
        print(f"❌ Assistant Professor named '{name}' was not found in IIIT Ranchi's structure.")


if __name__ == "__main__":
    main()



# Task - 5 :- Use matplotlib to plot the monthly sales and highlight the month with the highest sales.


import matplotlib.pyplot as plt

# ------------------ Sales Data (in thousands) ------------------
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ------------------ Calculations using loops ------------------
total_sales = 0
highest_sales = sales_data[0]
highest_month_index = 0

for i in range(len(sales_data)):
    total_sales += sales_data[i]
    if sales_data[i] > highest_sales:
        highest_sales = sales_data[i]
        highest_month_index = i

average_sales = total_sales / len(sales_data)

# ------------------ Print results ------------------
print(f"Total Sales (in thousands): {total_sales}")
print(f"Average Monthly Sales (in thousands): {average_sales:.2f}")
print(f"Highest Sales: {highest_sales} in {months[highest_month_index]}")

# ------------------ Plotting ------------------
plt.figure(figsize=(10, 6))
plt.plot(months, sales_data, marker='o', linestyle='-', label="Sales Data")

# Highlight the highest sales point
plt.scatter(months[highest_month_index], highest_sales, color='red', s=150, label="Highest Sales")
plt.text(months[highest_month_index], highest_sales + 2,
         f"{highest_sales}", ha='center', fontsize=10, color='red')

# Formatting the plot
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.legend()
plt.grid(True)
plt.show()
