from pydantic import BaseModel,EmailStr,Field,AnyUrl
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="name of the field",description="give the name of the patient max character is 50 characters",examples=['sakshi','isha'])]
    name:str = Field(max_length=50)
    email : EmailStr
    age:int = Field(gt=0,lt=120)
    weight:float = Field(gt=0)
    married:bool = False
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]  # when we make any optional filed we need to assign any value
    contact_details : Dict[str,str]



def insert_patien_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted")

Patient_info = {'name':'sakshi','email':'skashi@gmail.com','age':'30','weight':72,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'sakshi@gmail.com','phone':'6956363'}}


pateient_1= Patient(**Patient_info)

insert_patien_data(pateient_1)
