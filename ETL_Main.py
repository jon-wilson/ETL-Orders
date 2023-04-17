######
#
#   This program will extract data from from an API souce and CSV files and load it into their corresponding staging tables in a MSSQL database. The CSV files are:
#       1.  dates.csv
#       2.  orders.csv
#       3.  customers.csv
#
#   The API contains product related data.
#   
######
import FileHandler
import ProductApi
import SQLHandler

###
# 
#   Constants
# 
###
BASE_FILEPATH = "C:\\Users\\jon.wilson\\OneDrive - iescorporate.onmicrosoft.com\\Documents\\Me\\Fairfield University\\SY 23\\Spring - SWEG 6508\\Exam\\Midterm\\Files\\CSV\\"
CUSTOMERS_FILENAME = BASE_FILEPATH + "FairfieldU_DW_customers.csv"
DATES_FILENAME = BASE_FILEPATH + "FairfieldU_DW_dates.csv"
EMPLOYEES_FILENAME = BASE_FILEPATH + "FairfieldU_DW_employees.csv"
GEOGRAPHY_FILENAME = BASE_FILEPATH + "FairfieldU_DW_geography.csv"
ORDERS_FILENAME = BASE_FILEPATH + "FairfieldU_DW_orders.csv"
PRODUCT_API_URL = "https://dummyjson.com/products?limit=0"

###
# 
#   Main function
# 
###
if __name__ == '__main__':
    #   Get API and CSV file data
    lstCustomers = FileHandler.Get_Customers(True, CUSTOMERS_FILENAME)
    lstDates = FileHandler.Get_Dates(True, DATES_FILENAME)
    lstEmployees = FileHandler.Get_Employees(True, EMPLOYEES_FILENAME)
    lstGeography = FileHandler.Get_Geography(True, GEOGRAPHY_FILENAME)
    lstOrders = FileHandler.Get_Orders(True, ORDERS_FILENAME)
    lstProducts = ProductApi.GetProductAPIData(PRODUCT_API_URL)

    #   Establish a connection with the MySQL database
    conn = SQLHandler.GetConn()

    #   As long as each step is successful clear the date table then insert the dates. Finally clear the customer table then insert the customers.
    if SQLHandler.ClearAllOrders(conn) \
        and SQLHandler.ClearAllCustomers(conn) \
        and SQLHandler.ClearAllDates(conn) \
        and SQLHandler.ClearAllEmployees(conn) \
        and SQLHandler.ClearAllGeography(conn) \
        and SQLHandler.ClearAllProducts(conn) \
        and SQLHandler.InsertDates(conn, lstDates) \
        and SQLHandler.InsertEmployees(conn, lstEmployees) \
        and SQLHandler.InsertGeography(conn, lstGeography) \
        and SQLHandler.InsertProducts(conn, lstProducts) \
        and SQLHandler.InsertCustomers(conn, lstCustomers) \
        and SQLHandler.InsertOrders(conn, lstOrders):
        print("Data was successfully uploaded to the database")
    else:
        print("There was an issue uploading data to the database")


