def insert_patient_data(name,age):
    print(name)
    print(age)

    print("inserted into the database")

insert_patient_data('sakshi','thirty')

def insert_patient_data(name:str,age:int):
    print(name)
    print(age)

    print("inserted into the database")

insert_patient_data('sakshi','21')


# to solve this problem
def insert_patient_data(name:str,age:int):
    if age<0:
        raise ValueError("age can not be negative")

    if type(name) == str and type(age) == int:
        print(name)
        print(age)

    print("inserted into the database")

insert_patient_data('sakshi',21) ## must need to write in this way

