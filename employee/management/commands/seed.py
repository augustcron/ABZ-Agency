from django.core.management.base import BaseCommand

import random

from employee.models import Employee


first_name = "Jay", "Jim", "Roy", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul",\
            "Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren",\
            "Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet",\
            "Lydia", "Charles", "Pedro", "Bradley", "Aaron", "Abraham", "Adam", "Adrian", "Aidan",\
            "Alan", "Albert", "Alejandro", "Alex", "Alexander", "Alfred", "Andrew", "Angel", "Anthony",\
            "Antonio", "Ashton", "Austin", "Daniel", "David", "Dennis", "Devin", "Diego", "Dominic",\
            "Donald", "Douglas", "Dylan", "Harold", "Harry", "Hayden", "Henry", "Herbert", "Horace",\
            "Howard", "Hugh", "Hunter", "Malcolm", "Martin", "Mason", "Matthew", "Michael", "Miguel",\
            "Miles", "Morgan"

last_name = "Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers",\
           "Warren", "Keller", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",\
           "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez",\
          "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez", "Harris",\
         "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young", "Allen", "Sanchez",\
         "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell",\
         "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins",\
         "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers",\
         "Morgan", "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward",\
         "Cox", "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes",\
         "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell",\
         "Sullivan", "Russell", "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler", "Barnes", "Fisher",\
         "Henderson", "Coleman", "Simmons", "Patterson", "Jordan", "Reynolds", "Hamilton", "Graham",\
         "Kim", "Gonzales", "Alexander", "Ramos", "Wallace", "Griffin", "West", "Cole", "Hayes", "Chavez",\
         "Gibson", "Bryant", "Ellis", "Stevens", "Murray", "Ford", "Marshall", "Owens", "McDonald", "Harrison",\
         "Ruiz", "Kennedy", "Wells", "Alvarez", "Woods", "Mendoza", "Castillo", "Olson", "Webb", "Washington",\
         "Tucker", "Freeman", "Burns", "Henry", "Vasquez", "Snyder", "Simpson", "Crawford", "Jimenez",\
         "Porter", "Mason", "Shaw", "Gordon", "Wagner", "Hunter", "Romero", "Hicks", "Dixon", "Hunt",\
         "Palmer", "Robertson", "Black", "Holmes", "Stone", "Meyer", "Boyd", "Mills", "Warren", "Fox",\
         "Rose", "Rice", "Moreno", "Schmidt", "Patel", "Ferguson", "Nichols", "Herrera", "Medina", "Ryan",\
         "Fernandez", "Weaver", "Daniels", "Stephens", "Gardner", "Payne", "Kelley", "Dunn", "Pierce",\
         "Arnold", "Tran", "Spencer", "Peters", "Hawkins", "Grant", "Hansen", "Castro", "Hoffman", "Hart",\
         "Elliott", "Cunningham", "Knight", "Bradley"

salary = {
    'pm': 15000,
    'lead': 10000,
    'senior': 7500,
    'middle': 4000,
    'junior': 2000
}

level = {
    'junior': 3,
    'middle': 2,
    'senior': 1,
    'lead': 0,
    'pm': None
}

employee = 'junior', 'middle', 'senior', 'lead', 'pm'


def get_name():
    name = random.choice(first_name) + ' ' + random.choice(last_name)
    return name

def get_position():
    position = random.choice(employee)
    return position

def get_salary(pos):
    sal = salary[pos]
    return sal

def get_parent(pos):
    parent = Employee.objects.filter(level=level[pos]).order_by('?').first()
    return parent
    

class Command(BaseCommand):
    help = 'Seed the database with initial data'
    def handle(self, *args, **options):

        for i in range(100):
            current_position = get_position()
            x = Employee.objects.create(
                name = get_name(),
                position = current_position,
                salary = get_salary(current_position),
                parent = get_parent(current_position),
            )
            print(x)

        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database.'))
