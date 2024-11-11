from Pharmacy.Medicine import medicine

class prescription:
    def __init__(self):
        self.medicines = []
    def show_constituting(self):
        j = 1
        print("Состав рецепта:\n")
        for i in self.medicines:
            print(f"{j}: {medicine.__str__(i)}\n")
            j += 1
    def add_medicine(self, medicine):
        self.medicines.append(medicine)
    def delete_medicine(self, index):
        self.medicines.pop(index)
