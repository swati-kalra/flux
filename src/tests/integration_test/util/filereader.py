import json
import pandas as pd
import logging

def read_json_file_and_return_json_data(file_path):
    data = read_file("json", file_path)
    return data


def read_csv_file_and_return_json_data(file_path):
    data = read_file("csv", file_path)
    return data


def read_excel_file_and_return_json_data(file_path):
    data = read_file("excel", file_path)
    return data


def read_file(file_type, file_path):
    try:
        if file_type == "json":
            f = open(file_path, mode="r")
            json_data = json.load(f)
            return json_data
        if file_type == "csv":
            data = pd.read_csv(file_path)
            return data
        if file_type == "excel":
            data = pd.read_excel(file_path)
            return data
    except FileNotFoundError:
        logging.error("File not found!!")
    except Exception:
        logging.error("Something wrong with the file")
