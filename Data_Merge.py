import pathlib
import zipfile
import pandas as pd
from tqdm.auto import tqdm
import numpy as np

data_pd = pd.DataFrame()

zip_files_directory = pathlib.Path("Zip-file-local-path")
zip_filepaths = list(zip_files_directory.glob('*.zip'))

for zip_filepath in tqdm(zip_filepaths):
    with zipfile.ZipFile(zip_filepath) as czip:
        csv_name = zip_filepath.name.replace('.zip', '.csv')
        temp_pd = pd.read_csv(czip.open(csv_name))
        data_pd = pd.concat([data_pd, temp_pd])

data_pd = data_pd.reset_index(drop=True)

print(f'{data_pd.shape = }')

data_pd.to_csv("storage-path", index=False)
