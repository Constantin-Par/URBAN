def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for ow in other_words:
        ow_lower = ow.lower()
        if root_word_lower.find(ow_lower) != -1 or ow_lower.find(root_word_lower) != -1:
            same_words.append(ow)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
