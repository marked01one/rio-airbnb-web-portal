import dash, flask


def return_endpoints():
  for page in dash.page_registry.values():
    print(page['path'].split("/"))
    

print(flask.helpers.get_root_path())