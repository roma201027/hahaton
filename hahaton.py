departments = {
    'продажу': {
        'співробітники': ['Федорчук', 'Григоренко'],
        'менеджер': 'Григоренко',
        'завідувач': 'Федорчук'
    },
    'розробка': {
        'співробітники': ['Василенко', 'Валько', 'Бондаренко'],
        'менеджер': 'Валько',
        'завідувач': 'Бондаренко'
    }
}

print("Завідуючі відділів:")
for department in departments:
    print("-", departments[department]["завідувач"])
print("Проектні менеджери відділів:")
for department in departments:
    print("-", departments[department]["менеджер"])
