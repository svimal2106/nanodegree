class Parent:
    """Base class for a family"""
    def __init__(self, eye_color, last_name):
        self.eye_color = eye_color
        self.last_name = last_name

    def to_string(self):
        return "Parent(" + self.eye_color + ", " + self.last_name + ")"


class Child(Parent):
    """Child class"""
    def __init__(self, eye_color, last_name, height):
        Parent.__init__(self, eye_color, last_name)
        self.height = height

    def to_string(self):
        return "Child(" + self.eye_color + ", " + self.last_name + "," + self.height + ")"


p1 = Parent("black", "chawla")
c1 = Child("blue", "sharma", "185")
print p1.to_string()
print c1.to_string()