import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def export_csv(df: pd.DataFrame, path: str):
    """
    The functions provided allow for exporting a pandas DataFrame to various file formats such as CSV,
    JSON, Parquet, and Feather.
    
    :param df: A pandas DataFrame containing the data to be exported
    :type df: pd.DataFrame
    :param path: The `path` parameter in the functions `export_csv`, `export_json`, `export_parquet`,
    and `export_feather` represents the file path where the DataFrame `df` will be exported in the
    respective format (CSV, JSON, Parquet, Feather). It specifies the location and name
    :type path: str
    """
    df.to_csv(path, index=False)

def export_json(df: pd.DataFrame, path: str):
    df.to_json(path, orient="records", indent=2)

def export_parquet(df: pd.DataFrame, path: str):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, path)

def export_feather(df: pd.DataFrame, path: str):
    df.to_feather(path)


