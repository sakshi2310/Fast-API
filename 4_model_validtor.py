from pydantic import BaseModel,EmailStr,Field,AnyUrl,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age :int
    weight :float
    married : bool
    allergies : list[str]
    contact_details : Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("patients older then 60 must have an emerengy contact")

def insert_patien_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted")

Patient_info = {'name':'sakshi','email':'skashi@hdfs.com','age':'68','weight':72,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'sakshi@gmail.com','phone':'6956363','emergency':'364637673'}}


pateient_1= Patient(**Patient_info) ## validation perform

insert_patien_data(pateient_1)
