from pycountry import countries
from nltk.corpus import words
import pandas as pd
import os
import random
import nltk
# download nltk list of words to use it in generate random game names
nltk.download('words')


class Generator:
    def __init__(self, BASE_DIR):
        self.BASE_DIR = BASE_DIR

    # generate a random data that match our formation
    def generate(self):
        id_list, release_date, game_name, country_code, copies_sold, price = [], [], [], [], [], []
        id = 1
        # generate data with 5 to 20 rows
        for row in range(random.randint(5, 20)):
            id_list.append(id)
            id += 1

            release_date.append(str(random.randint(1980, 2022)) + '/' +
                                str(random.randint(1, 12)) + '/' + str(random.randint(1, 30)))

            # generate a game name contains 1 to 3 words
            name = ""
            for x in range(random.randint(1, 4)):
                if name == "":
                    # pick words that have less or equal to 5 characters
                    name += random.choice(list(word for word in words.words()
                                          if len(word) <= 5))
                else:
                    name += '-' + \
                        random.choice(
                            list(word for word in words.words() if len(word) <= 5))

            game_name.append(name)

            # randomly pick an alpha-3 country code for 249 countries
            country_code.append(
                list(countries)[random.randint(0, 248)].alpha_3)

            copies_sold.append(random.randint(1000, 10000000))

            price.append(str(round(random.uniform(5, 100), 2)) + ' USD')

        data_list = [id_list, release_date, game_name,
                     country_code, copies_sold, price]

        # data_list rows is columns in the new data frame
        df = pd.DataFrame(data_list).transpose()

        # save the randomly generated data frame as CSV file in test_files dir
        path = os.path.join(self.BASE_DIR, 'test_files')

        df.to_csv((path + '/test3.csv'), header=False,
                  index=False, encoding='utf-8')
