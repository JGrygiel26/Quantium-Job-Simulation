import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
from plotly.express import line

#Prepare data
data = pd.read_csv("data/processed_sales_data.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values("date")
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="header",
            children=[
                html.H1(
                    "Pink Morsels Sales Visualiser",
                    className="title"
                ),  
                dcc.RadioItems(
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    id="region-filter",
                    inline=True,
                    className="radio-items"
                ),
            ]
        ),
        dcc.Graph(id="sales-graph", className="graph")
    ]
)

#When region-filter changes, update sales-graph
@callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)

def update_graph(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"].str.lower() == selected_region]

    #Split data
    data_before = filtered_data[filtered_data["date"] <= "2021-01-15"]
    data_after = filtered_data[filtered_data["date"] > "2021-01-15"]

    #Create before and after
    line_before = line(data_before, x="date", y="sales")
    line_before.update_traces(line_color="blue", name="Before Price Increase",)
    line_after = line(data_after, x="date", y="sales")
    line_after.update_traces(line_color="red", name="After Price Increase")

    #Combine
    comb_line = line_before
    comb_line.add_traces(line_after.data)

    #Graph labels
    comb_line.update_layout(
        title={
            "text": "Sales Over Time",
            "font": {"color": "#ffffff", "size": 24}
        },
        xaxis={
            "title": {"text": "Date","font": {"size":18, "color":"#ffffff"}},
            "tickfont": {"size": 14,"color":"#ffffff"}
        },
        yaxis={
            "title": {"text": "Sales","font": {"size":18, "color":"#ffffff"}},
            "tickfont": {"size":14, "color":"#ffffff"}
        },
        plot_bgcolor="#C7C7C7",
        paper_bgcolor="#001633"
    )
    return comb_line


if __name__ == "__main__":
    app.run(debug=True)