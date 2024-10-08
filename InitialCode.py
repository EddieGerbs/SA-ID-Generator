import datetime

# Luhn algorithm is used to generate the last digit (check digit)
def luhn_checksum(id_number):
    total = 0
    reverse_digits = id_number[::-1] #If you look up the algorithm you will see that it starts from the back 
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit from the right
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10

# Function to generate South African ID numbers and validate with the check digit
def generate_sa_id_numbers(file_path):
    valid_ids = []
    
    # Define a range of birth years. We use 1900 - 2000 since it will repeat after 2000
    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date(1999, 12, 31)
    delta = datetime.timedelta(days=1)
    
    # Open the file in append mode to write the IDs
    with open(file_path, 'a') as file:
        # Iterate through all possible birth dates
        while start_date <= end_date:
            birth_date = start_date.strftime("%y%m%d")  # format date as YYMMDD
            
            # Iterate through all gender digits (0000-4999 for females, 5000-9999 for males)
            for gender_code in range(10000):
                gender_code_str = f"{gender_code:04d}"  # 4-digit padded number
                
                # Iterate over both citizen (0) and permanent resident (1)
                for citizenship in ['0', '1']:
                    # Set race classification digit (modern IDs use 8)
                    race_digit = '8'
                    # Create the ID number without the check digit
                    id_without_check_digit = birth_date + gender_code_str + citizenship + race_digit
                    
                    # Generate the Luhn check digit
                    check_digit = (10 - luhn_checksum(id_without_check_digit)) % 10
                    
                    # Complete the ID number by adding the check digit
                    full_id = id_without_check_digit + str(check_digit)
                    
                    # Write the valid ID to the file, appending each new one on a new line
                    file.write(full_id + '\n')
            
            # Increment the date
            start_date += delta

# Path to save the generated IDs (this will save to a text file in the same directory)
file_path = 'All_SA_IDs.txt'

# Call the function to generate IDs and save them to a file
generate_sa_id_numbers(file_path)