'''has_high_income=True
has_good_credit=True
if has_high_income or has_good_credit:
    print("Eligible for loan")
if has_high_income and has_good_credit:
    print("Eligible for loan")'''
    
has_crime_record=False
has_good_credit=True
if has_good_credit and not has_crime_record:
    print("Eligible for loan")