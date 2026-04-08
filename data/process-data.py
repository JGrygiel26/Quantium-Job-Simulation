import csv
import os

#Set up all file locations and groups up the input files into one
base_dir = os.path.dirname(__file__)
input_files = [os.path.join(base_dir, "daily_sales_data_0.csv"), os.path.join(base_dir, "daily_sales_data_1.csv"), os.path.join(base_dir, "daily_sales_data_2.csv")]
output_file = os.path.join(base_dir, "processed_sales_data.csv")

new_rows = []

#iterate over each csv file
for infile in input_files:
    #DictReader as in documentation
    with open(infile, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Skip non pink morsels
            if row["product"] != "pink morsel":
                continue
            #Creates sales column
            price = float(row["price"].replace("$", ""))
            quantity = int(row["quantity"])
            sales = price * quantity
            #Add read data into new_rows
            new_rows.append({
                "date": row["date"],
                "region": row["region"],
                "sales": sales
            })

#DictWriter as in documentation
with open(output_file, mode="w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["date", "region", "sales"])
    writer.writeheader()
    writer.writerows(new_rows)