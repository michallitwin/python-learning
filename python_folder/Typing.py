from typing import Literal, Any, Annotated, Optional
from enum import Enum
from pydantic import (
    BaseModel,
    ValidationError, 
    Field, 
    EmailStr, 
    computed_field, 
    field_validator,
    ConfigDict,
)

### - 1
# def format_response(
#     code: int | str,
#     status: Literal["success", "error", "pending"], 
#     data: dict | None = None,
# ) -> dict[str, Any]:
#     return {
#         "code": code,
#         "status": status,
#         "data": data,
#     }

# a = format_response("hello","error")
# print(a)

# ### - 2

# def filter_adults(people: list[dict[str, Any]]) -> list[dict[str, Any]]:
#     adults = []
#     for p in people:
#         if p["age"] >= 18:
#             adults.append(p)
#     return adults

# people_list = [
#     {"name": "Michał", "age": 20},
#     {"name": "Adam", "age": 15},
#     {"a":"b", "age":22}
# ]

# print(filter_adults(people_list))

# # ### - 3

# def analyze_numbers(numbers: list[int]) -> dict[str, float]:

#     return {
#         "min": min(numbers),
#         "max": max(numbers),
#         "sum": sum(numbers),
#         "avg": sum(numbers)/len(numbers)
#     }

# list_of_numbers = [2, 1, 43, 2, 6, 7, 864]

# print(analyze_numbers(list_of_numbers))

# # #PYDANTIC

# # ### - 4

# class User(BaseModel):
#     username: Annotated[str, Field(min_length=3,max_length=20)]
#     email: EmailStr
#     age: Annotated[int, Field(gt=18, lt=120)]
#     is_active: bool = True

# try:
#     user1 = User(
#         username = "Michal",
#         email = "Michal@wp.pl",
#         age = 24)

#    # print(user1)
        
# except ValidationError as e:
#     print("Wystapił jakiś bład")

# # ### - 5

# class Account(BaseModel):
#     username: str
#     password: str


#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, v:str):
#         check_upper = False
#         check_digit = False
#         if len(v) < 8:
#             raise ValueError("Too short password")
#         for l in v:
#             if l.isdigit():
#                 check_digit = True
#             if l.isupper():
#                 check_upper = True
#         if not check_upper:
#             raise ValueError("Add upper letter")
#         if not check_digit:
#             raise ValueError("Add some digits")
        

# # password = Account(username='michal', password='Hasloooo2')
# # password2 = Account(username='michal', password='Haslo')
# # password3 = Account(username='michal', password='hasloooo')


# # ### - 6

#  class Invoice(BaseModel):
#     customer: str
#     price_net: float
#     vat_rate: float = 0.23

#     @computed_field
#     @property
#     def price_gross(self) -> float:
#         Price = self.price_net * (1 + self.vat_rate)
#         return Price
    

#     model_config = ConfigDict(
#         str_strip_whitespace=True,
#         extra="forbid",
#     )

# price = Invoice(
#     customer="michal",
#     price_net="10"
# )

# print(price)




# ### - 7


# class Department(str, Enum):
#     IT = "it",
#     HR = "hr",
#     SALES = "sales",
#     MARKETING = "marketing"

# class Employee(BaseModel):
#     name: str
#     salary: Annotated[float, Field(gt=0)]
#     department: Department

# try:
#     user1 = Employee(
#         name="Michal",
#         salary= 4242,
#         department="abc"
#     )
#     print(user1)

# except ValidationError as e:
#     print(e)





# ### - 8 

# class User(BaseModel):
#     name: str
#     email: str
#     age: int

# def greet_user(user: User) -> str:
#     return f"Hello {user.name}, your email is {user.email}"


# user1 = User(
#     name="michal",
#     email="michal123@wp.pl",
#     age=32
# )

# print(greet_user(user1))


# ### - 9

# class Customer(BaseModel):
#     name: str
#     email: str

# class Order(BaseModel):
#     order_id: int
#     amount: float


# def send_confirmation(customer: Customer, order: Order) -> str:
#     return f"Order {order.order_id} for {order.amount} PLN confirmed for {customer.name} ({customer.email})"
    

# customer1= Customer(name="Michal", email="michal@wp.pl")
# order1= Order(order_id=123, amount= 5)

# print(send_confirmation(customer1,order1))



# ### -10


# class Address(BaseModel):
#     city: str
#     street: str
#     zip_code: str


# class Person:
#     def __init__(self, name: str, address: Address):
#         self.name = name
#         self.address = address

#     def show_address(self) -> str:
#         return f"{self.name} lives at {self.address.street}, {self.address.zip_code} {self.address.city}"
    



# adres = Address(city="WWA", street="złota", zip_code="20-200")
# individual= Person('Michal', adres)

# print(individual.show_address())


# ### -11

# class Task(BaseModel):
#     title: str
#     done: bool


# class ToDoList:
#     def __init__(self, owner: str, tasks: list[Task]):
#         self.owner = owner
#         self.tasks = tasks

#     def count_done(self) -> int:
#         done_tasks = []
#         for i in self.tasks:
#             if i.done:
#                 done_tasks.append(i)
#         return len(done_tasks)
    
#     def add_task(self, task: Task):
#         self.tasks.append(task)


# task1 = Task(title="ABCD", done=True)
# task2 = Task(title="auta", done=False)
# task3 = Task(title="123", done=False)
# newtask= Task(title="Aaaaaa", done=True)

# a = ToDoList("michal", [task1, task2])
# print(a.add_task(newtask))
# print(a.count_done())


### - 12

# class Employee(BaseModel):
#     name: str
#     department: str
#     salary: float


# def group_by_department(employees: list[Employee]) -> dict[str, list[Employee]]:
#     grouped_data = {}
#     for i in employees:
#         if i.department in grouped_data:
#             grouped_data[i.department].append(i)
#         else:
#             grouped_data[i.department] = [i]


#     return grouped_data


# user1 = Employee(name="ana", department="IT", salary= 1500)
# user2 = Employee(name="anna", department="HR",salary=  1300)
# user3 = Employee(name="dupa", department="IT",salary=  1200)


# print(group_by_department([user1, user2, user3]))
# #print(user1, user2, user3)












######################### - PART 2


### - 1

class Product(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=51)]
    price: Annotated[float, Field(gt=0)]
    quantity: Annotated[int, Field(ge=0)] = 0
    description: Optional[str] = None
    tags: list[str] | None = None
    sugar: Annotated[float, Field(gt=50)] = 50

product1 = Product(name="cola", price= 5.50, quantity=4, description="Very healthy drink", tags=['cola', 'coca-cola'] )
product2 = Product(name="water",price= 2.20)

print(product1)
print(product2)