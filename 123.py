def check_sensitive_words(text, sensitive_words):
    text = text.lower()
    for word in sensitive_words:
        if word in text and word != '':
            print("Error: Sensitive word found:", word)
            return 'true'
    return 'false'


# sensitive_words.txt）
with open('static/sensitive_words/words.txt', 'r', encoding='utf-8') as f:
    sensitive_words = [line.strip().lower() for line in f]


test_text = "badword1"


result = check_sensitive_words(test_text, sensitive_words)
if result == 'true':
    print('yes')
else:
    print('no')
