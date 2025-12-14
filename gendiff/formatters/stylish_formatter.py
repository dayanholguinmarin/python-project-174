def stylish(diff, depth=0):
    indent = " " * (depth * 4)
    lines = ["{"]

    for key, node in diff.items():
        status = node["status"]

        if status == "nested":
            lines.append(f"{indent}    {key}: {stylish(node['value'], depth + 1)}")
        elif status == "added":
            lines.append(f"{indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif status == "removed":
            lines.append(f"{indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif status == "unchanged":
            lines.append(f"{indent}    {key}: {format_value(node['value'], depth + 1)}")
        elif status == "changed":
            old_value = node["old_value"]
            new_value = node["new_value"]
            lines.append(
                f"{indent}  - {key}: "
                f"{format_value(old_value, depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: "
                f"{format_value(new_value, depth + 1)}"
            )

    lines.append(indent + "}")
    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * ((depth) * 4)
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(indent + "}")
        return "\n".join(lines)
    return str(value)
