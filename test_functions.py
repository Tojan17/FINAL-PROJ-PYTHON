import functions_Aid_distribution_program as funs
def test_add_shipment():
    data = []
    funs.add_shipment(data)
    print(data)

def test_search_item():
    data = [
        {
            "item":"Rice",
            "quantity":10,
            "donor":"UNRWA"
        }
    ]
    funs.search_item(data)

def test_report():
    data = [
        {
            "item":"Rice",
            "quantity":20,
            "donor":"UNRWA"
        }
    ]
    funs.report(data)


test_add_shipment()
test_search_item()
test_report()