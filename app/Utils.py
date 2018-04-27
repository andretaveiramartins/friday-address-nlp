import os
import json
import yaml

def load_json_from_file(fileName):
    """The filename arg can be either the filename or the relative path with the filename appended
    """
    template_full_path = os.path.join(os.path.dirname(__file__), fileName)
    json_template = None
    with open(template_full_path, 'r') as json_data:
        json_template = json.load(json_data)
        json_data.close()
    return json_template
    
def load_yml_config(fileName):
    """The filename arg can be either the filename or the relative path with the filename appended
    """
    template_full_path = os.path.join(os.path.dirname(__file__), fileName)
    config = None
    with open(template_full_path, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return config