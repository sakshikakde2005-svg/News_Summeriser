import heapq
from utils import clean_text, tokenize_words, tokenize_sentences

def calculate_word_frequency(words):
    """
    Calculate frequency of each word
    """
    freq_table = {}

    for word in words:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table


def normalize_frequency(freq_table):
    """
    Normalize frequency values
    """
    max_freq = max(freq_table.values())

    for word in freq_table:
        freq_table[word] = freq_table[word] / max_freq

    return freq_table


def score_sentences(sentences, freq_table):
    """
    Score sentences based on word frequency
    """
    sentence_scores = {}

    for sentence in sentences:
        words = sentence.lower().split()

        for word in words:
            if word in freq_table:

                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_table[word]
                else:
                    sentence_scores[sentence] += freq_table[word]

    return sentence_scores


def generate_summary(text, num_sentences=3):
    """
    Generate summary from text
    """

    cleaned = clean_text(text)

    words = tokenize_words(cleaned)

    sentences = tokenize_sentences(text)

    freq_table = calculate_word_frequency(words)

    freq_table = normalize_frequency(freq_table)

    sentence_scores = score_sentences(sentences, freq_table)

    summary_sentences = heapq.nlargest(
        num_sentences,
        sentence_scores,
        key=sentence_scores.get
    )

    summary = " ".join(summary_sentences)

    return summary