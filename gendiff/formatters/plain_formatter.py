def plain(diff, path=""):
    lines = []

    for key, node in diff.items():
        property_path = f"{path}{key}"
        status = node["status"]

        if status == "nested":
            # Recursividad: bajar un nivel
            lines.extend(plain(node["value"], f"{property_path}."))
        elif status == "added":
            value = format_value(node["value"]) # lo coloco aqui por que todos no usan el format_value
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
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    else:
        return str(value).lower()

