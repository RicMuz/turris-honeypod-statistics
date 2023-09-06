import pandas as pd
import researchpy as rp
import scipy.stats as stats

def main():
    df = pd.read_csv("export.csv")
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