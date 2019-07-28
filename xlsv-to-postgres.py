import psycopg2
import pandas
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from sqlalchemy import create_engine

# make sure your postgres database is owned by the user postgres, not a user with your local username
# if the postgres user does not exist: `createuser --superuser postgres`
# to make the postgres user owner of the postgres database: (1) `psql postgres`, (2) `ALTER DATABASE postgres OWNER TO postgres;`

engine = create_engine('postgresql://postgres@localhost:5432/postgres')

df = pandas.read_excel('../NCDB_Sample_Population_10jun2019.xlsx')
df.to_sql('ncdb_population_addendum', engine)
