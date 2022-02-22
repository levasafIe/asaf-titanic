import pandas as pd


def extract_titles(name):
    # if pd.Series(name).str.contains(".", regex=False)[0]:
    if "." in name:
        return name.split()[0]
    else:
        raise ValueError


if __name__ == "__main__":
    print("Script ran successfully")
