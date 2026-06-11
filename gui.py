import tkinter as tk
import logic 
from tkinter import messagebox
ORDERS_FILE = 'orders.json'
USERS = 'users.json'
PAID_ORDERS = 'paid_orders.json'
window = tk.Tk()
window.geometry('480x440')
window.title('Sistema Restaurante')




def clear_window():
    for widget in window.winfo_children():
        widget.destroy()



def manager_screen():
    clear_window()
    label = tk.Label (window,text= 'welcome manager')
    label.grid(row=1,column= 1, padx=10, pady=6)

    show_options =  tk.Label (window,text= 'Select an Option')
    show_options.grid(row=2,column= 1, padx=10, pady=6)
    def show_paid_orders ():
        orders = logic.show_orders(PAID_ORDERS)
        text = ''
        for order in orders:
            text += f'Mesa: {order ['table']}, '
            text += f'Items: {', '.join (order ['items'])},  '
            text += f'Total: {order ['total']}\n'
        clear_window()
        result_label = tk.Label(window,text=text)
        result_label.grid (row=3,column=1, padx=10, pady=6)
        paid_orders = tk.Button (window,text= 'Back', command= manager_screen )
        paid_orders.grid(row=4,column= 1, padx=10, pady=6)

    def show_unpaid_orders ():
        orders = logic.show_orders(ORDERS_FILE)
        text = ''
        for order in orders:
            text += f'Mesa: {order ['table']}, '
            text += f'Items: {', '.join (order ['items'])}, '
            text += f'Total: {order ['total']}\n'
        clear_window()
        result_label = tk.Label(window,text=text)
        result_label.grid (row=3,column=1, padx=10, pady=6)
        unpaid_orders = tk.Button (window,text= 'Back', command= manager_screen )
        unpaid_orders.grid(row=4,column= 1, padx=10, pady=6)
   
    def show_income ():
        income = logic.show_income(PAID_ORDERS)
        text = f'Ganancia del día: ${income}'
        clear_window()
        show_label_income = tk.Label(window,text=text)
        show_label_income.grid(row = 1, column= 1, padx=10, pady=6)
        income_button = tk.Button (window,text= 'Back', command= manager_screen )
        income_button.grid(row=2,column= 3, padx=10, pady=6)

    paid_orders = tk.Button (window,text= 'Paid Orders', command= show_paid_orders )
    paid_orders.grid(row=3,column= 2, padx=10, pady=6)
    unpaid_orders = tk.Button (window,text= 'Unpaid Orders', command= show_unpaid_orders )
    unpaid_orders.grid(row=3,column= 3, padx=10, pady=6)
    income_button = tk.Button (window,text= 'Income', command= show_income )
    income_button.grid(row=3,column= 5, padx=10, pady=6)
    exit = tk.Button (window,text= 'Exit', command= login_screen )
    exit.grid(row=3,column= 10, padx=10, pady=6)

def waiter_screen():
    clear_window()
    label = tk.Label (window,text= 'welcome waiter')
    label.grid(row=1,column= 2, padx=10, pady=6)
    def take_order ():
        clear_window()
        current_order = []
        order_var = tk.StringVar(value='FRIES')
        num_table = tk.Label(window,text='number of table')
        num_table.grid(row= 1, column=2, padx=10, pady=6)
        table_entry = tk.Entry(window)
        table_entry.grid(row=1,column= 3, padx=10, pady=6)
        def save_order():
            table = table_entry.get()
            orders = logic.load_orders_from_file(ORDERS_FILE)
            new_order = logic.take_order(orders, ORDERS_FILE, table, current_order)
            if new_order:
                messagebox.showinfo('Listo', 'Pedido guardado')
                waiter_screen()
            else:
                messagebox.showerror('Error', 'Mesa ocupada o pedido vacío')

        menu = tk.OptionMenu(window, order_var, *logic.MENU.keys())
        menu.grid(row = 1, column= 4, padx=10, pady=6)
        def add_item ():
            prduct = order_var.get()
            current_order.append(prduct)

            text = ', '.join(current_order)
            display_label = tk.Label(window, text='Pedido: (vacío)')
            display_label.config(text=text)
            display_label.grid(row=3,column=5, padx=10, pady=6)
            
        add_product=tk.Button (window,text= 'charge', command= add_item)
        add_product.grid(row=2,column= 5, padx=10, pady=6)
        save_button = tk.Button(window, text='Guardar pedido', command=save_order)
        save_button.grid(row=5, column=2, padx=10, pady=6)
    exit = tk.Button (window,text= 'Exit', command= login_screen )
    exit.grid(row=3,column= 10, padx=10, pady=6)




    def collect_the_bill():
        clear_window ()
        label_2 = tk.Label (window,text='Unpaid tables:')
        label_2.grid(row=1,column= 1, padx=10, pady=6)
        tables = logic.show_unpaid_tables(ORDERS_FILE)
        text = ', '.join(tables)
        result_label = tk.Label(window,text=text)
        result_label.grid (row=2,column=1, padx=10, pady=6)

        label_3 = tk.Label (window,text='Table: ')
        label_3.grid(row=5,column= 4, padx=10, pady=6)

        selected_table = tk.Entry(window)
        selected_table.grid(row=5,column= 5, padx=10, pady=6)

        def table_selected ():
            
            table = selected_table.get()
            charge_table = logic.pay_order(ORDERS_FILE,PAID_ORDERS,table)
            clear_window ()
            order = ''
            if charge_table:
                order += f'Mesa: {charge_table ['table']}, '
                order += f'Items: {', '.join (charge_table['items'])} '
                order += f'Total: {charge_table ['total']}\n'
                result_label = tk.Label(window,text=order)
                result_label.grid (row=6,column=1, padx=10, pady=6)
            else:
                messagebox.showerror('Error', 'mesa no encontrada')
            back = tk.Button (window,text= 'Back', command= waiter_screen )
            back.grid(row=4,column= 1, padx=10, pady=6)
            



        collect_charge=tk.Button (window,text= 'charge', command= table_selected)
        collect_charge.grid(row=3,column= 5, padx=10, pady=6)    

    charge=tk.Button (window,text= 'go to charge', command= collect_the_bill)
    charge.grid(row=3,column= 5, padx=10, pady=6)
    order=tk.Button (window,text= 'take order', command= take_order)
    order.grid(row=3,column= 6, padx=10, pady=6)

