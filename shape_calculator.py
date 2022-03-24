class Rectangle():

    def __init__(self, width, height):
        self.wid = width
        self.hei = height

    def __str__(self):
        return f'Rectangle(width={self.wid}, height={self.hei})'

    def set_width(self, width):
        self.wid = width

    def set_height(self, height):
        self.hei = height

    def get_area(self):
        area = self.wid * self.hei
        return area

    def get_perimeter(self):
        perimeter = 2 * self.wid + 2 * self.hei
        return perimeter

    def get_diagonal(self):
        diagonal = (self.wid ** 2 + self.hei ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        my_list = list()
        if self.wid > 50 or self.hei > 50:
            return 'Too big for picture.'
        else:
            for count in range(0, self.hei):
                line = (self.wid * '*') + '\n'
                my_list.append(line)
            lines = ''.join(my_list)
            return lines


    def get_amount_inside(self, shape):
        fit_wid = int(self.wid / shape.wid // 1)
        fit_hei = int(self.hei / shape.hei // 1)
        return fit_wid*fit_hei


class Square(Rectangle):
    def __init__(self, side):
        self.hei = self.wid = side

    def set_side(self, side):
        self.hei = self.wid = side

    def set_width(self, width):
        self.hei = self.wid = width

    def set_height(self, height):
        self.hei = self.wid = height

    def __str__(self):
        return f'Square(side={self.hei})'
