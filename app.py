import pandas as pd
from dash import Dash, html, dcc
from plotly.express import line

#Prepare data
data = pd.read_csv("data/processed_sales_data.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values("date")

#Split data
data_before = data[data["date"] <= "2021-01-15"]
data_after = data[data["date"] > "2021-01-15"]

#Create before and after
line_before = line(data_before, x="date", y="sales")
line_before.update_traces(line_color="blue", name="Before Price Increase")
line_after = line(data_after, x="date", y="sales")
line_after.update_traces(line_color="red", name="After Price Increase")

#Combine
comb_line = line_before
comb_line.add_traces(line_after.data)

#Graph labels
comb_line.update_layout(
    title="Sales Over Time",
    xaxis_title="Date",
    yaxis_title="Sales"
)

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=comb_line)
])
if __name__ == "__main__":
    app.run(debug=True)