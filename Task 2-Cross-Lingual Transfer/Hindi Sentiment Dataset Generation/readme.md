The csv dataset is generated using OpenAI's GPT4o and Claude 4 Sonnet with the below **prompt**.

`count_duplicate.py` script count duplicate rows in the csv.

`remove_duplicate` script deletes duplicate rows and saves it in a new csv file.

All the 2500 rows of this CSV dataset is manually verified for correctness.

> Prompt given to GPT4o for Hindi Sentiment dataset generation.
```
Generate a dataset of 250 unique examples of Hindi sentences labeled with sentiment.  

Instructions:
- Each example must be a single line CSV, in the format:
  
  Sentence,sentiment_label

- The sentence must be in Hindi language.
- The sentiment label must be one of:
  - positive
  - negative
  - neutral
- Make sure:
  - The sentences are grammatically correct.
  - The sentences vary in length and style (short, medium, long).
  - Avoid repetition; each sentence should be unique.
  - Sentences should cover diverse topics: movies, products, experiences, services, decisions, travel, etc.
  - No headers in output.
  - No quotes or escaping characters.
  - Output only the data, no explanations or extra text.

Example Output Format:
यह फिल्म बहुत अच्छी थी।,positive
मुझे यह अनुभव निराशाजनक लगा।,negative
इस विषय पर मेरी कोई खास राय नहीं है।,neutral
```