def create_account_screen():
    clear_window ()
    label_role = tk.Label (window,text='Role')
    label_role.grid(row=0,column= 1, padx=10, pady=6)

    selected_role = tk.StringVar(value='manager')

    role_waiter = tk.Radiobutton(window, text = 'waiter',variable = selected_role, value = 'waiter')
    role_waiter.grid(row=1,column= 1, padx=10, pady=6)

    role_manager = tk.Radiobutton(window,text = 'manager',variable = selected_role, value = 'manager')
    role_manager.grid(row=2,column= 1, padx=10, pady=6)

    label_login = tk.Label (window,text='Login')
    label_login.grid(row=3,column= 1, padx=10, pady=6)

    label_user = tk.Label (window,text='User')
    label_user.grid(row=4,column= 1, padx=10, pady=6)
    user = tk.Entry(window)
    user.grid(row=4,column= 2, padx=10, pady=6)
    label_password = tk.Label (window,text='password')
    label_password.grid(row=5,column= 1, padx=10, pady=6)
    password = tk.Entry(window)
    password.grid(row=5,column= 2, padx=10, pady=6)
    def register ():
        username = user.get()
        role = selected_role.get()
        write_password = password.get()

        create_account = logic.create_new_user(role,username,write_password)
        if create_account:
            messagebox.showinfo('Listo', 'Cuenta creada')
            login_screen()
        else:
             messagebox.showinfo('El usuario ya existe')
    btn = tk.Button (window,text= 'Crear Cuenta', command= register )
    btn.grid(row=6,column= 1, padx=10, pady=6)
    back = tk.Button(window, text='Volver', command=login_screen)
    back.grid(row=7, column=1, padx=10, pady=6)

def login_screen():
    clear_window()
    label_role = tk.Label (window,text='Role')
    label_role.grid(row=0,column= 1, padx=10, pady=6)

    selected_role = tk.StringVar(value='manager')

    role_waiter = tk.Radiobutton(window, text = 'waiter',variable = selected_role, value = 'waiter')
    role_waiter.grid(row=1,column= 1, padx=10, pady=6)

    role_manager = tk.Radiobutton(window,text = 'manager',variable = selected_role, value = 'manager')
    role_manager.grid(row=2,column= 1, padx=10, pady=6)

    label_login = tk.Label (window,text='Login')
    label_login.grid(row=3,column= 1, padx=10, pady=6)

    label_user = tk.Label (window,text='User')
    label_user.grid(row=4,column= 1, padx=10, pady=6)
    user = tk.Entry(window)
    user.grid(row=4,column= 2, padx=10, pady=6)
    

    label_password = tk.Label (window,text='password')
    label_password.grid(row=5,column= 1, padx=10, pady=6)
    password = tk.Entry(window)
    password.grid(row=5,column= 2, padx=10, pady=6)
    def try_login():
        username = user.get()
        role = selected_role.get()
        write_password = password.get()

        result = logic.verify_login(role,username,write_password)
        if result:
            clear_window()
            if role == 'waiter':
                waiter_screen()
            elif role == 'manager':
                manager_screen()
        else:
            messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

    btn = tk.Button (window,text= 'Crear Cuenta', command= create_account_screen )
    btn.grid(row=6,column= 2, padx=10, pady=6)

    btn = tk.Button (window,text= 'Entrar', command= try_login )
    btn.grid(row=6,column= 1, padx=10, pady=6)
login_screen()    
window.mainloop()