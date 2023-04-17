######
#
#   The functions in this file handle consuming products from any API
#
######
import requests
from Models import Product

######
#
#   Functions
#
######
def GetProductAPIData(productApiUrl):
    lstProducts = list()

    try:
        print("...Retrieving product API data")
        apiProductData = requests.get(productApiUrl)
        jsonProductData = apiProductData.json()        
        print("...Product API data has been retrieved")

        for product in jsonProductData.get("products"):
            lstProducts.append(Product(product.get("id"), product.get("title"), product.get("description"), product.get("price"), \
                product.get("discountPercentage"), product.get("rating"), product.get("stock"), product.get("brand"), product.get("category"), \
                product.get("thumbnail"), product.get("images")))
    except Exception as ex:
        print(ex.args[1]) 
        print("*** Failed to correctly retrieve all data from API data source")

    return lstProducts

