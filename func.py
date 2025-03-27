from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re


def  clean_id(id):
    if id == 'MERAH':
        return '10021032400001'
    elif id == 'BIRU':
        return '10021032400002'
    elif id == 'HIJAU':
        return '10021032400003'
    
def clean_phone(phone):
    phone = phone.replace('-', '')
    
    if phone.startswith('08'):
        return '+62' + phone[1:]
    elif phone.startswith('01'):
        return '+60' + phone[1:]
    elif phone.startswith('09'):
        return '+65' + phone[1:]
    elif phone.startswith('60'):
        return '+60' + phone[2:]
    elif phone.startswith('62'):
        return '+62' + phone[2:]
    elif phone.startswith('65'):
        return '+65' + phone[2:]
    elif phone.startswith('+65'):
        return '+65' + phone[3:]
    elif phone.startswith('+62'):
        return '+62' + phone[3:]
    elif phone.startswith('+60'):
        return '+60' + phone[3:]
    else:
        return phone

def clean_country(country):
    if country.startswith('+62'):
        return 'ID'
    elif country.startswith('+60'):
        return 'MY'
    elif country.startswith('+65'):
        return 'SG'
    
def clean_name(name):
    if pd.isna(name) or name.strip() == '':
        return ''  
    cleaned_name = re.sub(r'[^A-Za-z\s]', '', name)
    cleaned_name = cleaned_name.title().strip()
    return cleaned_name


def clean_email(email):
    if pd.isna(email) or email.strip() == '':
        return ''  
    email = re.sub(r'\s*@\s*', '@', email)  
    email = re.sub(r'[,.]+com$|(@test)\.\w+$', r'\1.com', email) 
    return email.strip() 


def clean_date(date_str):
    if pd.isna(date_str) or date_str.strip() == '':
        return ''

    bulan_mapping = {
        'Januari': 'Jan', 'Februari': 'Feb', 'Maret': 'Mar', 'April': 'Apr',
        'Mei': 'May', 'Juni': 'Jun', 'Juli': 'Jul', 'Agustus': 'Aug',
        'September': 'Sep', 'Oktober': 'Oct', 'November': 'Nov', 'Desember': 'Dec'
    }

    for indo, eng in bulan_mapping.items():
        date_str = date_str.replace(indo, eng)

    possible_formats = [
        '%d-%m-%Y', '%d/%m/%Y', '%d %b %Y', '%Y-%m-%d'
    ]
    
    for fmt in possible_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    
    return ''

def save_table_as_image(dataframe, title, filename):
    plt.figure(figsize=(10, 5))
    plt.title(title, fontsize=14, fontweight='bold')
    sns.heatmap(dataframe, annot=True, fmt='g', cmap='Blues', linewidths=0.5, cbar=False)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()