from pydantic import BaseModel

class address(BaseModel):
    city:str
    state : str
    pin : str


class patient(BaseModel):
    name:str
    gender:str
    age:int
    address:address

address_dics = {'city':'jaipur','state':'rajsthan','pin':'32001'}

address1 = address(**address_dics)

patient_dics = {'name':'sakshi','gender':'Female','age':35,'address':address1}

patient1 = patient(**patient_dics)

print(patient1)
print(patient1.address.city)

temp = patient1.model_dump()
print(temp)
print(type(temp))