import pandas as pd
import researchpy as rp
import scipy.stats as stats

def main():
    df = pd.read_csv("export.csv")
    """
    print(rp.summary_cat(df[["country","password"]]))
    print("==================================================")
    crosstab = pd.crosstab(df["country"], df["password"])
    print(crosstab)
    print("==================================================")
    print(stats.chi2_contingency(crosstab))
    print("==================================================")
    """

    '''
    print(rp.summary_cat(df["password"]))
    print(df["password"].mode()[0])
    print("==================================================")
    crosstab,test_result,expected=rp.crosstab(df["country"],df["password"],test="chi-square",expected_freqs=True,prop="cell")
    new_crosstab = crosstab["0"]
    print(new_crosstab)
    print("==================================================")
    print(test_result)
    print("==================================================")
    print(expected)
    '''

    """
    # Filter just the most used username
    new_df = df[df["user_name"] == df["user_name"].mode()[0]]
    print(new_df)
    print("==================================================")
    print(rp.crosstab(new_df["country"], new_df["user_name"]))

    crosstab, test_result, expected = rp.crosstab(new_df["country"],new_df["user_name"],
                                                  test="chi-square",
                                                  expected_freqs=True,
                                                  prop="cell")
    
    print(crosstab)
    print("==================================================")
    print(test_result)
    print("==================================================")
    print(expected)
    """
    df["most_common_user_name"] = (df["user_name"] == df["user_name"].mode()[0]).astype(int)
    print(rp.crosstab(df["country"], df["most_common_user_name"]))
    print("==================================================")
    print(stats.chi2_contingency(rp.crosstab(df["country"],df["most_common_user_name"])))
    print("==================================================")

    crosstab, test_result, expected = rp.crosstab(df["country"],df["most_common_user_name"],
                                                  test="chi-square",
                                                  expected_freqs=True,
                                                  prop="cell")
    print(crosstab)
    print("==================================================")
    print(test_result)
    print("==================================================")
    print(expected)


if __name__ == "__main__":
    main()