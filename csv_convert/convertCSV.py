import pandas as pd
import os
import uuid
from .formatData import FD
from .dataGenerator import Generator

# get script's path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Convert:

    def __init__(self, file, is_test=False):
        self.file = file
        self.is_test = is_test

    # open the CSV file

    def open_file(self):
        # check if client uploaded a file or decided to use test file
        if self.is_test:
            try:
                # picking test file 3 will generate a new data for the test file
                if self.file == "3":
                    Generator(BASE_DIR).generate()

                return pd.read_csv(self.get_test_file(),
                                   encoding='utf-8',
                                   names=['id', 'date', 'game name', 'country code', 'copies sold', 'price'])

            except FileNotFoundError:
                return None

        else:
            return pd.read_csv(self.file,
                               encoding='utf-8',
                               names=['id', 'date', 'game name', 'country code', 'copies sold', 'price'])

    # get data from the CSV file and build a new DataFrame

    def change_data_formation(self):
       # check the file's data if it have the right formation
        try:
            data_frame = self.open_file()
            return FD(data_frame).new_data_frame()

        except:
            return None

    # create CSV file with the new DataFrame

    def create_new_file(self):
        # create transformed_csv_files directory if not exist
        path = os.path.join(BASE_DIR, 'transformed_csv_files')
        if not os.path.exists(path):
            os.makedirs(path)

        # saving the DataFrame as a CSV file in transformed_csv_files dir
        new_data = self.change_data_formation()
        if new_data is None:
            return None

        # check if it is a test file
        if self.is_test:
            new_file_name = 'new_test' + self.file + '.csv'
        else:
            # create a unique file
            new_file_name = self.file.filename.replace(
                '.csv', '_' + uuid.uuid4().hex[:10]) + '.csv'

        new_data.to_csv((path + '/' + new_file_name),
                        index=False, encoding='utf-8')

        # the function return the file's path in the system
        return path + '/' + new_file_name

    # get the required test file

    def get_test_file(self):
        return os.path.join(BASE_DIR, 'test_files/test' + self.file + '.csv')
