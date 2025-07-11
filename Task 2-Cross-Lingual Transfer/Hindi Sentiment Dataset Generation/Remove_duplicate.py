import csv
input_path = 'C:/Users/aman/Desktop/LLM project/Hindi Sentiment Dataset/hindi_sentiment_analysis.csv'
output_path = 'C:/Users/aman/Desktop/LLM project/Hindi Sentiment Dataset/hindi_sentiment_analysis_dedup.csv'

with open(input_path, 'r', newline='', encoding='utf-8') as csvfile:
    rows = list(csv.reader(csvfile))

# Remove duplicates while preserving order
seen = set()
dedup_rows = []
for row in rows:
    row_tuple = tuple(row)  # lists are unhashable, so convert to tuple
    if row_tuple not in seen:
        seen.add(row_tuple)
        dedup_rows.append(row)

# Write the deduplicated rows to a new CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dedup_rows)

print(f"Original rows: {len(rows)}")
print(f"Rows after removing duplicates: {len(dedup_rows)}")
