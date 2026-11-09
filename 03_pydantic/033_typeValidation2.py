from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None              #by default is required if we dont add optional
    allergies: List[str]                 #list (it only tells that is list not list of string)
    contact_details: Dict[str, str]      #dist (it only telss that is dict not dict of string)

patient_info = {'name': 'kumar', 'age': 25, 'weight': 79.5, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '987654321'}}

patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

insert_patient_data(patient1) 



"""
outputs

kumar
25
79.5
None
['pollen', 'dust']
{'email': 'abc@gmail.com', 'phone': '987654321'}

"""