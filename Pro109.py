import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv("Pro109Data.csv")
lst = df["math score"].tolist()
#Calculating the mean and the standard deviation
mean = sum(lst) / len(lst)
std_deviation = statistics.stdev(lst)
median = statistics.median(lst)
mode = statistics.mode(lst)


print("Mean, Median and Mode of math is {}, {} and {} respectively".format(mean,median,mode))



math_first_std_deviation_start, math_first_std_deviation_end = mean-std_deviation, mean+std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

lst_of_data_within_1_std_deviation = [result for result in lst if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
lst_of_data_within_2_std_deviation = [result for result in lst if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
lst_of_data_within_3_std_deviation = [result for result in lst if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

print("{}% of data for math score lies within 1 standard deviation".format(len(lst_of_data_within_1_std_deviation)*100.0/len(lst)))
print("{}% of data for math score lies within 2 standard deviations".format(len(lst_of_data_within_2_std_deviation)*100.0/len(lst)))
print("{}% of data for math score lies within 3 standard deviations".format(len(lst_of_data_within_3_std_deviation)*100.0/len(lst)))

fig = ff.create_distplot([lst], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[math_first_std_deviation_start, math_first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[math_first_std_deviation_end, math_first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[math_second_std_deviation_start, math_second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.add_trace(go.Scatter(x=[math_second_std_deviation_end, math_second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()
