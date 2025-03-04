def check_sensitive_words(text, sensitive_words):
    text = text.lower()  # 将文本转换为小写  
    for word in sensitive_words:
        if word in text and word != '':  # 检查不区分大小写的敏感词
            print("Error: Sensitive word found:", word)
            return 'true'  # 找到敏感词后返回true  
    return 'false'  # 如果没有找到敏感词，循环结束后返回false  


# 读取敏感词列表（这里假设敏感词列表在sensitive_words.txt文件中）
with open('static/sensitive_words/words.txt', 'r', encoding='utf-8') as f:
    sensitive_words = [line.strip().lower() for line in f]  # 读取时转换为小写  

# 测试文本  
test_text = "你去死吧"

# 检测敏感词  
result = check_sensitive_words(test_text, sensitive_words)
if result == 'true':
    print('有')
else:
    print('没有')
