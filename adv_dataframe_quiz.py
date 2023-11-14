import pandas as pd

def remove_empty_col(df):
    pass
    
def remove_any_missing_row(df):
    pass

def change_data_type(df):
    pass

def merge_data(left, right):
    pass

def main():
    test_data = pd.read_csv("student_data.csv")
    print(test_data)
    test_data = remove_empty_col(test_data)
    test_data = remove_any_missing_row(test_data)
    test_data = change_data_type(test_data)
    
    demographic_data = pd.read_csv("student_demo_data.csv")
    merged_data = merge_data(test_data, demographic_data)
    
    
    
    

    
    
    
    print(df)

if __name__ == "__main__":
    main()