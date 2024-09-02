def repl_chars(string, chars, new_char):
    for char in chars:
        string = string.replace(char, new_char)
    return string


class WordsFinder:

    def __init__(self, cp, *files_names):
        self.cp = cp
        self.files_list = []
        for file_name in files_names:
            self.files_list.append(file_name)

    def get_all_words(self):
        all_words = {}
        OLD_DELIMS = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.files_list:
            with open(file_name,
                      encoding=self.cp) as file:  # encoding='1252' - только для примера с несколькими файлами
                all_lines = ''
                for line in file:
                    all_lines = all_lines + " " + repl_chars(line.lower(), OLD_DELIMS, ' ')
                all_words[file_name] = all_lines.split()
        return all_words

    def find(self, word_to_find):
        founded = {}
        for name, words in self.get_all_words().items():
            pos = 1
            for word in words:
                if word.lower() == word_to_find.lower():
                    founded[name] = pos
                    break
                pos += 1
        return founded

    def count(self, word_to_find):
        counted = {}
        for name, words in self.get_all_words().items():
            count = 0
            for word in words:
                if word.lower() == word_to_find.lower():
                    count += 1
            if count > 0:
                counted[name] = count
        return counted


finder2 = WordsFinder('1251', 'test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print('------------------')

finder1 = WordsFinder('1252', 'Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
