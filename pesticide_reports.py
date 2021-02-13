from datetime import datetime
import pandas as pd

def string_input():
    new_string = input()
    return new_string

def customer_name():
    print("Customer name: ")
    string = input()
    print(string)
    return string

def customer_address():
    print("Customer address: ")
    string = input()
    print(string)
    return string

def applicator_name():
    print("Applicator name: ")
    string = input()
    print(string)
    return string

def application_date():
    print("Application date (dd/mm/yyyy): ")
    string  = str(input())
    string = pd.to_datetime(string)
    print(string)
    return string

def certification_number():
    print("Certification number: ")
    string = str(input())
    return string

def crop():
    print("Crop treated: ")
    string = input()
    return string

def site_size():
    print("Area treated: ")
    string = int(input())
    return string

def target_pest():
    print("Target pest: ")
    string = input()
    return string

def pesticide_used():
    print("Select pesticide: ")
    string = input()
    return string

def pesticide_amount():
    print("Amount applied: ")
    string = input()
    return string 

class report:
    def __init__(self,
                 customer_name,
                 customer_address,
                 application_date,
                 applicator_name,
                 certification_number,
                 crop,
                 site_size,
                 target_pest,
                 pesticide_applied,
                 application_amount):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.application_date = application_date
        self.applicator_name = applicator_name
        self.certification_number = certification_number
        self.crop = crop
        self.site_size = site_size
        self.target_pest = target_pest
        self.pesticide_applied = pesticide_applied
        self.application_amount = application_amount

Paul = report(customer_name(),
              customer_address(),
              application_date(),
              applicator_name(),
              certification_number(),
              crop(),
              site_size(),
              target_pest(),
              pesticide_used(),
              pesticide_amount())