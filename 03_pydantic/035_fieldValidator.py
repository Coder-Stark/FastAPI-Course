#field_validator -> work on 1 field

from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]                 #list (it only tells that is list not list of string)
    contact_details: Dict[str, str]      #dist (it only telss that is dict not dict (key and value of string))

    @field_validator('email')            #run in 2 mode (mode = before and mode = after (by default))
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]       #abc@gmail.com -> gmail.com

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


patient_info = {'name': 'kumar', 'email': 'abc@hdfc.com', 'age': 25, 'weight': 79.5, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '987654321'}}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient1) 


"""
outputs

KUMAR
abc@hdfc.com
25
79.5
False
['pollen', 'dust']
{'phone': '987654321'}
"""