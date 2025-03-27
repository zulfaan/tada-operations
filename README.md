# Excel Test Data Processing

## About the Project
This project focuses on processing and transforming raw data using Excel formulas and Python scripting. The objective is to clean, format, and analyze the given dataset efficiently. The steps include extracting IDs, formatting phone numbers, assigning country codes, cleaning names and emails, converting date formats, assigning extra points, and summarizing data using pivot tables.

## Steps & Processing
### Step 1: Extract ID
Use a formula to extract the ID of individuals from the "Data" tab.

### Step 2: Format Phone Numbers
Convert phone numbers into international format (e.g., `08123456789` → `+628123456789`).

### Step 3: Assign Country Code
Extract the country code from the formatted phone numbers.

### Step 4: Clean Names
Remove special characters and extra spaces from names.

### Step 5: Clean Emails
Correct email addresses by removing incorrect symbols and spacing.

### Step 6: Convert Date Format
Change the date format to `YYYY-MM-DD`.

### Step 7: Assign Extra Points
Assign additional points based on the given ID.

### Step 8: Pivot Table Analysis
A pivot table is created in Excel to analyze data distribution. The results are compared with Python-based calculations to ensure accuracy.

#### Excel Pivot Table Results:
- **Count of ACTIVE members per ID**
- **Count of INACTIVE members per ID**
- **Count of SUSPEND members per ID**
- **Sum of total points for ACTIVE members per ID**
- **Sum of total points for INACTIVE members per ID**
- **Sum of total points for SUSPEND members per ID**
- **Count of members from each country (ID, MY, SG)**
- **Country with the highest total points from ACTIVE members**

#### Python DataFrame Comparison:
A similar analysis is performed using Python (Pandas) to validate the pivot table results from Excel. Below are sample comparisons:

| Metric | Excel Result | Python Result |
|--------|-------------|--------------|
| Count of ACTIVE members (ID MERAH) | X | Y |
| Sum of points for ACTIVE members (ID BIRU) | X | Y |
| Country with highest total points | ID | MY |

The differences, if any, are analyzed to determine discrepancies between the two methods.
