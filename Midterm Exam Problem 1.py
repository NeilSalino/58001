class Circle:
    def __init__(self):
        self.radius = None
        self.diameter = None

    def set_radius(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def set_diameter(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.radius


radius_or_diameter = input("Enter radius or diameter: ")
if radius_or_diameter.isdigit():
    radius_or_diameter = int(radius_or_diameter)
    if radius_or_diameter > 0:

        circle = Circle()
        if radius_or_diameter > 100:
            circle.set_diameter(radius_or_diameter)
        else:
            circle.set_radius(radius_or_diameter)

        print("Area:", circle.get_area())
        print("Perimeter:", circle.get_perimeter())
    else:
        print("Invalid input: must be a positive integer")
else:
    print("Invalid input: must be a positive integer")