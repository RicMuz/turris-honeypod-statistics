import pandas as pd
import researchpy as rp
import scipy.stats as stats

def main():
    # load the data
    data_frame = pd.read_csv("export.csv")

    # find the most used user name:
    most_common_user_name = data_frame["user_name"].mode()[0]

    # create bit map of the most common user name (true if the most common user name was used on that line)
    data_frame["most_common_user_name"] = (data_frame["user_name"] == most_common_user_name).astype(bool)

    # count how many times was it used or was not for each country 
    print(rp.crosstab(data_frame["country"], data_frame["most_common_user_name"]))

    print("==================================================")

    # print result of chi2 test (lib scipy.stats) -> worse formatting, but includes degrees of freedom
    print(stats.chi2_contingency(rp.crosstab(data_frame["country"], data_frame["most_common_user_name"])))

    print("==================================================")

    # get the results from researchpy
    crosstab, test_result, expected = rp.crosstab(data_frame["country"],
                                                  data_frame["most_common_user_name"],
                                                  test="chi-square",
                                                  expected_freqs=True,
                                                  prop="cell")
    
    # percentage of the cell to whole 
    print(crosstab)

    print("==================================================")

    # results of the chi2 test
    print(test_result)

    print("==================================================")

    # expected count for each cell
    print(expected)


if __name__ == "__main__":
    main()