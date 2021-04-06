import unittest
import sys
import pandas as pd
import pathlib

class knownlengths(unittest.TestCase):
    def test_length_arguments(self):
        result = len(sys.argv)
        if result == 1:
            print("Error: There are no csv files give in the Command line")
        elif result == 2:
            if(pathlib.Path(sys.argv[1]).suffix!='.csv'):
                print("Error: Incorrect File Format - The input should be a minimum of 2 csv files")
            else:
                print("Error: Cannot merge as input should be a minimum of 2 csv files")
        else:
            extenfile = sys.argv[1:]
            start = True
            length = len(extenfile)
            for i in range(length):
                if (pathlib.Path(extenfile[i]).suffix != '.csv'):
                    start = False
            if start:
                all_df = []
                for i in range(1, result):
                    #Read a CSV file to dataframe
                    df = pd.read_csv(sys.argv[i], error_bad_lines=False,)
                    # Column named 'filename' created with csv filename values
                    df['filename'] = sys.argv[i]
                    all_df.append(df)
                    # Reset the index value
                merged_df = pd.concat(all_df, ignore_index=True)
                    #Remove extra columns
                merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]
                    #Convert dataframe to CSV
                merged_df = merged_df.to_csv()
                print(merged_df)
            else:
                print("Error: Incorrect File Format - The input should be csv files")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


