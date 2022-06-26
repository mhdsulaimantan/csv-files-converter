import pycountry
import pandas as pd


class FD:

    def __init__(self, df):
        self.df = df

    # change game name formation

    def game_name(self):
        # split the name at '-' and capitalize every word
        return self.df['game name'].apply(lambda game: ' '.join(word.capitalize() for word in game.split('-')))

    # change the country code to the name of the country

    def country_name(self):
        return self.df['country code'].apply(lambda code: pycountry.countries.get(alpha_3=code.upper()).name)

    # calculating the total revenue for each game (copied sold * price)

    def total_revenue(self):
        return list(map(lambda copy, price: str(round(copy * float(price.replace('USD', '')))) + ' USD', self.df['copies sold'], self.df['price']))

    # creating a new data frame for the new data formation

    def new_data_frame(self):
        data_list = [list(self.df['id']), self.df['date'], self.game_name(
        ), self.country_name(), self.df['copies sold'], self.df['price'], self.total_revenue()]

        # data_list rows as columns in the new dataFrame
        new_df = pd.DataFrame(data_list).transpose()

        new_df.columns = ['ID', 'Release Date', 'Name',
                          'Country', 'Copies Sold', 'Copy Price', 'Total Revenue']

        return self.sort_by_date(new_df)

    # sort data frame by its date

    def sort_by_date(self, data_frame):
        # changing the format for release date to be able to sort the data frame by date
        data_frame['Release Date'] = pd.to_datetime(data_frame['Release Date'])
        data_frame = data_frame.sort_values('Release Date')

        # change release date format to (DD.MM.YYYY)
        data_frame['Release Date'] = data_frame['Release Date'].dt.strftime(
            '%d.%m.%Y')

        return data_frame
