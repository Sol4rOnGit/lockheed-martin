import sys

#Almost there, but still incorrect

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    num_items, num_commands = map(int, sys.stdin.readline().rstrip().split())

    inventory = [] #Store lists of items with QNT, NAME, COST
    customers = [] #Store customers as list [ID, [item_NAME, QNT]]

    for _ in range(num_items):
        current_item = sys.stdin.readline().rstrip().split()
        num_of_current_item = int(current_item[0])
        current_item_name = current_item[1]
        current_item_cost = current_item[2]

        #print(current_item)
        #print(num_of_current_item, current_item_name, current_item_cost) #Works

        inventory.append([num_of_current_item, current_item_name, current_item_cost])
    
    for _ in range(num_commands):
        current_command = sys.stdin.readline().rstrip().split()

        #Get cust. ID
        current_customer_id = int(current_command[0])

        #ADD command
        if(current_command[1] == "ADD"):
            item_to_add_cart = current_command[2]
            num_item_to_add_cart = int(current_command[3])

            #print(item_to_add_cart, type(item_to_add_cart))
            #print(num_item_to_add_cart, type(num_item_to_add_cart))

            total_amt = num_item_to_add_cart

            #Check for customer's pre-existing cart
            customer_done = 0
            for customer in customers:
                if customer[0] == current_customer_id: #If customer is the same customer
                    i = 1
                    while (i < len(customer)):
                        if (customer[i][0] == item_to_add_cart): #If it has the same item
                            total_amt += customer[i][1] #Add customer items
                        
                        i+=1
                customer_done=True

            #Check allowed
            for item in inventory:
                if item[1] == item_to_add_cart:
                    if (total_amt > item[0]): #If total amount > quantity
                        print(f"Not enough {item_to_add_cart} for customer {current_customer_id}") #Disagree statement
                        customer_done = True #Don't add customer
                    else:
                        for customer in customers:
                            if customer[0] == current_customer_id: #If customer is the same customer
                                i = 1
                                while (i < len(customer)):
                                    if customer[i][0] == item_to_add_cart: #If it has the same item
                                        #Add customer items
                                        total_amt += customer[i][1] 
                                        customer[i][1] += num_item_to_add_cart
                                    else: #Create new item in customer's basket
                                        customer.append([item_to_add_cart, num_item_to_add_cart])
                                    print(f"Added {num_item_to_add_cart} {item_to_add_cart} to customer {current_customer_id}'s cart")
                                    i+=1

            #If customer not already in "db"
            if(not customer_done):
                customers.append([current_customer_id, [item_to_add_cart, num_item_to_add_cart]])
                print(f"Added {num_item_to_add_cart} {item_to_add_cart} to customer {current_customer_id}'s cart")

        #Remove
        if(current_command[1] == "REMOVE"):
            item_to_remove_cart = current_command[2]
            num_item_to_remove_cart = int(current_command[3])

            #Check for customer's pre-existing cart
            for customer in customers:
                if customer[0] == current_customer_id: #If customer is the same customer
                    i = 1
                    while (i < len(customer)):
                        if customer[i][0] == item_to_remove_cart: #If it has the same item
                            #Check it isn't more than trying to remove
                            if (customer[i][1] < num_item_to_add_cart):
                                #Deny
                                print(f"Customer {current_customer_id} does not have that many {item_to_remove_cart}s")
                            else:
                                print(f"Removed {num_item_to_remove_cart} {item_to_remove_cart} from customer {current_customer_id}'s cart")

                        i+=1
            
        if(current_command[1] == "CHECKOUT"):
            #Check for items and if they're in stock
            out_of_stock = []

            for customer in customers:
                if customer[0] == current_customer_id: #If customer is the same customer
                    i = 1
                    while (i < len(customer)):
                        
                        for item in inventory:
                            if(customer[i][0] == item[1]): #Same name
                                if (customer[i][1] > item[0]): #out of stock
                                    out_of_stock.append(item)
                        
                        i+=1
                    
                    if (out_of_stock == []):
                        #Calculate Cost
                        total_cost = 0
                        i = 1
                        while (i < len(customer)):
                            for item in inventory:
                                if(customer[i][0] == item[1]):
                                    cost = item[2] * customer[i][1]

                        total_cost = f"{total_cost:0.2f}"
                        print(f"Customer {current_customer_id}'s total: ${total_cost}")

                    else:
                        #Output sorted out of stock
                        out_of_stock = sorted(out_of_stock, key=lambda x: x[0])
                        for item in out_of_stock:
                            print(f"Out of stock of {item[1]}") #item[2] is item_name

    for item in inventory:
        print(f"{item[1]} - {item[0]}")