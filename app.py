from layout import make_layout
import dash, os

# Import stylesheets
external_stylesheets = [
  {
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css",
    "rel": "stylesheet",
    "integrity": "sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD",
    "crossorigin": "anonymous"
  }
]

external_scripts = [
  {
    "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js",
    "integrity": "sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD",
    "crossorigin": "anonymous"
  }
]


# Initialize app
app = dash.Dash(
  __name__,
  external_stylesheets=external_stylesheets,
  use_pages=True
)

server = app.server

# Run server
if __name__ == '__main__':
  app.layout = make_layout()
  app.run(debug=True, port=os.getenv("PORT", 5000))