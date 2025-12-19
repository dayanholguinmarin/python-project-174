"""def _to_str(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def _format_literal_dict(dct, depth):
    indent = "    " * depth
    lines = ["{"]
    for k in sorted(dct.keys()):
        v = dct[k]
        if isinstance(v, dict):
            inner = _format_literal_dict(v, depth + 1)
            lines.append(f"{'    ' * (depth + 1)}{k}: {inner}")
        else:
            lines.append(f"{'    ' * (depth + 1)}{k}: {_to_str(v)}")
    lines.append(f"{indent}" + "}")
    return "\n".join(lines)


def stylish(diff, depth=1):

    def _iter_nodes(node, depth):
        lines = []
        base_indent = "   " * depth

        for key in sorted(node.keys()):
            info = node[key]
            status = info.get("status")

            if status == "nested":
                lines.append(f"{base_indent}{key}: {{")
                lines.extend(_iter_nodes(info["value"], depth + 1))
                lines.append(f"{base_indent}}}")
            elif status == "unchanged":
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth + 1)
                    lines.append(f"{base_indent}{key}: {formatted}")
                else:
                    lines.append(f"{base_indent}{key}: {_to_str(val)}")
            elif status == "added":
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth + 1)
                    lines.append(f"{base_indent[:-2]}+ {key}: {formatted}")
                else:
                    lines.append(f"{base_indent[:-2]}+ {key}: {_to_str(val)}")
            elif status == "removed":
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth + 1)
                    lines.append(f"{base_indent[:-2]}- {key}: {formatted}")
                else:
                    lines.append(f"{base_indent[:-2]}- {key}: {_to_str(val)}")
            elif status == "changed":
                old = info.get("old_value")
                new = info.get("new_value")
                if isinstance(old, dict):
                    formatted_old = _format_literal_dict(old, depth + 1)
                    lines.append(f"{base_indent[:-2]}- {key}: {formatted_old}")
                else:
                    lines.append(f"{base_indent[:-2]}- {key}: {_to_str(old)}")
                if isinstance(new, dict):
                    formatted_new = _format_literal_dict(new, depth + 1)
                    lines.append(f"{base_indent[:-2]}+ {key}: {formatted_new}")
                else:
                    lines.append(f"{base_indent[:-2]}+ {key}: {_to_str(new)}")
            else:
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth + 1)
                    lines.append(f"{base_indent}{key}: {formatted}")
                else:
                    lines.append(f"{base_indent}{key}: {_to_str(val)}")

        return lines

    lines = ["{"]
    lines.extend(_iter_nodes(diff, depth))
    lines.append("}")
    return "\n".join(lines)"""




def stylish(diff, depth=1):
    indent_size = depth * 4
    indent = ' ' * (indent_size - 2)
    closing_indent = ' ' * ((depth - 1) * 4)
    lines = []
    print(depth, diff)
    for item in diff:
        key = item['key']
        type_ = item['type']

        if type_ == 'added':
            lines.append(f"{indent}+ {key}: {to_str(item['value'], depth)}")
        elif type_ == 'removed':
            lines.append(f"{indent}- {key}: {to_str(item['value'], depth)}")
        elif type_ == 'unchanged':
            lines.append(f"{indent}  {key}: {to_str(item['value'], depth)}")
        elif type_ == 'changed':
            lines.append(f"{indent}- {key}: {to_str(item['old_value'], depth)}")
            lines.append(f"{indent}+ {key}: {to_str(item['new_value'], depth)}")
        elif type_ == 'nested':
            children = stylish(item['children'], depth + 1)
            lines.append(f"{indent}  {key}: {children}")

    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def to_str(value, depth):
    if isinstance(value, dict):
        inner_indent_size = depth * 4 + 4
        inner_indent = ' ' * inner_indent_size
        closing_indent = ' ' * (depth * 4)
        lines = [
            f"{inner_indent}{k}: {to_str(v, depth + 1)}"
            for k, v in value.items()
        ]
        return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"

    if isinstance(value, bool):
        return str(value).lower()  # True -> 'true', False -> 'false'

    if value is None:
        return "null"

    return str(value)