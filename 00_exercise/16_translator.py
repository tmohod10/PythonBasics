from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("test.txt", mode="r") as f:
        line = f.read()
        translation = translator.translate(line)
        with open("test-output.txt", mode="w") as wr:
            wr.write(translation)
except FileNotFoundError as e:
    print("File not found")
