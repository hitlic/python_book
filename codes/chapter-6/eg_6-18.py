def class_dec3(class_deced):
    class Inner:
        def __init__(self, *args, **kwargs):
            self.class_obj = class_deced(*args, **kwargs)

        def __getattr__(self, prop_name):
            return getattr(self.class_obj, prop_name)
    return Inner
