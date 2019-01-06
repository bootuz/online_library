

def replacer(string, char='ӏ', to_be_replaced='iIlL1|'):
    for i in to_be_replaced:
        if string.startswith(i):
            string = string.replace(i, 'Ӏ')
        if i in string:
            string = string.replace(i, char)
    return string


def rename_and_path(instance, filename):
    return f'books/{instance.slug.replace("-", "_")}/{filename}'
