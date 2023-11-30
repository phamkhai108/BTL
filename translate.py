# from deep_translator import GoogleTranslator
# from deep_translator.exceptions importdetect

# text = input("Nhập vào đoạn văn bản: ")
# source = detect(text)

# translation = GoogleTranslator(source=source, target='en').translate(text)  

# print(f"Đoạn văn bản đã được dịch sang tiếng Anh: {translation}")

# import langid

# def detect_language(text):
#     lang, confidence = langid.classify(text)
#     return lang, confidence

# # Đoạn văn bản cần xác định ngôn ngữ
# text_to_detect = "ویکی (انگریزی: wiki) ا. tin không được xây dựng một cách tập trung theo nguyên tắc phân quyền như thường thấy ở các ứng dụng CMS hay forum mà theo nguyên tắc phân tán: ai cũng có thể chỉnh sửa, thêm mới, bổ sung thông tin lên các trang tin và khôngپنی نوعیت کی منفرد اور علمی ویب سائٹ ہوتی ہے جس کے صارفین یا زائرین ویب براؤزر یا مخصوص اطلاقیہ کی مدد سے اس کے مندرجات میں مفید اضافے اور تبدیلی کرتے ہیں۔ اس قسم کی ویب سائٹ پر لکھنے والوں کو ویکی نویس کہا جاتا ہے جو مخصوص زبان میں اس کے مضامین و مندرجات کو مرتب کر کے پیش کرتے ہیں۔ یہ مارک اپ زبان کہلاتی ہے اور بے حد س"

# # Xác định ngôn ngữ
# detected_language, confidence = detect_language(text_to_detect)

# # In kết quả
# print(f"Ngôn ngữ: {detected_language}, Độ chắc chắn: {confidence}")


import langid

def detect_language(text):
    lang, confidence = langid.classify(text)
    return lang, confidence

def detect_main_language(text):
    # Đọc nội dung từ tệp tin
    with open(text, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Chia đoạn văn thành các câu
    sentences = file_content.split('.')
    
    # Xác định ngôn ngữ của từng câu
    lang_confidence_list = [detect_language(sentence) for sentence in sentences]
    
    # Lấy ngôn ngữ xuất hiện nhiều nhất
    main_language = max(set(lang for lang, conf in lang_confidence_list), key=lang_confidence_list.count)
    
    return main_language

# Đoạn văn bản cần xác định ngôn ngữ
text_file_path = 'doan_8.txt'

# Xác định ngôn ngữ chính
main_language = detect_main_language(text_file_path)

# In kết quả
print(f"Ngôn ngữ chính: {main_language}")

