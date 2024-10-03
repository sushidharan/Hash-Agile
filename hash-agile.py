class EmployeeCollection:
    def __init__(self):
        self.collections = {}

#Create a new collection
    def create_collection(self, p_collection_name):
        self.collections[p_collection_name] = []
        print(f"Collection '{p_collection_name}' created.")



#Index employee data with sample employee data
    def index_data(self, p_collection_name, p_exclude_column):
        employee_data = [
            {'id': '101', 'name': 'Alice', 'department': 'HR', 'gender': 'Female', 'salary': 50000},
            {'id': '102', 'name': 'Bob', 'department': 'DE', 'gender': 'Male', 'salary': 60000},
            {'id': '103', 'name': 'Charlie', 'department': 'DA', 'gender': 'Male', 'salary': 55000},
            {'id': '104', 'name': 'David', 'department': 'SALES', 'gender': 'Male', 'salary': 40000},
        ]

        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return



        for employee in employee_data:
            indexed_employee = {k: v for k, v in employee.items() if k != p_exclude_column}
            self.collections[p_collection_name].append(indexed_employee)

        print(f"Indexed data into '{p_collection_name}', excluding column '{p_exclude_column}'.")

    def search_by_column(self, p_collection_name, p_column_name, p_column_value):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return []

        results = [
            emp for emp in self.collections[p_collection_name]
            if emp.get(p_column_name) == p_column_value
        ]
        return results

    def get_emp_count(self, p_collection_name):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return 0

        count = len(self.collections[p_collection_name])
        print(f"Employee count in '{p_collection_name}': {count}")
        return count

    def del_emp_by_id(self, p_collection_name, p_employee_id):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return False

        collection = self.collections[p_collection_name]
        for emp in collection:
            if emp.get('id') == p_employee_id:
                collection.remove(emp)
                print(f"Deleted employee with ID {p_employee_id} from '{p_collection_name}'.")
                return True

        print(f"Employee with ID {p_employee_id} not found in '{p_collection_name}'.")
        return False

    def get_dep_facet(self, p_collection_name):
        if p_collection_name not in self.collections:
            print(f"Collection '{p_collection_name}' does not exist.")
            return {}

        dep_count = {}
        for emp in self.collections[p_collection_name]:
            dep = emp.get('department')
            if dep:
                dep_count[dep] = dep_count.get(dep, 0) + 1

        print(f"Department facet in '{p_collection_name}': {dep_count}")
        return dep_count



# Execution of specified functions
v_nameCollection = 'Alice'
v_phoneCollection = '9897923231'

collection_manager = EmployeeCollection()
collection_manager.create_collection(v_nameCollection)
collection_manager.create_collection(v_phoneCollection)

# Function executions
collection_manager.get_emp_count(v_nameCollection)
collection_manager.index_data(v_nameCollection, 'Department')
collection_manager.index_data(v_phoneCollection, 'Gender')
collection_manager.del_emp_by_id(v_nameCollection, '101')
collection_manager.get_emp_count(v_nameCollection)

# Search operations
results1 = collection_manager.search_by_column(v_nameCollection, 'Department', 'IT')
print("Search Results (Department: IT):", results1)

results2 = collection_manager.search_by_column(v_nameCollection, 'Gender', 'Male')
print("Search Results (Gender: Male):", results2)

results3 = collection_manager.search_by_column(v_phoneCollection, 'Department', 'IT')
print("Search Results (Phone Collection, Department: IT):", results3)

# Get department
dep_facet1 = collection_manager.get_dep_facet(v_nameCollection)
dep_facet2 = collection_manager.get_dep_facet(v_phoneCollection)
