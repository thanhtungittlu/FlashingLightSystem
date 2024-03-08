class ClassEnumBase:
    @classmethod
    def all_value(cls):
        obj = cls()
        return [getattr(obj, attr) for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
