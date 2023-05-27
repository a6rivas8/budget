import pandas as pd


FILEPATH = "buddy_export.csv"


def total_spent_by_head_category(budget: pd.DataFrame):
    budget = budget[budget.HEAD_CATEGORY != "Income"]
    print(budget.groupby(by=['HEAD_CATEGORY']).sum()['AMOUNT'])


def total_spent_by_category(budget: pd.DataFrame):
    budget = budget[budget.HEAD_CATEGORY != "Income"]
    print(budget.groupby(by=['CATEGORY']).sum()['AMOUNT'])


def main():
    # I need to add an AMOUNT column to the csv before running this
    budget_dataframe = pd.read_csv(FILEPATH, sep=';')
    budget_dataframe.rename(columns={
                                        'Head categor': 'HEAD_CATEGORY', 
                                        'Date': 'DATE', 
                                        'Category': 'CATEGORY', 
                                        'Note': 'NOTE', 
                                        'Amount': 'AMOUNT'
                                    },
                            inplace=True)

    print(budget_dataframe[budget_dataframe.HEAD_CATEGORY == "Miscellaneous"])

    budget_dataframe = budget_dataframe[~budget_dataframe.NOTE.str.contains("Tio Carlos", na=False)]
    total_spent_by_category(budget_dataframe)


if __name__ == '__main__':
    main()