#computed_fields

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int                            
    weight: float                       #kg
    height: float                       #m
    married: bool 
    allergies: List[str]                
    contact_details: Dict[str, str]     

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi


patient_info = {'name': 'kumar', 'email': 'abc@hdfc.com', 'age': 65, 'weight': 79.5, 'height': 1.72, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '987654321', 'emergency': '987654322'}}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI', patient.calculated_bmi)         #from calculation

insert_patient_data(patient1) 


"""
outputs

kumar
abc@hdfc.com
65
79.5
1.72
False
['pollen', 'dust']
{'phone': '987654321', 'emergency': '987654322'}
BMI 26.87
"""