from scipy import stats


df_anova = [[1,2,3],[3,5,4],[7,6,5]]


F, p = stats.f_oneway(df_anova[0],df_anova[1],df_anova[2])
print("F-value for significance is: ", F)
if p < 0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")