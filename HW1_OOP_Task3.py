
# 2.* Create metaclass with inheritance\
MetaClass = type("MetaClass", (), {"is_meta_class": True, 'level': 15})
SubMetaClass = type("SubMetaClass", (MetaClass,), {})


class SampleClass(SubMetaClass):
    pass

#Create list of class
list_class=[]
x=0
for i in range(5):
    x+=1
    SubClass=type("Class{}".format(x), (MetaClass,), {'level': x})
    list_class.append(SubClass)

# call examples
x = list_class[1]
print(x.level)
print(SubMetaClass)
print(list_class)

