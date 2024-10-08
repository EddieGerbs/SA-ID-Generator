import datetime

def luhn_checksum(id_number):
    total = 0
    reverse_digits = id_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10

# Function to generate South African ID numbers based on user input
def generate_sa_id_numbers(birth_date, gender, citizenship_status, file_path):
    valid_ids = []
    
    # Format the birth date as YYMMDD
    birth_date_str = birth_date.strftime("%y%m%d")
    
    # Determine the gender code range
    if gender == 'M':
        gender_range = range(5000, 10000)  # Male: 5000-9999
    elif gender == 'F':
        gender_range = range(0, 5000)  # Female: 0000-4999
    else:
        gender_range = range(0, 10000)  # Both: 0000-9999
    
    # Determine citizenship status options
    citizenship_options = []
    if citizenship_status == 'C':
        citizenship_options = ['0']  # Citizen only
    elif citizenship_status == 'R':
        citizenship_options = ['1']  # Resident only
    else:
        citizenship_options = ['0', '1']  # Both citizen and resident
    
    # Open the file in append mode to write the IDs
    with open(file_path, 'a') as file:
        # Iterate through gender codes within the selected range
        for gender_code in gender_range:
            gender_code_str = f"{gender_code:04d}"  # 4-digit padded number
            
            # Iterate through the selected citizenship options
            for citizenship in citizenship_options:
                race_digit = '8'
                id_without_check_digit = birth_date_str + gender_code_str + citizenship + race_digit
                check_digit = (10 - luhn_checksum(id_without_check_digit)) % 10
                full_id = id_without_check_digit + str(check_digit)
                file.write(full_id + '\n')

# Function to get user input
def get_user_input():
    # Get the user's birthdate
    birth_date_str = input("Enter the birth date (YYYY-MM-DD): ")
    birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    
    # Get the user's gender (M for male, F for female, B for both)
    gender = input("Enter gender (M for male, F for female, B for both): ").upper()
    while gender not in ['M', 'F', 'B']:
        gender = input("Invalid input. Enter gender (M for male, F for female, B for both): ").upper()
    
    # Get the user's citizenship status (C for citizen, R for resident, U for unsure)
    citizenship_status = input("Enter citizenship status (C for citizen, R for resident, U for unsure): ").upper()
    while citizenship_status not in ['C', 'R', 'U']:
        citizenship_status = input("Invalid input. Enter citizenship status (C for citizen, R for resident, U for unsure): ").upper()
    
    return birth_date, gender, citizenship_status

# Main function
def main():
    # Get user input for birthdate, gender, and citizenship
    birth_date, gender, citizenship_status = get_user_input()
    
    # Path to save the generated IDs (this will save to a text file in the same directory)
    file_path = 'UserSA_ID.txt'
    
    # Call the function to generate IDs and save them to a file
    generate_sa_id_numbers(birth_date, gender, citizenship_status, file_path)
    print(f"ID numbers generated and saved to {file_path}")

# Call the main function
if __name__ == "__main__":
    main()