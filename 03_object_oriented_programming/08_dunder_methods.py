class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    # this is similar to overriding the toString() method in Java
    def __str__(self):
        return f"This is an action figure in color {self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return f"Yes???"

    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('red', 0)

# both are same
print(action_figure.__str__())
print(str(action_figure))

print(action_figure.__len__())
print(len(action_figure))

print(action_figure())

print(action_figure['name'])
print(action_figure['has_pets'])
