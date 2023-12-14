def two_sort(array: list) -> str:
    return '***'.join(sorted(array)[0])


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
