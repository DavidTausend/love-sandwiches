import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# Check API working
"""
sales = SHEET.worksheet("sales")

data = sales.get_all_values()

print(data)
"""

def get_sales_data():
    while True:

        """
        Get sales figures input from the user
        """
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        #print(f"The data provided is {data_str}")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        # Convert into an interger
        [int(value) for value in values]
        # Check if the values list has 6 values
        if len(values) != 6:
            raise ValueError(
                f"Excalty 6 values requierd, you provided {len(values)}"
            )
    except ValueError as e:
        print(F"Invalid data: {e}, please try again\n")
        return False

    return True

data = get_sales_data()