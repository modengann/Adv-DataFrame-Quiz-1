import pandas as pd

def remove_empty_col(df):
    pass
    
def remove_any_missing_row(df):
    pass

def mean_score(df):
    pass

def merge_data(left, right):
    pass

def main():
    raw_demo_data = {
        "StudentName": ["Alice", "Bob", "Charlie", "Diana"],
        "Advisor": ["Dr. Green", "Prof. Brown", "Dr. White", "Prof. Black"],
        "StudentID": ["2001", "2002", "2003", "2004"],
        "Major": ["Physics", "History", "English Literature", "Computer Science"],
        "Year": ["Sophomore", "Junior", "Senior", "Freshman"]
    }
    
    raw_test_data = {
        "Name": [
            "Alice", "Alice", "Alice", "Alice", "Alice",
            "Bob", "Bob", "Bob", "Bob", "Bob",
            "Charlie", "Charlie", "Charlie", "Charlie", "Charlie",
            "Diana", "Diana", "Diana", "Diana", "Diana"
        ],
        "TestID": [
            "Test01", "Test02", "Test03", "Test04", "Test05",
            "Test01", "Test02", "Test03", "Test04", "Test05",
            "Test01", "Test02", "Test03", "Test04", "Test05",
            "Test01", "Test02", "Test03", "Test04", "Test05"
        ],
        "NumberCorrect": [
            "20", "22", "23", "21", "24",
            "18", "19", "", "20", "21",
            "22", "23", "24", "25", "23",
            "19", "20", "21", "22", "23"
        ],
        "TotalQuestions": [
            "25", "25", "25", "25", "25",
            "25", "25", "25", "25", "25",
            "25", "25", "25", "25", "25",
            "25", "25", "25", "25", "25"
        ],
        "Score": [
            "80", "88", "92", "84", "96",
            "72", "76", "", "80", "84",
            "88", "92", "96", "100", "92",
            "76", "80", "84", "88", "92"
        ],
        "OverallGrade": [
            "", "", "", "", "",
            "", "", "", "", "",
            "", "", "", "", "",
            "", "", "", "", ""
        ]
    }

    test_data = pd.DataFrame(raw_test_data, dtype=str)


    test_data = remove_empty_col(test_data)
    test_data = remove_any_missing_row(test_data)
    average = mean_score(test_data)
    
    


    demographic_data = pd.read_csv(raw_demo_data, dtype=str)
    merged_data = merge_data(test_data, demographic_data)

if __name__ == "__main__":
    main()
