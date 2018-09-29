from llvmlite import ir, binding


def unwrap(obj):
    return obj.attr['native']


class ILObject:

    def __init__(self):
        self.attr = {"to_string": self.to_string}

    def to_string(self):
        str(self)


class LLVMModuleObject(ILObject):

    def __init__(self, name):
        super().__init__()
        self.attr['native'] = ir.Module(name=name)

    def to_string(self):
        str(self.attr.get('native'))


class LLVMFunctionObject(ILObject):

    def __init__(self, native_module, native_func_type, name):
        super().__init__()
        self.attr['native'] = ir.Function(native_module, native_func_type, name=name)


class LLVMFunctionTypeObject(ILObject):

    def __init__(self, native_func_type):
        super().__init__()
        self.attr['native'] = native_func_type


class LLVMTypeObject(ILObject):

    is_llvm_type = True

    def to_function_type(self):
        # TODO: add args
        return LLVMFunctionTypeObject(ir.FunctionType(unwrap(self), [], False))


class LLVMVoidObject(LLVMTypeObject):

    def __init__(self):
        super().__init__()
        self.attr['native'] = ir.VoidType()
