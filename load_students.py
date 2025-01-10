import csv
from students.models import Student

def load_students():
    with open('database.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Student.objects.create(
                student_number=row['Öğrenci Numarası'],
                first_name=row['Ad'],
                last_name=row['Soyad'],
                exam_score=int(row['Arasınav Notu'])
            )
    print("Veriler başarıyla yüklendi.")
