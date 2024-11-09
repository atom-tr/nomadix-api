def generate_docstring(spec: dict = {}, desc: str = ""):
    """Generate help text for the command."""

    def _key(key, spec, space=2):
        _str = f"{' ' * space}{key} ({spec['type'].__name__}, {'required' if spec['required'] else 'optional'})"
        if "help_text" in spec:
            _str += f": {spec['help_text']}"

        return _str

    if "attributes" in spec:
        desc += "\nAttributes:\n"
        for k, s in spec["attributes"].items():
            if "value" in s:
                desc += f"\n{k} = {s['value']}"
            else:
                desc += "\n" + _key(k, s)

    if "elements" in spec:
        desc += "\nElements:\n"
        desc += "\n".join([_key(k, s) for k, s in spec["elements"].items()])

    return desc
