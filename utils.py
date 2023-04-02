def transform(func: str, value: str, file_data: list[str]) -> list[str]:
    if func == 'filter':
        return list(filter(lambda v: v in value, file_data))

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
