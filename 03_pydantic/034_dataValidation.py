#Data Validation

"""
install email-validator first
-> python -m pip install "pydantic[email]"
"""
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Optional, Annotated

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    # weight: float = Field(gt=0)
    # married: Optional[bool] = None 
    
    name: Annotated[str, Field(max_length=50, title='Name of patient', description='Give the name of patient in less then 50 chars', examples=['Shivam', 'Kumar', 'Rajbhar'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0, lt = 120)
    weight: Annotated[float, Field(gt=0, strict=True)]                  #Strict now type coercing '79.5' -> 79.5 will not work
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]


patient_info = {
    'name': 'rajbhar', 
    'email': 'abc@gmail.com', 
    'linkedin_url': 'https://www.linkedin.com/in/shivamkr-developer/', 
    'age': 25, 
    'weight': 79.5, 
    'married': False
}              

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)

insert_patient_data(patient1)



"""
outputs

rajbhar
abc@gmail.com
https://www.linkedin.com/in/shivamkr-developer/
25
79.5
False
"""