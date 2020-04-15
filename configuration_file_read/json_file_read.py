import json


def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


@auto_str
class Employee:
    def __init__(self, userId, jobTitleName, firstName, lastName, preferredName, employeeCode, region, phone, email):
        self.userId = userId
        self.jobtype = jobTitleName
        self.firstName = firstName
        self.lastName = lastName
        self.preferredFullName = preferredName
        self.employeeCode = employeeCode
        self.region = region
        self.phoneNumber = phone
        self.email = email


def json_processing():
    with open('employee_detail.json', 'r') as json_data:
        data = json.load(json_data)
        # print(type(data))
        # print(len(data['Employees']))
        # print(data['Employees'])
        emp_list = data['Employees']
        for emp in emp_list:
            # extract fields from each dictionary
            userid = emp.get('userId')
            jobtype = emp.get('jobTitleName')
            fname = emp.get('firstName')
            lname = emp.get('lastName')
            full_name = emp.get('preferredFullName')
            employeecode = emp.get('employeeCode')
            region = emp.get('region')
            phone = emp.get('phoneNumber')
            email = emp.get('emailAddress')
            employee = Employee(userid, jobtype, fname, lname, full_name, employeecode, region, phone, email)
            print(employee)
            # print(emp.keys())


def main():
    json_processing()


if __name__ == "__main__":
    main()
