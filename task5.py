from json import loads

def remove(d: dict):
    result = {}
    for k, v in d.items():
        if v:
            if isinstance(v, dict):
                result[k] = remove(v);
            elif isinstance(v, list):
                result[k] = list(filter(None, [remove(i) if isinstance(i, dict) else i for i in v]))
            else:
                result[k] = v
    return result if result else None

def main():
    json_raw = input()
    json_obj = loads(json_raw)
    print(remove(json_obj))

main()