"""
Name: Wesley Fox
File: student_qualifications.py
Description: This app accepts student names and GPAs, then determines if each student 
qualifies for the Dean's List (GPA >= 3.5) or Honor Roll (GPA >= 3.25). 
The app continues processing until the user enters 'ZZZ' as the last name.
"""

# Initialize student counter
student_count = 0

print("=" * 50)
print("STUDENT QUALIFICATIONS CHECKER")
print("Enter 'ZZZ' as last name to quit")
print("=" * 50)
print()

# Main loop
while True:
    # Ask for last name
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    
    # Check if user wants to quit
    if last_name.upper() == 'ZZZ':
        print("\n" + "=" * 50)
        print(f"PROCESSING COMPLETE")
        print(f"Total students processed: {student_count}")
        print("=" * 50)
        break
    
    # Ask for first name
    first_name = input("Enter student's first name: ")
    
    # Ask for GPA with error handling
    while True:
        try:
            gpa = float(input("Enter student's GPA: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric GPA (e.g., 3.5)")
    
    # Increment student counter
    student_count += 1
    
    # Display student info
    print("\n" + "-" * 30)
    print(f"Student: {first_name} {last_name}")
    print(f"GPA: {gpa}")
    
    # Check qualifications
    if gpa >= 3.5:
        print("✅ QUALIFICATION: Dean's List")
    elif gpa >= 3.25:
        print("✅ QUALIFICATION: Honor Roll")
    else:
        print("❌ No qualification")
    print("-" * 30)
    print()

print("\nThank you for using the Student Qualifications Checker!")