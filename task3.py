import re

def normalize_phone(phone_number):
    cleaned_phone = re.sub(r'[^\d+]', '', phone_number)
    if not cleaned_phone.startswith('+'):
        if cleaned_phone.startswith('380'):
            cleaned_phone = '+' + cleaned_phone
        else:
            cleaned_phone = '+38' + cleaned_phone
    elif cleaned_phone.startswith('+') and not cleaned_phone.startswith('+380'):
        cleaned_phone = '+38' + cleaned_phone[1:]
    
    return cleaned_phone

