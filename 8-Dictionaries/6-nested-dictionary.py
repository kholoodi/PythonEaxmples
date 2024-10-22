#Build the nested dictionaries
customers  = {'customer1': {'id': 1, 'name': 'Noor', 'size': 37},
			  'customer2': {'id': 2, 'name': 'Mona', 'size': 36},
			  'customer3': {'id': 3, 'name': 'Sara', 'size': 38},
              }
#OR
customer1 = {'id': 1, 'name': 'Noor', 'size': 37}
customer2 = {'id': 2, 'name': 'Mona', 'size': 36}
customer3 = {'id': 3, 'name': 'Sara', 'size': 38}

customers=  {'customer1': customer1,
			 'customer2': customer2, 
			 'customer3':customer3
             }

#To access items in nested dictionaries
print(customers['customer1']['name'])