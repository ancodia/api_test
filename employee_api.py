import requests
from employee import Employee

base_url = 'http://dummy.restapiexample.com'


def create_employee(name=None, salary=None, age=None, profile_image=None):
    name_json = name if name is not None else ''
    salary_json = salary if salary is not None else ''
    age_json = age if age is not None else ''
    profile_image_json = profile_image if profile_image is not None else ''

    data = {'name': '%s' % name_json,
            'salary': '%s' % salary_json,
            'age': '%s' % age_json,
            'profile_image': '%s' % profile_image_json}
    url = base_url + '/api/v1/create'
    response = requests.post(url, json=data)
    status = response.status_code
    assert status == 200

    response_json = response.json()
    employee_id = response_json['id']
    print('>Employee was created, ID:%s' % employee_id)

    employee = Employee(id=employee_id, name=name, salary=salary, age=age, profile_image=profile_image)
    return employee


def get_employee(employee_id):
    url = base_url + '/api/v1/employee/%s' % employee_id
    response = requests.get(url)
    status = response.status_code
    assert status == 200
    print('>Employee found')

    response_json = response.json()
    existing_employee = Employee(id=response_json['id'],
                                 name=response_json['employee_name'],
                                 salary=response_json['employee_salary'],
                                 age=response_json['employee_age'],
                                 profile_image=response_json['profile_image'])
    return existing_employee


def compare_employee_objects(employee1, employee2):
    assert employee1.id == employee2.id
    assert employee1.name == employee2.name
    assert employee1.salary == employee2.salary
    assert employee1.age == employee2.age

    # POST employee response has profile_image in it but it is not returned with GET employee request
    # assert employee1.profile_image == employee2.profile_image
    print('>Employee details are equal')


def update_employee(employee, name=None, salary=None, age=None):
    name_json = name if name is not None else employee.name
    salary_json = salary if salary is not None else employee.salary
    age_json = age if age is not None else employee.age

    data = {'name': '%s' % name_json,
            'salary': '%s' % salary_json,
            'age': '%s' % age_json}
    url = base_url + '/api/v1/update/%s' % employee.id
    response = requests.put(url, json=data)
    status = response.status_code
    assert status == 200
    print('>Employee was updated')

    response_json = response.json()
    employee.name = response_json['name']
    employee.salary = response_json['salary']
    employee.age = response_json['age']


def delete_employee(employee):
    url = base_url + '/api/v1/delete/%s' % employee.id
    response = requests.delete(url)
    status = response.status_code
    assert status == 200
    print('>Employee was deleted')


def employee_does_not_exist(employee):
    url = base_url + '/api/v1/employee/%s' % employee.id
    response = requests.get(url)
    content = response.content
    assert content.decode("utf-8") == 'false'
    print('>Employee not found')


if __name__ == "__main__":
    print('Creating employee record:')
    new_employee = create_employee(name='Employee1',
                                   salary="24000",
                                   age="33",
                                   profile_image='resources/image.png')

    employee_from_api = get_employee(new_employee.id)
    compare_employee_objects(new_employee, employee_from_api)

    print('\nUpdating employee record:')
    update_employee(new_employee, salary='42000')
    updated_employee = get_employee(new_employee.id)
    compare_employee_objects(new_employee, updated_employee)

    print('\nDeleting employee record:')
    delete_employee(new_employee)
    employee_does_not_exist(new_employee)

