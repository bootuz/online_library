

def replacer(string, char='ӏ', to_be_replaced='iIlL1|'):
    for i in to_be_replaced:
        if string.startswith(i):
            string = string.replace(i, 'Ӏ')
        if i in string:
            string = string.replace(i, char)
    return string


def rename_and_path(instance, filename):
    slug = instance.slug.replace("-", "_")
    file_slug_name = filename.split(".")
    file_slug_name[0] = slug
    return 'books/{}/{}'.format(slug, ".".join(file_slug_name))
