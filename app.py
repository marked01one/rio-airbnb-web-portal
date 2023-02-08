from layout import make_layout
import dash, os
import dash_bootstrap_components as dbc

# Import stylesheets
external_stylesheets = [
  {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css",
    "integrity": "sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi",
    "crossorigin": "anonymous"
  }
]

# <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

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
  app.run(debug=True, port=os.getenv("PORT", default=5000))