def stylish(diff, depth=1):
    indent = "    " * depth
    lines = ["{"]

    for key in sorted(diff.keys()):
        node = diff[key]
        status = node["status"]

        if status == "added":
            lines.append(f"{indent[:-2]}+ {key}: {format_value(node['value'], depth)}")
        elif status == "removed":
            lines.append(f"{indent[:-2]}- {key}: {format_value(node['value'], depth)}")
        elif status == "unchanged":
            lines.append(f"{indent}{key}: {format_value(node['value'], depth)}")
        elif status == "changed":
            lines.append(f"{indent[:-2]}- {key}: {format_value(node['old_value'], depth)}")
            lines.append(f"{indent[:-2]}+ {key}: {format_value(node['new_value'], depth)}")
        elif status == "nested":
            nested_value = stylish(node["value"], depth + 1)
            lines.append(f"{indent}{key}: {nested_value}")

    lines.append("    " * (depth - 1) + "}")
    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for k in sorted(value.keys()):
            lines.append(f"{' ' * (depth + 1)}{k}: {format_value(value[k], depth + 1)}")
        lines.append(f"{' ' * depth}" + "}")
        return "\n".join(lines)


    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
