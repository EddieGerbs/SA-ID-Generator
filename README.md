# South African ID Number Generator

This repository contains two Python programs that generate valid South African ID numbers. It provides insights into the structure of South African ID numbers and how they are formatted. The GenSAID program allows you to generate ID numbers based on user input (birthdate, gender, and citizenship status) and validate them using the Luhn algorithm.

## Overview of South African ID Numbers

A South African ID number is a 13-digit number structured as follows: YYMMDD SSSS C R N


Each section of the ID number encodes specific information:

- **YYMMDD**: The first six digits represent the date of birth in the format `YYMMDD`.
  - `YY`: Last two digits of the year of birth.
  - `MM`: Month of birth (01 to 12).
  - `DD`: Day of birth (01 to 31).

- **SSSS**: The next four digits represent a serial number that encodes gender.
  - **Females**: Serial numbers range from `0000` to `4999`.
  - **Males**: Serial numbers range from `5000` to `9999`.

- **C**: The 11th digit represents citizenship status.
  - `0`: South African citizen.
  - `1`: Permanent resident.

- **R**: The 12th digit was historically used for race classification.
  - Under apartheid, this digit was used to denote race, but in modern ID numbers, it is always set to `8`.

- **N**: The 13th digit is the **check digit**, used for validation. It is calculated using the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

### Example

For someone born on 17th May 1985, the ID number might look like this:
850517 5234 08 5

Here:
- `850517`: Birthdate (17th May 1985).
- `5234`: A male serial number.
- `0`: South African citizen.
- `8`: Race classification digit.
- `5`: Luhn check digit.

## Features of the Repository

- **Initial ID Generator**: A Python script that generates South African ID numbers based on predefined ranges of dates and serial numbers.
- **Updated ID Generator**: An enhanced version that allows user input for birthdate, gender, and citizenship status, generating valid South African ID numbers accordingly.

### How to Run the Program

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sa-id-number-generator.git
    ```
2. **Run the Python script**:
    ```bash
    python GenSAID.py
    ```
3. Follow the prompts to generate ID numbers based on your input.
4. You should see a generated text file in the same directory as the GenSAID.py file.

## About the Luhn Algorithm

The **Luhn algorithm** is used to calculate the check digit (13th digit) of the ID number. It helps ensure that the ID number is correctly formatted and valid. For more information, you can refer to the [Wikipedia article on the Luhn Algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

---

## Contributing

Feel free to contribute by opening issues or submitting pull requests. We welcome improvements to the code and suggestions for additional features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

