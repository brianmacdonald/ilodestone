from .ast import *


class LLVMTypes:

    @staticmethod
    def create_void_type():
        LLVMVoidObject()


class LLVMFunction:

    @staticmethod
    def create_function(module, func_type, name):
        # validate
        if isinstance(module, LLVMModuleObject) and isinstance(func_type, LLVMFunctionTypeObject):
            return LLVMFunctionObject(module, func_type, name)

    @staticmethod
    def create_function_type(llvm_type):
        if llvm_type.is_llvm_type:
            return llvm_type.to_function_type()


class LLVMModule:

    @staticmethod
    def create_module(name):
        return LLVMModuleObject(name)


class Builtins:

    @property
    def methods(self):
        return {
            "println": print,
            "llvm_create_void_type": LLVMTypes.create_void_type,
            "llvm_create_function_type": LLVMFunction.create_function_type
        }