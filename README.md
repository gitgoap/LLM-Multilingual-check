# LLM-Multilingual-Check

## Project: *"How Does a Multilingual Language Model Handle Multiple Languages?"*

### Objective
Understand how multilingual models (specifically **BLOOM-1.7B**) represent and transfer knowledge across languages.


<img width="512" height="512" alt="Bloom ccreature Jul 22, 2025, 10_33_27 AM" src="https://github.com/user-attachments/assets/6dc002c3-cc97-41f7-9ab4-41dc46b2358a" />


## Task 1: Embedding Similarity

-  Making a parallel word list (500–5000 entries) in **English**, **French**, and **Portuguese** — languages supported by BLOOM.
-  **Compute cosine similarity** between word embeddings across languages to check if “meaning” aligns.

**Percentage distibution** of 3 language in Bloom 1.7B dataset [source](https://huggingface.co/bigscience/bloom-1b7):
- English: **31.3%**
- French: **13.5%**
- Portuguese: **5.2%**

### Task 1 Result
**Average Cosine Similarity:**
- English–French: **0.9365**
- French–Portuguese: **0.9349**
- Portuguese–English: **0.9153**

GPU Used for the task: `Nvidia T4` on `Google Collab`

#### Verdict: High average cosine similarity in all 3 pairs signifies that Bloom 1.7B has similar meaning for words in different language since Portuguese having only 5.2% share in total Bloom training dataset  gives similar cosine similariy of english, french pair.

---

### Task 2: Cross-Lingual Transfer (Zero-Shot Learning)

-  **Fine-tuning** BLOOM on a downstream task (e.g., **sentiment classification**) using only **English** data (High-Resource Language).
-  **Test** the model on the `SentiHin-2500` (Sentimental Analysis Hindi Dataset) in a **Low-Resource Language** (e.g., **Hindi** or **Swahili**) *without any additional training*.
- Further testing the base Bloom 1.7B on SentiHin-2500 for comparison with the result of above finetuned model.




### Task 2 Result

| Metric     | Finetuned BLOOM (`MLap/bloom1.7-lora-sentiment-analysis-classification`) | Original BLOOM (`bigscience/bloom-1b7`) |
|------------|-------------------------------------------------------------------------|------------------------------------------|
| Accuracy   | 0.3392                                                                  | 0.4628                                   |
| Precision  | 0.1131                                                                  | 0.5731                                   |
| Recall     | 0.3333                                                                  | 0.4590                                   |
| F1 Score   | 0.1689                                                                  | 0.4131                                   |

##  Goal
Check if BLOOM can generalize and transfer task knowledge across languages — a key indicator of its multilingual capabilities and usefulness in **low-resource language settings**.
Bloom chosen due to **Multilingual Pretraining**, then Finetuning.


## Dataset and Model Information

### Fine-tuned Model: [MLap/bloom1.7-lora-sentiment-analysis-classification](https://huggingface.co/MLap/bloom1.7-lora-sentiment-analysis-classification)

This model is based on BLOOM-1.7B, fine-tuned using LoRA (Low-Rank Adaptation) for sentiment classification tasks. The fine-tuned model is available on Hugging Face Hub.

### LoRA Finetuning Dataset: [Sp1786/multiclass-sentiment-analysis-dataset](https://huggingface.co/datasets/Sp1786/multiclass-sentiment-analysis-dataset)

The model was fine-tuned on this English multiclass sentiment analysis dataset before being evaluated on the Hindi dataset to assess cross-lingual transfer capabilities.

### Hindi Inference Dataset: [MLap/SentiHin-2500](https://huggingface.co/datasets/MLap/SentiHin-2500)

SentiHin-2500 is a Hindi sentiment analysis dataset containing 2,500 labeled datapoints with three classes: positive, negative, and neutral. **This dataset was specifically created for this project and is publicly available on Hugging Face.**

GPU Used for the task: `Nvidia T4 2x` on `Kaggle`




---

### Future Note
This project can be scaled to 15-20 languages in task 1 to check cross-lingual capability of multiple different LLMs.

Feel free to contribute or explore further improvements!
