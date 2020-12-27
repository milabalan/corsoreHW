
# 2.* Create metaclass with inheritance\
MetaClass = type("MetaClass", (), {"is_meta_class": True})
SubMetaClass = type("SubMetaClass", (MetaClass,), {})

class SampleClass(SubMetaClass):
    pass

x = SampleClass()
print(x.is_meta_class)
