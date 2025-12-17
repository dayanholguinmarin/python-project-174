def plain(diff):
    lines = []

    def walk(node, path=""):
        for key in sorted(node.keys()):
            item = node[key]
            status = item.get("status")
            prop = f"{path}.{key}" if path else key

            if status == "nested":
                walk(item["value"], prop)
            elif status == "added":
                val = format_value_plain(item["value"])
                lines.append(f"Property '{prop}' was added with value: {val}")
            elif status == "removed":
                lines.append(f"Property '{prop}' was removed")
            elif status == "changed":
                old = format_value_plain(item["old_value"])
                new = format_value_plain(item["new_value"])
                lines.append(f"Property '{prop}' was updated. From {old} to {new}")

    walk(diff)

    if not lines:
        return ""
    return "\n" + "\n".join(f"    {ln}" for ln in lines)


def format_value_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
