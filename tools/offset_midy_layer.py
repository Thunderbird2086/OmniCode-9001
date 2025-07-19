import csv
import argparse

def process_cpl(input_file, filter_value, offset, new_layer, output_file):
    with open(input_file, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        header = reader[0]
        val_idx = header.index("Val")
        midy_idx = header.index("Mid Y")
        layer_idx = header.index("Layer")

        processed_rows = []
        for row in reader[1:]:
            if row[val_idx] == filter_value:
                row[midy_idx] = str(float(row[midy_idx]) + offset)
                row[layer_idx] = new_layer
            processed_rows.append(row)

    with open(output_file, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(processed_rows)
    print(f"Filtered, offset, and layer-changed file saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Offset Mid Y and change Layer for filtered Val in CPL-GlyphMatrix.csv")
    parser.add_argument("--filter_value", required=True, help="Value to filter by (e.g., '100nF')")
    parser.add_argument("--offset", type=float, required=True, help="Offset to add to Mid Y")
    parser.add_argument("--new_layer", required=True, help="New layer value (e.g., 'top', 'bottom')")
    parser.add_argument("--input_file", default="CPL-GlyphMatrix.csv", help="Input CSV file name")
    args = parser.parse_args()

    output_file = f"CPL-GlyphMatrix_{args.filter_value}_offset_{args.offset}_layer_{args.new_layer}.csv"
    process_cpl(args.input_file, args.filter_value, args.offset, args.new_layer, output_file)

if __name__ == "__main__":
    main()
