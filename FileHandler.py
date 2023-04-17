from Models import *
def Get_Customers(hasHeader, filename):
    lstCustomers = list()

    print("...Retrieving customer file")
    with open(filename, "r") as file:
        for customer in file:
            if not(hasHeader):
                row = customer.split(",")
                row[17] = row[17].replace("\n", "")
                lstCustomers.append(Customer(row))
            else:
                hasHeader = False
    print("...Customer file retrieved")

    return lstCustomers

def Get_Dates(hasHeader, filename):
    lstDates = list()

    print("...Retrieving date file")
    with open(filename, "r") as file:
        for date in file:            
            if not(hasHeader):
                row = date.split(",")
                row[7] = row[7].replace("\n", "")
                lstDates.append(Date(row))
            else:
                hasHeader = False
    print("...Date file retrieved")

    return lstDates

def Get_Employees(hasHeader, filename):
    lstEmployees = list()

    print("...Retrieving employee file")
    with open(filename, "r") as file:
        for employee in file:            
            if not(hasHeader):
                row = employee.split(",")
                row[21] = row[21].replace("\n", "")
                lstEmployees.append(Employee(row))
            else:
                hasHeader = False
    print("...Employee file retrieved")

    return lstEmployees

def Get_Geography(hasHeader, filename):
    lstGeography = list()

    print("...Retrieving geography file")
    with open(filename, "r") as file:
        for geography in file:            
            if not(hasHeader):
                row = geography.split(",")
                row[9] = row[9].replace("\n", "")
                lstGeography.append(Geography(row))
            else:
                hasHeader = False
    print("...Geograpy file retrieved")

    return lstGeography

def Get_Orders(hasHeader, filename):
    lstOrders = list()

    print("...Retrieving order file")
    with open(filename, "r") as file:
        for order in file:            
            if not(hasHeader):
                row = order.split(",")
                row[3] = row[3].replace("\n", "")

                # Only add orders with product ids that aren't zero
                if row[2] != '0':
                    lstOrders.append(Order(row))
            else:
                hasHeader = False
    print("...Order file retrieved")

    return lstOrders