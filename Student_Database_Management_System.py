def manage_student_database():
    # Initialize an empty list to store student tuples
    students = []
    student_id = 1  # Counter to generate sequential student IDs

    # Step 2: Handle user input until "stop" is entered
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        # Step 2: Check if the user wants to stop
        if name.lower() == 'stop':
            break
        
        # Step 3: Check for duplicate names
        if any(student[1].lower() == name.lower() for student in students):
            print("This name is already in the list.")
        else:
            # Step 3: Add the student to the list if not a duplicate
            students.append((student_id, name))
            student_id += 1

    # Step 4: Display the complete list of students as tuples
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Step 5: Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Step 6: Calculate and display statistics
    if students:
        # Total number of students
        total_students = len(students)
        print(f"\nTotal number of students: {total_students}")

        # Total length of all student names combined
        total_name_length = sum(len(student[1]) for student in students)
        print(f"Total length of all student names combined: {total_name_length}")

        # Find the student with the longest name
        longest_name_student = max(students, key=lambda student: len(student[1]))
        print(f"The student with the longest name is: {longest_name_student[1]}")

        # Find the student with the shortest name
        shortest_name_student = min(students, key=lambda student: len(student[1]))
        print(f"The student with the shortest name is: {shortest_name_student[1]}")
    else:
        print("\nNo students in the database.")

# Step 7: Call the manage_student_database function
manage_student_database()
