def plain(diff, path=""):
    lines = []

    for key, node in diff.items():
        status = node["status"]
        property_path = f"{path}{key}"

        if status == "nested":
            nested_lines = plain(node["value"], property_path + ".")
            if nested_lines:
                lines.append(nested_lines)
        elif status == "added":
            value = format_value(node["value"])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif status == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif status == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{property_path}' was updated. From {old_value} to {new_value}"
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
