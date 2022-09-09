from io import StringIO
import sys
import logging
from dvc import api
import pandas as pd

from pandas.core.tools import numeric

logging.basicConfig(
    format = '%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logger.info('Fetching data ...')

movie_data_path = api.read('data/movies.csv', remote='data_storage')
finantials_data_path = api.read('data/finantials.csv', remote='data_storage')
logger = logging.getLogger(__name__)
opening_gros_data_path = api.read('data/opening_gross.csv', remote='data_storage')

movie_data = pd.read_csv(StringIO(movie_data_path))
finantials_data = pd.read_csv(StringIO(finantials_data_path))
opening_gros_data = pd.read_csv(StringIO(opening_gros_data_path))

numeric_columns_mask = (movie_data.dtypes ==float) | (movie_data.dtypes == int)
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]
movie_data = movie_data[numeric_columns + ["movie_title"]]

finantials_data = finantials_data[['movie_title', 'production_budget', 'worldwide_gross']]
fin_movie_data = pd.merge(finantials_data, movie_data, on='movie_title', how='left')
full_movie_data = pd.merge(opening_gros_data, fin_movie_data, on='movie_title', how='left')

full_movie_data = full_movie_data.drop(['gross', 'movie_title'], axis=1)

full_movie_data.to_csv('data/full_data.csv', index=False)

logger.info('Data Fetched and prepared')