import json
import os
MENU: dict[str, int] = {
    "CLASSIC BURGER": 18000,
    "CHEESE BURGER": 20000,
    "BACON BURGER": 23000,
    "DOUBLE SMASH BURGER": 29000,
    "BBQ BURGER": 25000,
    "CHICKEN CRISPY BURGER": 24000,
    "VEGGIE BURGER": 21000,
    "FRIES": 8000,
    "CHEESE FRIES": 11000,
    "ONION RINGS": 9000,
    "SODA": 5000,
    "LEMONADE": 6000,
    "MILKSHAKE": 12000
}
COSTS = {
    "CLASSIC BURGER": 9000,
    "CHEESE BURGER": 10000,
    "BACON BURGER": 12000,
    "DOUBLE SMASH BURGER": 15000,
    "BBQ BURGER": 13000,
    "CHICKEN CRISPY BURGER": 11000,
    "VEGGIE BURGER": 9000,
    "FRIES": 3000,
    "CHEESE FRIES": 4000,
    "ONION RINGS": 3500,
    "SODA": 1500,
    "LEMONADE": 2000,
    "MILKSHAKE": 5000
}
def load_orders_from_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=4)
        return []

    with open(filename, "r") as file:
        return json.load(file)
    
def save_orders_to_file(filename, orders_list):
    with open(filename , "w") as file:
        json.dump(orders_list, file, indent=4)
    
def load_users():
    if not os.path.exists("users.json"):
        users = {
            "manager": [{"username": "admin", "password": "1234"}], "waiter": []}
        with open ("users.json","w") as file:
            json.dump(users,file,indent = 4)
        return users
         
    with open("users.json", "r") as file:
        users = json.load(file)
        if "manager" not in users:
            users["manager"] = []
        if "waiter" not in users:
            users["waiter"] = []
        return users        

    

    
def save_users (users):
        with open("users.json","w")as file:
            json.dump(users,file,indent = 4)
        return True

def verify_login(role,username,password):
    users = load_users()

    if role not in users:
        
        return False
    for user in users[role]:
        if user["username"] == username and user ["password"]== password:
            return True
    
    return False

def create_new_user(role,username,password):
    users = load_users()
    if role not in users:
        
        return False
    
    for user_role in users:
        for user in users [user_role]:
            if user["username"] == username:
             
             return False

    users[role].append({
            "username": username,
            "password": password
        })  
    success = save_users(users)
    if success:
        
        return True
    else:
        
        return False

    
def take_order (orders_list,filename,table,products):

    table_exist = any(order["table"] == table for order in orders_list)
    if table_exist:
            return None  
    orders_items = []
    total = 0
    for product in products:
        orders_items.append(product)
        total += MENU[product]
    
    if not products:

            return None
    order = {
        "table": table,
        "items": orders_items,
        "total": total
        }
        
    orders_list.append(order)

    save_orders_to_file(filename,orders_list)

    return order 


def find_order_by_table (orders_list, table_number):
    for order in orders_list:
        if order["table"] == table_number:
            return order
    return None

def move_order_to_paid (paid_order,active_orders_file,paid_orders_file):
    with open(active_orders_file,"r") as file:
        active_orders = json.load(file)

    update_active_orders = [
        order for order in active_orders
        if order["table"] != paid_order["table"]

    ]
    with open (active_orders_file, "w") as file:
        json.dump(update_active_orders,file, indent = 4)
        
    if not os.path.exists(paid_orders_file):
        with open (paid_orders_file, "w") as file:
            json.dump([],file,indent=4)
        
    with open(paid_orders_file, "r") as file:
        paid_orders = json.load(file)

    paid_orders.append(paid_order)
    with open(paid_orders_file, "w") as file:
        json.dump(paid_orders, file, indent=4)

def show_unpaid_tables(orders_filename):
    with open(orders_filename, "r") as file:
        orders = json.load(file)
    tables = [order["table"] for order in orders]
    return tables
    
def pay_order(orders_filename,paid_filename,table_number):
    

    with open (orders_filename, "r") as file:
        orders = json.load(file)
    orders = find_order_by_table(orders,table_number)

    if orders is None:
        
        return None
    
    

    
    move_order_to_paid(orders,orders_filename,paid_filename)
    return orders

   

def show_orders (orders_filename):
    orders = load_orders_from_file(orders_filename)
    return orders



def show_income(paid_filename):
    paid_orders = load_orders_from_file(paid_filename)

    total_income = 0
    total_cost = 0
    for order in paid_orders:
        total_income += order ["total"]

        for item in order["items"]:
            
            if item in COSTS:
                total_cost += COSTS[item]
            else :
                continue
    profit = total_income - total_cost
    
    return profit




        

