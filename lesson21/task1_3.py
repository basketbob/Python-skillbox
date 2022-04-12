def search_elemente(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    for v in dictionary.values():
        if isinstance(v, dict):
            result = search_elemente(v, key)
            if result:
                break
    else:
        result = None

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

a = search_elemente(site, 'div')
print(a)
