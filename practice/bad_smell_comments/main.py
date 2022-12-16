class Unit:
    def move(self, field, x_cord: int, y_cord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_cord + speed
                new_x = x_cord
            elif direction == 'DOWN':
                new_y = y_cord - speed
                new_x = x_cord
            elif direction == 'LEFT':
                new_y = y_cord
                new_x = x_cord - speed
            elif direction == 'RIGHT':
                new_y = y_cord
                new_x = x_cord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_cord + speed
                new_x = x_cord
            elif direction == 'DOWN':
                new_y = y_cord - speed
                new_x = x_cord
            elif direction == 'LEFT':
                new_y = y_cord
                new_x = x_cord - speed
            elif direction == 'RIGHT':
                new_y = y_cord
                new_x = x_cord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
