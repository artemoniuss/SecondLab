class medicine:
   def __init__(self, med_cost, med_name, reception_time):
       if med_cost < 0:
           raise ValueError("Стоимость не может быть отрицательная")
       self.med_cost = med_cost
       if med_name == "":
           raise ValueError("Имя не может быть пустым")
       self.med_name = med_name
       if reception_time <= 0:
           raise ValueError("Время приема не может быть отрицательным или равно нулю")
       self.reception_time = reception_time

   def __str__(self):
       return f"{self.med_name} с курсом приема {self.reception_time} стоит {self.med_cost}."
