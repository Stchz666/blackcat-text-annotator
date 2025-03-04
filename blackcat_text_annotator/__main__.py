from blackcat_text_annotator.language_labeler import LanguageLabeler

def main():
    lang_labeler = LanguageLabeler()

    lang_samples = [
        "Python and Java are popular languages",
        "I prefer C++ over C",
        "Golang is also called Go",
        "Ruby on Rails framework"
    ]

    print("===== 语言标注结果 =====")
    for i, text in enumerate(lang_samples):
        results = lang_labeler.label([text])
        print(f"文本{i+1}: {text} → {results[0]}")

if __name__ == '__main__':
    main()



