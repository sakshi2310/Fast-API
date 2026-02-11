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

    @field_validator('email',mode='after') # default mode after # before is used to take a value before the type converstion
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfs.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valide domain")
        
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("age should be between 0 and 100")

def insert_patien_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted")

Patient_info = {'name':'sakshi','email':'skashi@hdfs.com','age':'30','weight':72,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'sakshi@gmail.com','phone':'6956363'}}


pateient_1= Patient(**Patient_info) ## validation perform

insert_patien_data(pateient_1)
