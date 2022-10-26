'''
OnsiteRestaurants are initiated with an additional num_tables parameter, the number of tables where customers can be seated on-site. 

These type of restaurants need the following two methods:

- occupy_table() subtracts 1 from the restaurants available_tables. 
If there are no more tables available, a Warning() should be raised.
- free_table() adds 1 to the restaurants available_tables. 
If there are as many tables available as the restaurant 
total num_tables a Warning() should be raised.
'''

from restaurant import Restaurant


class OnsiteRestaurant(Restaurant):

    def __init__(self, name, cuisine_type, num_tables, is_open=False):
        super().__init__(name, cuisine_type, is_open)
        self.__available_tables = num_tables
        self.__total_tables = num_tables

    def occupy_table(self):
        if self.__available_tables >= 1:
            self.__available_tables -= 1
        else:
            raise Warning('No more available tables.')


    def free_table(self):
        if self.__available_tables < self.__total_tables:
            self.__available_tables += 1
        else:
            raise Warning('Available tables exceeded the total number of tables.')

    def get_available_tables(self):
        return self.__available_tables