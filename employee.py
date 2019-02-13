class Employee:
    def __init__(self, id=None, name=None, salary=None, age=None, profile_image=None):
        self.id = id

        self.name = name

        self.salary = salary

        self.age = age

        self.profile_image = profile_image

    @property
    def to_string(self):
        object_string = 'id: %s, name: %s, salary:%s, age: %s' \
                        % (self.id, self.name, self.salary, self.age)
        return object_string