class MyClass:
    my_attr = 2


def introspection_info(obj):
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_info = {
        'type': type(obj),
        'attributes': attributes,
        'methods': methods,
        'module': obj.__module__ if callable(obj) else type(obj).__module__,
    }
    return obj_info


if __name__ == '__main__':
    obj = 42
    info = introspection_info(obj)
    print('Объект:', obj)
    print(info['type'])
    print(info['attributes'])
    print(info['methods'])
    print(info['module'])
    print()

    obj = introspection_info
    info = introspection_info(obj)
    print('Объект:', obj)
    print(info['type'])
    print(info['attributes'])
    print(info['methods'])
    print(info['module'])
    print()

    obj = MyClass
    info = introspection_info(obj)
    print('Объект:', obj)
    print(info['type'])
    print(info['attributes'])
    print(info['methods'])
    print(info['module'])
