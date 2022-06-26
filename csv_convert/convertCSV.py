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

    def create_new_transformed_csv(self):
        transformed_file = ''
        # create a new dir if it does not exist
        path = os.path.join(BASE_DIR, 'transformed_csv_files')
        if not os.path.exists(path):
            os.makedirs(path)

        transformed_data = self._transform()
        if transformed_data is None:
            return None

        if self.is_test:
            transformed_file = 'new_test' + self.file + '.csv'
        else:
            # create a unique file
            transformed_file = self.file.filename.replace(
                '.csv', '_' + uuid.uuid4().hex[:10]) + '.csv'

        transformed_data.to_csv((path + '/' + transformed_file),
                        index=False, encoding='utf-8')

        # return file dir
        return path + '/' + transformed_file

    def _open_file(self):
        generated_random_file = "3"
        # testing cases
        if self.is_test:
            try:
                # if the user select to generate a new random data for the test file
                if self.file == generated_random_file:
                    Generator(BASE_DIR).generate()

                return pd.read_csv(self._get_test_file(),
                                   encoding='utf-8',
                                   names=['id', 'date', 'game name', 'country code', \
                                    'copies sold', 'price'])

            except FileNotFoundError:
                return None

        # user uploaded CSV file
        else:
            return pd.read_csv(self.file,
                               encoding='utf-8',
                               names=['id', 'date', 'game name', 'country code', 'copies sold', 'price'])

    def _transform(self):
        try:
            '''check data's format. If it is correct format, then create the new transformed file'''
            data_frame = self._open_file()
            return FD(data_frame).new_data_frame()

        except:
            return None

    def _get_test_file(self):
        return os.path.join(BASE_DIR, 'test_files/test' + self.file + '.csv')
