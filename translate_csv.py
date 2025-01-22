import openai
import pandas as pd

# Đặt API key của bạn từ GitHub Secrets
import os
openai.api_key = os.getenv("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")

def translate_text(text, target_language="es"):
    """
    Hàm dịch nội dung text sang ngôn ngữ đích sử dụng OpenAI API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Dịch đoạn văn sau sang tiếng {target_language}:"},
                {"role": "user", "content": text}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return text  # Trả về văn bản gốc nếu lỗi xảy ra

def translate_csv(input_file, output_file, target_language="es"):
    """
    Hàm dịch toàn bộ file CSV sang ngôn ngữ đích.
    """
    # Đọc file CSV
    df = pd.read_csv(input_file)

    # Tạo danh sách chứa nội dung đã dịch
    translated_html = []

    # Duyệt qua từng hàng và dịch nội dung cột cần thiết
    for html in df['NEEDED CHECK']:
        translated_text = translate_text(html, target_language=target_language)
        translated_html.append(translated_text)

    # Thêm cột đã dịch vào DataFrame
    df['Translated'] = translated_html

    # Ghi ra file mới
    df.to_csv(output_file, index=False)
    print(f"Translation completed. Translated file saved to {output_file}")

# Chạy chương trình
if __name__ == "__main__":
    input_file = "english.csv"  # Tên file CSV đầu vào
    output_file = "spanish_translated.csv"  # Tên file CSV đầu ra
    target_language = "es"  # Ngôn ngữ đích (es = tiếng Tây Ban Nha)
    translate_csv(input_file, output_file, target_language)

