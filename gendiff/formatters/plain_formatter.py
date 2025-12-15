def plain(diff, path=""):
    lines = []

    for key, node in diff.items():
        full_path = f"{path}.{key}" if path else key 
        status = node["status"]

        if status == "nested":
            lines.extend(plain(node["value"], full_path))
        elif status == "added":
            value = format_value(node["value"])
            lines.append(f"Property '{full_path}' was added with value: {value}")
        elif status == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif status == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{full_path}' was updated. From {old_value} to {new_value}"
            )

    return "\n".join(lines)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
