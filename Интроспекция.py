def introspection_info(obj):
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_info = {
        'type': type(obj),
        'attributes': attributes,
        'methods': methods,
        'module': type(obj).__module__,
    }
    return obj_info


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info['type'])
    print(number_info['attributes'])
    print(number_info['methods'])
    print(number_info['module'])
