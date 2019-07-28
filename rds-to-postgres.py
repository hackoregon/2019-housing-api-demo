import psycopg2
import pandas
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from sqlalchemy import create_engine

# make sure your postgres database is owned by the user postgres, not a user with your local username
# if the postgres user does not exist: `createuser --superuser postgres`
# to make the postgres user owner of the postgres database: (1) `psql postgres`, (2) `ALTER DATABASE postgres OWNER TO postgres;`

pandas2ri.activate()
engine = create_engine('postgresql://postgres@localhost:5432/postgres')
readRDS = robjects.r['readRDS']

df = readRDS('~/hmda_orwa_final_clean_df.RDS')
df = pandas2ri.ri2py_dataframe(df)
df.to_sql('hmda_orwa', engine)
