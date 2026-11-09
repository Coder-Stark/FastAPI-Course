#model_validator -> work on whole model

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]                 #list (it only tells that is list not list of string)
    contact_details: Dict[str, str]      #dist (it only telss that is dict not dict (key and value of string))

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older then 60 must have an emergency contact')
        return model

patient_info = {'name': 'kumar', 'email': 'abc@hdfc.com', 'age': 65, 'weight': 79.5, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '987654321', 'emergency': '987654322'}}

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

kumar
abc@hdfc.com
65
79.5
False
['pollen', 'dust']
{'phone': '987654321', 'emergency': '987654322'}
"""