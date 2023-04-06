import re


def transform(func: str, value: str, file_data: list[str]) -> list[str]:
    """
    :param func: function name
    :param value: value to be applied to func
    :param file_data: the file to which func will be applied
    :return: a list of the modified file
    """
    if func == 'filter':
        return list(filter(lambda v: value in v, file_data))

    if func == 'map':
        return list(map(lambda v: v.split()[int(value)], file_data))

    if func == 'unique':
        return list(set(file_data))

    if func == 'sort':
        if value == 'desc':
            return sorted(file_data, reverse=True)
        return sorted(file_data, reverse=False)

    if func == 'limit':
        return [i for i in list(file_data)[:int(value)]]

    if func == 'regex':
        regex = re.compile(value)
        return list(filter(lambda v: regex.findall(v), file_data))

    return []
