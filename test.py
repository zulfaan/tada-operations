from tabulate import tabulate
import pandas as pd
import luigi
from func import *

class CleanData(luigi.Task):
    def requires(self):
        pass
    
    def output(self):
        return [
            luigi.LocalTarget('output/clean_operations_officer.csv'),
            luigi.LocalTarget('output/clean_operations_officer.xlsx'),
            luigi.LocalTarget('output/answer_question.txt')
        ]
    
    def run(self):
        # Ekstrak Data
        df_data = pd.read_excel('source/Operations Officer_Using Jupyter Python - Excel Test.xlsx', sheet_name='Data')

        # Cleaning Data
        point_mapping = {'MERAH': 3, 'BIRU': 2, 'HIJAU': 1}

        df_data['ID Update'] = df_data['ID Update'].fillna(df_data['ID'].apply(clean_id))
        df_data['Phone Number Update'] = df_data['Phone Number Update'].fillna(df_data['Phone Number'].apply(clean_phone))
        df_data['Country Code'] = df_data['Country Code'].fillna(df_data['Phone Number Update'].apply(clean_country))
        df_data['Name Update'] = df_data['Name Update'].fillna(df_data['Name'].apply(clean_name))
        df_data['Email Update'] = df_data['Email Update'].fillna(df_data['Email'].apply(clean_email))
        df_data['Birthday (yyy-mm-dd)'] = df_data['Birthday (yyy-mm-dd)'].fillna(df_data['Birthday (dd/mm/yyyy)'].apply(clean_date))

        df_data['Extra Point'] = df_data['ID'].map(point_mapping)
        df_data['Final Point'] = df_data['Final Point'].fillna(df_data['Total Point'] + df_data['Extra Point'])

        df_data['ID'] = df_data['ID'].astype(str)
        df_data['Final Point'] = pd.to_numeric(df_data['Final Point'], errors='coerce')

        # Save Answer to File
        with open('output/answer_question.txt', 'w') as file:

            # Pivot Table - Count of Members by Status and ID
            pivot_count = df_data.groupby(['ID', 'Status']).size().unstack(fill_value=0).reset_index()
            file.write('\nCount of Members by Status and ID:\n')
            file.write(tabulate(pivot_count, headers='keys', tablefmt='grid'))
            file.write('\n\n')

            # Pivot Table - Sum of Final Points by Status and ID
            pivot_sum = df_data.groupby(['ID', 'Status'])['Final Point'].sum().unstack(fill_value=0).reset_index()
            file.write('\nSum of Final Points by Status and ID:\n')
            file.write(tabulate(pivot_sum, headers='keys', tablefmt='grid'))
            file.write('\n\n')

            # Count of Members by Country (ID, MY, SG)
            count_country = df_data['Country Code'].value_counts().reset_index()
            count_country.columns = ['Country', 'Count']
            count_country = count_country[count_country['Country'].isin(['ID', 'MY', 'SG'])]
            file.write('\nCount of Members by Country (ID, MY, SG):\n')
            file.write(tabulate(count_country, headers='keys', tablefmt='grid'))
            file.write('\n\n')

            # Country with Highest Total Points from ACTIVE Members
            active_points = df_data[df_data['Status'] == 'Active'].groupby('Country Code')['Final Point'].sum()
            if not active_points.empty:
                top_country = active_points.idxmax()
                file.write('\nCountry with Highest Total Points from ACTIVE Members: ' + top_country + '\n')
            else:
                file.write('\nNo Active members found in the dataset.\n')

        # Save final data to file
        df_data.to_csv('output/clean_operations_officer.csv', index=False)
        df_data.to_excel('output/clean_operations_officer.xlsx', index=False)


if __name__ == '__main__':
    luigi.build([CleanData()], local_scheduler=True)

