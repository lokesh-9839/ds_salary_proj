import glassdoor_scraper as gs

import pandas as pd

path = "C:/Users/DELL/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs (' dato scientist ', 15 ,False, path, 15)

df.to_csv("glassdoor.jobs_csv",index = False)