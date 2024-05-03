import employee_info as einf

def test_get_employees_by_age_range():
    result = []
    expected = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    lowrange = 24
    uprange = 33
    result = einf.get_employees_by_age_range(lowrange, uprange)
    assert(result == expected)

def test_calculate_average_salary():
    result = 0
    expected = 60166.666666666664
    result = einf.calculate_average_salary()
    assert(result == expected)

def test_get_employees_by_dept():
    result = []
    expected = ["sales good", "marketing good", "engineering good"]
    temp = []
    exp1 = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    exp2 = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
    exp3 = [{'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    temp = einf.get_employees_by_dept("Sales")
    if (temp == exp1):
        result.append("sales good")
    temp = einf.get_employees_by_dept("Marketing")
    if (temp == exp2):
        result.append("marketing good")
    temp = einf.get_employees_by_dept("Engineering")
    if (temp == exp3):
        result.append("engineering good")
    assert(result == expected)