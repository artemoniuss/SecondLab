from Pharmacy import Patient, Prescription, Medicine
import platform
import os
from docx import Document

def main():
    choices = {
        1: "Создать лекарство",
        2: "Создать рецепт",
        3: "Создать пациента",
        4: "Редактировать рецепт",
        5: "Назначить рецепт пациенту",
        6: "Посмотреть рецепты пациента",
        7: "Выйти из программы"
    }
    medicines = []
    prescriptions = []
    patients = []
    while True:
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = int(input("Ваш выбор: "))
        if choice not in choices:
            print("Неправильный выбор. Пожалуйста, выберите один из доступных вариантов.")
            continue
        if choice == 1:
            print("Введите имя лекарства")
            name_med = input("Имя: ")
            for mee in medicines:
                if name_med == mee.med_name:
                    print("Лекарство с таким именем уже существует!!!")
                    name_med = "-12"
            if name_med == "-12":
                continue
            print("Введите стоимость лекарства")
            cost_med =  int(input("Стоимость: "))
            print("Введите время приёма в днях для лекарства")
            time_med =  int(input("Время приема: "))
            new_med = Medicine.medicine(cost_med, name_med, time_med)
            medicines.append(new_med)
            print("Лекарство создан")
        if choice ==  2:
            print("Рецепт создан")
            new_prec = Prescription.prescription()
            prescriptions.append(new_prec)
        if choice ==  3:
            print("Введите имя пациента")
            name_pat = input("Имя: ")
            for pat in patients:
                if name_pat == pat.name:
                    print("Пациент с таким именем уже существует!!!")
                    name_pat = "-12"
            if name_pat == "-12":
                continue
            new_pat = Patient.patient(name_pat)
            patients.append(new_pat)
            print("Пациент создан")
        if choice ==  4:
            j = 1
            for i in prescriptions:
                print(f"Рецепт номер {j}\n")
                print(f"{Prescription.prescription.show_constituting(i)}")
                j += 1
            print("Выберите рецепт для редактирования:")
            num_rec =  int(input("Номер: "))
            if num_rec >= j:
                print("Рецепта с таким номером не существует")
                continue
            print("Введите 1 если хотите добавить рецепт, 2 если хотите удалить рецепт")
            num_do =  int(input("Номер действия: "))
            if num_do == 1:
                s = 1
                print("Доступные лекарства:\n")
                for me in medicines:
                    print(f"{s}: {me.__str__()}\n")
                    s += 1
                print("Выберите лекарство")
                num_mmm = int(input("Номер: "))
                if num_mmm >= s:
                    print("лекарства с таким номером не существует")
                    continue
                acc = 1
                for me in medicines:
                    if acc == num_mmm:
                        prescriptions[num_rec - 1].add_medicine(me)
                    acc += 1
            if num_do == 2:
                s = 1
                print("Состав рецепта:\n")
                for me in prescriptions[num_rec].medicines:
                    print(f"{s}: {me.__str__()}\n")
                    s += 1
                print("Выберите лекарство")
                num_mmm = int(input("Номер: "))
                if num_mmm >= s:
                    print("лекарства с таким номером не существует")
                    continue
                prescriptions[num_rec - 1].delete_medicine(num_mmm)
        if choice ==  5:
            qj = 1
            for i in patients:
                print(f"Пациент номер {qj}\n")
                print(f"{Patient.patient.show_prescriptions(i)}")
                qj += 1
            print("Выберите пациента")
            num_pat = int(input("Номер: "))
            if num_pat >= qj:
                print("Пациента с таким номером не существует")
                continue
            j = 1
            for i in prescriptions:
                print(f"Рецепт номер {j}\n")
                print(f"{Prescription.prescription.show_constituting(i)}")
                j += 1
            print("Выберите рецепт")
            num_rec =  int(input("Номер: "))
            if num_rec >= j:
                print("Рецепта с таким номером не существует")
                continue
            s = 1
            patients[num_pat - 1].add_prescription(prescriptions[num_rec - 1])
        if choice ==  6:
            qj = 1
            for i in patients:
                print(f"Пациент номер {qj}\n")
                print(f"{Patient.patient.show_prescriptions(i)}")
                qj += 1
            print("Выберите пациента")
            num_pat = int(input("Номер: "))
            if num_pat >= qj:
                print("Пациента с таким номером не существует")
                continue
            cost = 0
            time = 0
            for ads in patients[num_pat - 1].prescriptions:
                for ads_med in ads.medicines:
                    if ads_med.reception_time > time:
                        time = ads_med.reception_time
                    cost += ads_med.med_cost
            result = f"Курс приема пациента равен {time}, а стоимость всех рецептов равна {cost}."
            print(result)
            choice = input("Сохранить результат в docx? (Да/Нет) [Нет]: ")
            doc = Document()
            if choice == 'Да':
                doc.add_paragraph(result)
                doc.save("costs.docx")
                print("Файл сохранен")
        if choice ==  7:
            print("До свидания!!!")
            break

if __name__ == "__main__":
    main()