import csv
from collections import defaultdict

with open('C:/Users/aman/Desktop/LLM project/Hindi Sentiment Dataset/hindi_sentiment_analysis.csv','r',newline='', encoding='utf-8') as csvfile:
    csv_reader = list(csv.reader(csvfile))

    count = 0
    seen = set()  # Keep track of which rows have been considered duplicates
    duplicate_index = defaultdict(list)

    for i in range(len(csv_reader)):
        temp = tuple(csv_reader[i])  # make it hashable for 'seen'
        if temp in seen:
            continue  # skip rows already matched as duplicates
        for j in range(i + 1, len(csv_reader)):
            if csv_reader[j] == list(temp):
                duplicate_index[i].append(j)
                count += 1
                seen.add(tuple(csv_reader[j]))

    print("Duplicate Count:", count)
    print("Duplicate row index:", dict(duplicate_index))
