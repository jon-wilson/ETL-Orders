######
#
#   Classes
#
######
from datetime import datetime

class Customer:
    def __init__(self, lstCustomer):
        self.TransformCustomer(lstCustomer)
    
    def TransformCustomer(self, lstCustomer):
        try:
            self.customerKey = lstCustomer[0]
            self.geographyKey = lstCustomer[1]
            self.customerAlternateKey = lstCustomer[2]
            self.firstName = lstCustomer[3]
            self.middleName = lstCustomer[4]
            self.lastName = lstCustomer[5]
            self.birthDate = datetime.strptime(lstCustomer[6], "%m/%d/%Y")
            self.maritalStatus = lstCustomer[7]
            self.gender = lstCustomer[8]
            self.emailAddress = lstCustomer[9]
            self.yearlyIncome = float(lstCustomer[10])
            self.totalChildren = int(lstCustomer[11])
            self.numberChildrenAtHome = int(lstCustomer[12])
            self.houseOwnerFlag = bool(lstCustomer[13])
            self.numberCarsOwned = int(lstCustomer[14])
            self.addressLine1 = lstCustomer[15]
            self.phone = lstCustomer[16]
            self.dateFirstPurchase = datetime.strptime(lstCustomer[17], "%m/%d/%Y")
        except Exception as ex:
            print(f"Can not convert customer row: {lstCustomer[0]} | {ex}")
    
    def GetListFormat(self):
        return [self.customerKey, self.geographyKey, self.customerAlternateKey, self.firstName, self.middleName, self.lastName, self.birthDate, self.maritalStatus,\
                self.gender, self.emailAddress, self.yearlyIncome, self.totalChildren, self.numberChildrenAtHome, self.houseOwnerFlag, self.numberCarsOwned, self.addressLine1,\
                self.phone, self.dateFirstPurchase]

    def __str__(self):
        return f"CustomerKey: {self.customerKey}, GeorgraphyKey: {self.geographyKey}, CustomerAlternateKey: {self.customerAlternateKey}, FirstName {self.firstName}, \
MiddleName: {self.middleName}, LastName: {self.lastName}, BirthDate: {self.birthDate}, MaritalStatus: {self.maritalStatus}, Gender: {self.gender}, \
EmailAddress: {self.emailAddress}, YearlyIncome: {self.yearlyIncome}, TotalChildren: {self.totalChildren}, NumberChildrenAtHome: {self.numberChildrenAtHome}, \
HouseOwnerFlag: {self.houseOwnerFlag}, NumberCarsOwned: {self.numberCarsOwned}, AddressLine1: {self.addressLine1}, Phone: {self.phone}, DateFirstPurchase: {self.dateFirstPurchase}"

class Date:
    def __init__(self, lstDate):
       self.TransformDate(lstDate)

    def TransformDate(self, lstDate):
        try:
            self.dateKey = lstDate[0]
            self.fullDate = datetime.strptime(lstDate[1], "%m/%d/%Y")
            self.dayName = lstDate[2] 
            self.dayNumber = int(lstDate[3])
            self.monthName = lstDate[4]
            self.monthNumber = int(lstDate[5])
            self.quarterNumber = int(lstDate[6])
            self.year = int(lstDate[7])
        except Exception as ex:
            print(f"Can not convert date row: {lstDate[0]} | {ex}")
    
    def GetListFormat(self):
        return [self.dateKey, self.fullDate, self.dayName, self.dayNumber, self.monthName, self.monthNumber, self.quarterNumber, self.year]

    def __str__(self):
        return f"dateKey: {self.dateKey}, fullDate: {self.fullDate}, dayName: {self.dayName}, dayNumber: {self.dayNumber}, monthName: {self.monthName}, quarterNumber: {self.quarterNumber}, year: {self.year}"

class Employee:
    def __init__(self, lstEmployee):
        self.TransformEmployee(lstEmployee)
                 
    def TransformEmployee(self, lstEmployee):
        try:
            self.employeeKey = lstEmployee[0]
            self.parentEmployeeKey = lstEmployee[1]
            self.salesTerritoryKey = lstEmployee[2]
            self.firstName = lstEmployee[3]
            self.middleName = lstEmployee[4]
            self.lastName = lstEmployee[5]
            self.nameStyle = int(lstEmployee[6])
            self.title = lstEmployee[7]
            self.hireDate = datetime.strptime(lstEmployee[8], "%m/%d/%Y")
            self.birthDate = datetime.strptime(lstEmployee[9], "%m/%d/%Y")
            self.emailAddress = lstEmployee[10]
            self.phone = lstEmployee[11]
            self.maritalStatus = lstEmployee[12]
            self.salariedFlag = bool(lstEmployee[13])
            self.gender = lstEmployee[14]
            self.payFrequency = bool(lstEmployee[15])
            self.baseRate = float(lstEmployee[16])
            self.vacationHours = int(lstEmployee[17])
            self.sickLeaveHours = int(lstEmployee[18])
            self.departmentName = lstEmployee[19]
            self.startDate = datetime.strptime(lstEmployee[20], "%m/%d/%Y")
            if lstEmployee[21].upper() != "NULL":
                self.endDate = datetime.strptime(lstEmployee[21], "%m/%d/%Y")
            else:
                self.endDate = datetime(1900, 1, 1)
        except Exception as ex:
            print(f"Can not convert employee row: {lstEmployee[0]} | {ex}")
    
    def GetListFormat(self):
        return [self.employeeKey, self.parentEmployeeKey, self.salesTerritoryKey, self.firstName, self.middleName, self.lastName, self.nameStyle, self.title, self.hireDate, \
                self.birthDate, self.emailAddress, self.phone, self.maritalStatus, self.salariedFlag, self.gender, self.payFrequency, self.baseRate, self.vacationHours, \
                self.sickLeaveHours, self.departmentName, self.startDate, self.endDate]

    def __str__(self):
        return f"employeeKey:{self.employeeKey}, parentEmployeeKey: {self.parentEmployeeKey}, salesTerritoryKey: {self.salesTerritoryKey}, firstName: {self.firstName}, middleName: {self.middleName},\
lastName: {self.lastName}, nameStyle: {self.nameStyle}, title: {self.title}, hireDate: {self.hireDate}, birthDate: {self.birthDate}, emailAddress: {self.emailAddress}, phone: {self.phone}, \
maritalStatus: {self.maritalStatus}, salariedFlag: {self.salariedFlag}, gender: {self.gender}, payFrequency: {self.payFrequency}, baseRate: {self.baseRate}, vacationHours: {self.vacationHours}, \
sickLeaveHours: {self.sickLeaveHours}, departmentName: {self.departmentName}, startDate: {self.startDate}, endDate: {self.endDate}"  

