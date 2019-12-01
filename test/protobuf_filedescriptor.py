from google.protobuf.descriptor_pb2 import *

with open("test/ProtoTest.pb", "rb") as f:
    file_descriptor_set = FileDescriptorSet.FromString(f.read())
    # print(file_descriptor_set)
    # print("---")
    # print("---")

    for file_descriptor in file_descriptor_set.file:
        for message_desc in file_descriptor.message_type:
            print(type(message_desc))
            print(message_desc.name)
            for f in message_desc.field:
                print(f.name)
                print(FieldDescriptorProto.Label.Name(f.label))
                print(FieldDescriptorProto.Type.Name(f.type))
                print("--")

        # for enum_desc in file_descriptor.enum_type:
        #     print(type(enum_desc))
        #     print(enum_desc)
        #     print("--")
        #     print(enum_desc.name)
            
        #     for v in enum_desc.value:
        #         print(v.name, v.number)

           

