"""辅助函数，主要与模板模式有关"""

import inspect

from typing import Union, Type
from typing import List, Dict, Any

JsonExportable = Union[int, float, bool, str, List["JsonExportable"], Dict[str, "JsonExportable"]]

def provide_ctor_defaults(cls: Type) -> Dict[str, Any]:
    """为构造函数提供默认值，以绕开构造函数的参数限制"""

    signature = inspect.signature(cls.__init__)
    provided_defaults: Dict[str, Any] = {}

    for name, param in signature.parameters.items():
        if name == 'self': continue
        if param.default is not inspect.Parameter.empty: continue

        if param.annotation is int or param.annotation is float:
            provided_defaults[name] = 0
        elif param.annotation is str:
            provided_defaults[name] = ""
        elif param.annotation is bool:
            provided_defaults[name] = False
        else:
            raise ValueError(f"Unsupported parameter type: {param.annotation}")

    return provided_defaults

def assign_attr_with_json(obj: object, attrs: List[str], json_data: Dict[str, Any]):
    """根据json数据赋值给指定的对象属性

    若有复杂类型，则尝试调用其`import_json`方法进行构造
    """
    type_hints: Dict[str, Type] = {}
    for cls in obj.__class__.__mro__:
        if '__annotations__' in cls.__dict__:
            type_hints.update(cls.__annotations__)

    for attr in attrs:
        if hasattr(type_hints[attr], 'import_json'):
            obj.__setattr__(attr, type_hints[attr].import_json(json_data[attr]))
        else:
            obj.__setattr__(attr, type_hints[attr](json_data[attr]))

def export_attr_to_json(obj: object, attrs: List[str]) -> Dict[str, JsonExportable]:
    """将对象属性导出为json数据

    若有复杂类型，则尝试调用其`export_json`方法进行导出
    """
    json_data: Dict[str, Any] = {}
    for attr in attrs:
        if hasattr(getattr(obj, attr), 'export_json'):
            json_data[attr] = getattr(obj, attr).export_json()
        else:
            json_data[attr] = getattr(obj, attr)
    return json_data
