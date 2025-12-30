def _to_str(value):
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
        base_indent = "    " * depth

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
                    formatted = _format_literal_dict(val, depth)
                    lines.append(f"{base_indent}{key}: {formatted}")
                else:
                    str_val = _to_str(val)
                    sep = ":" if str_val == "" else ": "
                    lines.append(f"{base_indent}{key}{sep}{str_val}")
            elif status == "added":
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth)
                    lines.append(f"{base_indent[:-2]}+ {key}: {formatted}")
                else:
                    str_val = _to_str(val)
                    sep = ":" if str_val == "" else ": "
                    lines.append(f"{base_indent[:-2]}+ {key}{sep}{str_val}")
            elif status == "removed":
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth)
                    lines.append(f"{base_indent[:-2]}- {key}: {formatted}")
                else:
                    str_val = _to_str(val)
                    sep = ":" if str_val == "" else ": "
                    lines.append(f"{base_indent[:-2]}- {key}{sep}{str_val}")
            elif status == "changed":
                old = info.get("old_value")
                new = info.get("new_value")
                if isinstance(old, dict):
                    formatted_old = _format_literal_dict(old, depth)
                    lines.append(f"{base_indent[:-2]}- {key}: {formatted_old}")
                else:
                    str_old = _to_str(old)
                    sep = ":" if str_old == "" else ": "
                    lines.append(f"{base_indent[:-2]}- {key}{sep}{str_old}")
                if isinstance(new, dict):
                    formatted_new = _format_literal_dict(new, depth)
                    lines.append(f"{base_indent[:-2]}+ {key}: {formatted_new}")
                else:
                    str_new = _to_str(new)
                    sep = ":" if str_new == "" else ": "
                    lines.append(f"{base_indent[:-2]}+ {key}{sep}{str_new}")
            else:
                val = info.get("value")
                if isinstance(val, dict):
                    formatted = _format_literal_dict(val, depth)
                    lines.append(f"{base_indent}{key}: {formatted}")
                else:
                    str_val = _to_str(val)
                    sep = ":" if str_val == "" else ": "
                    lines.append(f"{base_indent}{key}{sep}{str_val}")

        return lines

    lines = ["{"]
    lines.extend(_iter_nodes(diff, depth))
    lines.append("}")
    return "\n".join(lines)
