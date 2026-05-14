def insert_patient_data(name:str,age:int,id:int):
  
  if type(name) ==str and type(age)==int and type(id) ==int:
    print(name)
    print(age)
    print(id)
  else :
    raise TypeError('incorrect data type')
insert_patient_data('sarthak', 90, 85)    
