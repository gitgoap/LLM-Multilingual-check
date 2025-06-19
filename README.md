# LLM-Multilingual-Check

## Project: *"How Does a Multilingual Language Model Handle Multiple Languages?"*

### Objective
Understand how multilingual models (specifically **BLOOM-1.7B**) represent and transfer knowledge across languages.

---

## Task 1: Embedding Similarity

-  Making a parallel word list (500–5000 entries) in **English**, **French**, and **Portuguese** — languages supported by BLOOM.
-  **Compute cosine similarity** between word embeddings across languages to check if “meaning” aligns.

**Percentage distibution** of 3 language in Bloom 1.7B dataset (source)[https://huggingface.co/bigscience/bloom-1b7]:
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

##  Task 2: Cross-Lingual Transfer (Zero-Shot Learning)

-  **Fine-tuning** BLOOM on a downstream task (e.g., **sentiment classification**) using only **English** data (High-Resource Language).
-  **Test** the model on the same task in a **Low-Resource Language** (e.g., **Hindi** or **Swahili**) *without any additional training*.

###  Goal
Check if BLOOM can generalize and transfer task knowledge across languages — a key indicator of its multilingual capabilities and usefulness in **low-resource language settings**.

Bloom chosen due to **Multilingual Pretraining**, then Finetuning.

---

### Future Note
This project can be scaled to 15-20 languages in task 1 using 7-10 different LLMs.

Feel free to contribute or explore further improvements!
