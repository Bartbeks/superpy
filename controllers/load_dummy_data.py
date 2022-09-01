from classes.product import Product

def load_example_data():
    dummy_data=["tomaat" " 1.90" " 7" " 2023-08-25" " true",
            " bananen" " 1.90" " 2"  " 2023-08-25" " true",
            "appel " " 3.10" " 5" " 2022-08-31" " true",
            "kiwi " " 3.10" " 5" " 2022-08-29" " true"


]
    for prod in dummy_data:
        prod.split()
        Product.add_product(prod.split()[0], prod.split()[1],prod.split()[2], prod.split()[3], prod.split()[4])
