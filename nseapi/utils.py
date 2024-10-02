
def generate_docstring(cmd: str="", spec:dict = {}, desc: str = ""):
    """Generate help text for the command."""

    def _key(key, spec, space=2):
        _str = f"{' ' * space}{key} ({spec['type'].__name__}, {'required' if spec['required'] else 'optional'})"
        if 'help_text' in spec:
            _str += f": {spec['help_text']}"
        
        return _str



    if 'attributes' in spec:
        desc += "\nAttributes:\n"
        desc += "\n".join([_key(k,s) for k, s in spec['attributes'].items()])
        # for key, spec in spec['attributes'].items():
        #     if key == 'COMMAND':
        #         continue
        #     desc += f"  {key}: "
        #     if 'help_text' in spec:
        #         desc += f"{spec['help_text']}\n"
        #     else:
        #         desc += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
    if 'elements' in spec:
        desc += "\nElements:\n"
        desc += "\n".join([_key(k,s) for k, s in spec['elements'].items()])
        # for key, spec in spec['elements'].items():
        #     desc += f"  {key}: "
        #     if 'help_text' in spec:
        #         desc += f"{spec['help_text']}\n"
        #     else:
        #         desc += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
    
    return desc