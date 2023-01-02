from a import app
from flask import current_app
app_cxt = app.app_context()
app_cxt.push()
print(current_app.name)
app_cxt.pop()
print(app.url_map)
