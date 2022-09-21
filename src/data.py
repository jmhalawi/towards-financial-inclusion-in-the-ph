# This script is for processing the data
import pandas as pd

class ProcessData:
    def load_data():
    # Loading the data
        data = pd.read_csv("micro_world.csv")
        
        return data
    
    # Filtering Philippine data
    def filter_data(data):
        # Filter Philippine Data
        philippine_data = data[
            (data['economy'] == 'Philippines')&(data['age'] > 20)
        ]

        # Add new column to dataframe for those without bank accounts
        philippine_data['no_accounts'] = philippine_data.apply(
        lambda x: 1 if x['fin11a'] == 1 or x['fin11b'] == 1 or x['fin11c'] == 1 or x['fin11d'] == 1 or x['fin11e'] == 1 or x['fin11f'] == 1 or x['fin11g'] == 1 or x['fin11h'] == 1
        or x['fin11a'] == 2 or x['fin11b'] == 2 or x['fin11c'] == 2 or x['fin11d'] == 2 or x['fin11e'] == 2 or x['fin11f'] == 2 or x['fin11g'] == 2 or x['fin11h'] == 2
        or x['fin11a'] == 3 or x['fin11b'] == 3 or x['fin11c'] == 3 or x['fin11d'] == 3 or x['fin11e'] == 3 or x['fin11f'] == 3 or x['fin11g'] == 3 or x['fin11h'] == 3
        or x['fin11a'] == 4 or x['fin11b'] == 4 or x['fin11c'] == 4 or x['fin11d'] == 4 or x['fin11e'] == 4 or x['fin11f'] == 4 or x['fin11g'] == 4 or x['fin11h'] == 4
        else 0, axis=1
        )

        # Create another column for each reason why they don't have bank account
        get_reason(philippine_data, 'r_too_far', 'fin11a')
        get_reason(philippine_data, 'r_too_expensive', 'fin11b')
        get_reason(philippine_data, 'r_lack_documentation', 'fin11c')
        get_reason(philippine_data, 'r_trust', 'fin11d')
        get_reason(philippine_data, 'r_religious_reasons', 'fin11e')
        get_reason(philippine_data, 'r_lack_of_money', 'fin11f')
        get_reason(philippine_data, 'r_family_already_have', 'fin11g')
        get_reason(philippine_data, 'r_no_need_for_fs', 'fin11h')

        return philippine_data

# This method adds a new column to the dataframe for each reason
def get_reason(data, new_col, col_name ):
    data[new_col] = data.apply(
        lambda x: 1 if x[col_name] == 1 else 0, axis=1
    )

