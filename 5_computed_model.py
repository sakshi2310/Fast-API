from pydantic import BaseModel,EmailStr,Field,AnyUrl,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age :int
    weight :float
    height: float
    married : bool
    allergies : list[str]
    contact_details : Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self) ->float:
        height_in_meters = self.height / 100
        bmi= round(self.weight / (height_in_meters**2),2)
        return bmi


def insert_patien_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.calculate_bmi)
    print("Data inserted")

Patient_info = {'name':'sakshi','email':'skashi@hdfs.com','age':'68','weight':72,'height':173,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'sakshi@gmail.com','phone':'6956363'}}


pateient_1= Patient(**Patient_info) ## validation perform

insert_patien_data(pateient_1)
