# code to get user input and display the data

# Define the function to recommend a doctor's visit
def recommend_doctor_visit(symptoms):
    if not all(symptoms.values()):
        print("It is recommended to visit a doctor.")
    else:
        print("You seem to be doing well.")

# Get user input
stress = input("Do you have a stress related to work? (yes/no): ")
anxiety = input("Do you have anxiety issues? (yes/no): ")
depression = input("Do you have any symptoms of depression? (yes/no): ")

# Store user input in a dictionary
symptoms = {
  "anxiety": anxiety == "no",
  "stress": stress == "no",
  "depression": depression == "no"
}

# Display the user input
print("You entered:")
print(symptoms)

# Call the function to recommend a doctor's visit

recommend_doctor_visit(symptoms)
