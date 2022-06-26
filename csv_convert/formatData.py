import pycountry
import pandas as pd


class FD:

    def __init__(self, df):
        self.df = df

    def new_data_frame(self):
        ''' creating a new data frame for the new transformed data'''
        data_list = [list(self.df['id']), self.df['date'], self._game_name(
        ), self._country_name(), self.df['copies sold'], self.df['price'], self._total_revenue()]

        new_df = pd.DataFrame(data_list).transpose()

        new_df.columns = ['ID', 'Release Date', 'Name',
                          'Country', 'Copies Sold', 'Copy Price', 'Total Revenue']

        return self._sort_by_date(new_df)

    def _game_name(self):
        ''' split the name at '-' and capitalize every word '''
        return self.df['game name'].apply(lambda game: ' '.join(word.capitalize() for word in game.split('-')))


    def _country_name(self):
        ''' transform country code to name '''
        return self.df['country code'].apply(lambda code: pycountry.countries.get(alpha_3=code.upper()).name)


    def _total_revenue(self):
        ''' calculate the total revenue per game (copied sold * price) '''
        return list(map(lambda copy, price: str(round(copy * float(price.replace('USD', '')))) + ' USD', self.df['copies sold'], self.df['price']))

    def _sort_by_date(self, data_frame):
        data_frame['Release Date'] = pd.to_datetime(data_frame['Release Date'])
        data_frame = data_frame.sort_values('Release Date')

        # change release date format to (DD.MM.YYYY)
        data_frame['Release Date'] = data_frame['Release Date'].dt.strftime(
            '%d.%m.%Y')

        return data_frame