class Geography:
    def __init__(self, lstGeography):
       self.TransformGeography(lstGeography)

    def TransformGeography(self, lstGeography):
        try:
            self.geographyKey = lstGeography[0]
            self.city = lstGeography[1]
            self.stateProvinceCode = lstGeography[2]
            self.stateProvinceName = lstGeography[3]
            self.countryRegionCode = lstGeography[4]
            self.englishCountryRegionName = lstGeography[5]
            self.spanishCountryRegionName = lstGeography[6]
            self.frenchCountryRegionName = lstGeography[7]
            self.postalCode = lstGeography[8]
            self.salesTerritoryKey = lstGeography[9]
        except Exception as ex:
            print(f"Can not convert date row: {lstGeography[0]} | {ex}")
    
    def GetListFormat(self):
        return [self.geographyKey, self.city, self.stateProvinceCode, self.stateProvinceName, self.countryRegionCode, self.englishCountryRegionName, self.spanishCountryRegionName, self.frenchCountryRegionName, self.postalCode, self.salesTerritoryKey]

    def __str__(self):
        return f"geographyKey: {self.geographyKey}, city: {self.city}, stateProvinceCode: {self.stateProvinceCode}, stateProvinceName: {self.stateProvinceName}, countryRegionCode: {self.countryRegionCode}, \
englishCountryRegionName: {self.englishCountryRegionName}, spanishCountryRegionName: {self.spanishCountryRegionName}, frenchCountryRegionName: {self.frenchCountryRegionName}, \
postalCode: {self.postalCode}, salesTerritoryKey: {self.salesTerritoryKey}"
    
class Order:
    def __init__(self, lstOrder):
       self.TransformOrder(lstOrder)

    def TransformOrder(self, lstOrder):
        try:
            self.dateKey = lstOrder[0]
            self.customerKey = lstOrder[1]
            self.employeeKey = ""
            self.geographyKey = ""
            self.productKey = lstOrder[2]
            self.orderQuantity = int(lstOrder[3])
        except Exception as ex:
            print("Cannot convert order row with DateKey: {}, CustomerKey: {}, ProductKey: {}".format(lstOrder[0], lstOrder[1], lstOrder[2]), f"| Error: {ex}")
    
    def GetListFormat(self):
        return [self.customerKey, self.dateKey, self.employeeKey, self.geographyKey, self.productKey, self.orderQuantity]

    def __str__(self):
        return f"customerKey: {self.customerKey}, dateKey: {self.dateKey}, employeeKey: {self.employeeKey}, geographyKey: {self.geographyKey}, productKey: {self.productKey}, \
orderQuantity: {self.orderQuantity}"
    
class Product:
    def __init__(self, id, title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images):
        try:
            self.id = id
            self.title = title 
            self.description = description 
            self.price = float(price)
            self.discountPercentage = float(discountPercentage)
            self.rating = float(rating)
            self.stock = int(stock)
            self.brand = brand 
            self.category = category 
            self.thumbnail = thumbnail 
            self.images = images
        except Exception as ex:
            print(f"Cannot convert product row with product id: {id} | {ex}")

    def GetImages(self):
        return ", ".join(self.images)    
    
    def GetListFormat(self):
        return [self.id, self.title, self.description, self.price, self.discountPercentage, self.rating, self.stock, self.brand, self.category, self.thumbnail, self.GetImages()]

    def GetCSVFormat(self):
        return f"{self.id},{self.title},{self.description},{self.price},{self.discountPercentage},{self.rating},{self.stock},{self.brand},{self.category},{self.thumbnail},{self.GetImages()}"

    def __str__(self):
        return f"id: {self.id}, title: {self.title}, description: {self.description}, price: {self.price}, discountPercentage: {self.discountPercentage}, rating: {self.rating}, \
stock: {self.stock}, brand: {self.brand}, category: {self.category}, thumbnail: {self.thumbnail}, images: {self.GetImages()}"