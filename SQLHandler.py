######
#
#   The functions in this file handle all database related functionality
#
######
import pyodbc
from Models import *

######
#
#   Functions
#
######

#   This function will return a connection to the MSSQL database
def GetConn():

    print("...Establishing a connection to the database")
    server = 'localhost' 
    database = 'fairfieldudw' 
    username = 'sweg6508-agent' 
    password = 'sweg6508-agent1' 
    
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# Clear all customers in the Dim.customers table
def ClearAllCustomers(conn):
    flag = True
    sql = "DELETE FROM [Dim].[Customers]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All customers have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Customers failed to be deleted from the database")

    return flag

# Insert customers into the Dim.customer table
def InsertCustomers(conn, lstCustomers):
    flag = True
    sql = "INSERT INTO [Dim].[Customers]([CustomerKey],[GeographyKey],[CustomerAlternateKey],[FirstName],[MiddleName],[LastName],[BirthDate],[MaritalStatus],[Gender],\
        [EmailAddress],[YearlyIncome],[TotalChildren],[NumberChildrenAtHome],[HouseOwnerFlag],[NumberCarsOwned],[AddressLine1],[Phone],[DateFirstPurchase]) \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for customer in lstCustomers:
                cursor.execute(sql, customer.GetListFormat())
                conn.commit()
            print("...All customers have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Customers failed to insert into the database")

    return flag

# Clear all dates in the Dim.dates table
def ClearAllDates(conn):
    flag = True
    sql = "DELETE FROM [Dim].[Dates]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All dates have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Dates failed to be deleted from the database")

    return flag

# Insert dates into the Dim.dates table
def InsertDates(conn, lstDates):
    flag = True
    sql = "INSERT INTO [Dim].[Dates] ([DateKey],[FullDate],[DayName],[DayNumber],[MonthName],[MonthNumber],[QuarterNumber],[Year]) VALUES (?,?,?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for date in lstDates:
                cursor.execute(sql, date.GetListFormat())
                conn.commit()
            print("...All dates have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Dates failed to insert into the database")

    return flag

# Clear all employees in the Dim.employees table
def ClearAllEmployees(conn):
    flag = True
    sql = "DELETE FROM [Dim].[Employees]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All employees have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Employees failed to be deleted from the database")

    return flag

# Insert employees into the Dim.employees table
def InsertEmployees(conn, lstEmployees):
    flag = True
    sql = "INSERT INTO [Dim].[Employees] ([EmployeeKey],[ParentEmployeeKey],[SalesTerritoryKey],[FirstName],[MiddleName],[LastName],[NameStyle],[Title],[HireDate],\
        [BirthDate],[EmailAddress],[Phone],[MaritalStatus],[SalariedFlag],[Gender],[PayFrequency],[BaseRate],[VacationHours],[SickLeaveHours],[DepartmentName] \
        ,[StartDate],[EndDate]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for employee in lstEmployees:
                cursor.execute(sql, employee.GetListFormat())
                conn.commit()
            print("...All employees have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Employees failed to insert into the database")

    return flag


# Clear all geography in the Dim.geography table
def ClearAllGeography(conn):
    flag = True
    sql = "DELETE FROM [Dim].[Geography]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All geography regions have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Geography regions failed to be deleted from the database")

    return flag

# Insert dates into the Dim.dates table
def InsertGeography(conn, lstGeography):
    flag = True
    sql = "INSERT INTO [Dim].[Geography] ([GeographyKey],[City],[StateProvinceCode],[StateProvinceName],[CountryRegionCode],[EnglishCountryRegionName],\
            [SpanishCountryRegionName],[FrenchCountryRegionName],[PostalCode],[SalesTerritoryKey]) VALUES (?,?,?,?,?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for geography in lstGeography:
                cursor.execute(sql, geography.GetListFormat())
                conn.commit()
            print("...All geography regions have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Geography regions failed to insert into the database")

    return flag

# Clear all orders in the fact.orders table
def ClearAllOrders(conn):
    flag = True
    sql = "DELETE FROM [Fact].[Orders]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All orders have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Orders failed to be deleted from the database")

    return flag

# Insert Orders into the Fact.Orders table
def InsertOrders(conn, lstOrders):
    flag = True
    sql = "INSERT INTO [Fact].[Orders] ([CustomerKey],[DateKey],[EmployeeKey],[GeophraphyKey],[ProductKey],[OrderQuantity]) VALUES (?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for order in lstOrders:
                order.geographyKey = GetGeographyKey(cursor, order.customerKey)
                order.employeeKey = GetEmployeeManagerKey(cursor, order.customerKey)
                cursor.execute(sql, order.GetListFormat())
                conn.commit()
            print("...All orders have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[1]) 
            flag = False
            print("*** Orders failed to insert into the database")

    return flag

def GetGeographyKey(cursor, customerKey):
    sql = '''SELECT [GeographyKey] FROM [FairfieldUDW].[Dim].[Customers] where CustomerKey = ?'''
    try:
        result = cursor.execute(sql, customerKey)
        row =  result.fetchone()
        return row.GeographyKey
    except pyodbc.Error as ex:
        print("Failed to find geographyKey for customerKey:", customerKey, "|", ex.args[0]) 

    return -1

def GetEmployeeManagerKey(cursor,customerKey):
    sql = '''
        SELECT
            e.ParentEmployeeKey 
        FROM
            [FairfieldUDW].[Dim].[Customers] c 
        JOIN	
            [FairfieldUDW].[Dim].[Geography] g ON c.GeographyKey = g.GeographyKey  
        JOIN
            [FairfieldUDW].[Dim].[Employees] e ON g.SalesTerritoryKey = e.SalesTerritoryKey 
        WHERE
            c.CustomerKey = ?
    '''
    try:
        result = cursor.execute(sql, customerKey)
        row =  result.fetchone()
        return row.ParentEmployeeKey
    except pyodbc.Error as ex:
        print("Failed to find parentEmployeeKey for customerKey:", customerKey, "|", ex.args[0]) 

    return -1

# Clear all Products in the Dim.Products table
def ClearAllProducts(conn):
    flag = True
    sql = "DELETE FROM [Dim].[Products]"

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            conn.commit()
            print("...All products have been deleted from the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Products failed to be deleted from the database")

    return flag

# Insert Products into the Dim.Products table
def InsertProducts(conn, lstProducts):
    flag = True
    sql = "INSERT INTO [Dim].[Products] ([ProductKey],[Title],[Description],[Price],[DiscountPercentage],[Rating],[Stock],[Brand],[Category],[Thumbnail],[Images]) VALUES (?,?,?,?,?,?,?,?,?,?,?)"

    with conn.cursor() as cursor:
        try:
            for product in lstProducts:
                cursor.execute(sql, product.GetListFormat())
                conn.commit()
            print("...All products have been inserted into the database")
        except pyodbc.Error as ex:
            print(ex.args[0]) 
            flag = False
            print("*** Products failed to insert into the database")

    return flag
