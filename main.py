from functions import json_to_csv


JSON_FILE_NAME = "input.json"
CSV_FILE_NAME = "output.csv"


if __name__ == "__main__":
    json_to_csv(JSON_FILE_NAME, CSV_FILE_NAME)
    print("Done!")