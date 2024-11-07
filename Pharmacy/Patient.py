from Pharmacy.Prescription import prescription

class patient:
    def __init__(self, name):
        self.prescriptions = []
        self.name = name
    def show_prescriptions(self):
        j = 1
        for i in self.prescriptions:
            print(f"Рецепт номер {j}\n")
            print(f"{prescription.show_constituting(i)}")
            j += 1
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
    def delete_prescription(self, index):
        j = 1
        new_prescriptions = []
        for i in self.prescriptions:
            if not j == index:
                new_prescriptions.append(i)
            j += 1
        self.prescriptions = new_prescriptions
