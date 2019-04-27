
class SingletonMetaClass(type):
    """
    单例
    """
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._inst[cls]
