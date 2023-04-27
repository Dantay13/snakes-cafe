"""
This is my lab 1 assignment: snake cafe assigment
"""


def main():
    """
    Do my docstring here
    """
    order_name = input("Hi, can you please enter a name for your order? >")

    print(f"Thank you! Your order name is {order_name}")

    menu = """**************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    """
    print(menu)

    ask_order = """
    ***********************************
    ** What would you like to order? **
    ***********************************"""
    print(ask_order)

    order_book = {}

    while True:
        customer_order = input("> ")
        if customer_order == "quit":
            break
        if customer_order in order_book:
            order_book[customer_order] += 1
        else:
            order_book[customer_order] = 1
        print(f"** {order_book[customer_order]} order of {order_book} has been added to your meal **")

        print(ask_order)


if __name__ == "__main__":
    main()
