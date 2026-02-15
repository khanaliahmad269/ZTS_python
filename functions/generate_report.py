'''write d function generate_report() that calls

.fetch_sales()

.filter_valid_orders()

.summaraize_data()



Task:

.generate_report()

'''

def fetch_sales():
    print("fetch sales function is called")

def filter_valid_orders():
    print("valid order function is called")

def summarize_data():
    print("Summarize data called")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("The report is generated")

generate_report()