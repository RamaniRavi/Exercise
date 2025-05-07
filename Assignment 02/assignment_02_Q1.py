import matplotlib.pyplot as plt
from collections import defaultdict

# Example documents
documents = ["data mining data analysis", "machine learning data mining", "deep learning deep thought"]

doc_freq = defaultdict(int)

for doc in documents:
    unique_terms = set(doc.lower().split())
    for term in unique_terms:
        doc_freq[term] += 1

terms = [term for term, freq in doc_freq.items()]
frequencies = [freq for term, freq in doc_freq.items()]

plt.figure(figsize=(10, 6))
plt.bar(terms, frequencies, color='skyblue')
plt.title("Document Frequencies in Corpus")
plt.xlabel("Terms")
plt.ylabel("Document Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
