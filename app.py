from importlib.resources import path
from dash import html, dcc, Input, Output, ALL
import dash, os
from components import footer

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
    "src": "https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js",
    "type": "text/javascript"
    }
]


# Initialize app
app = dash.Dash(
  __name__,
  external_stylesheets=external_stylesheets,
  external_scripts=external_scripts,
  use_pages=True
)

server = app.server
app.suppress_callback_exceptions = True


def filter_page(section: str) -> list:
    return_list = []
    
    for page in dash.page_registry.values():
      if page['path'].split('/')[1] == section:
        return_list.append(page)
    
    if len(return_list) == 0:
      raise Exception("There are no pages under this relative path")
    
    
    
    return [page for page in sorted(return_list, key=lambda x: x['relative_path'])]


app.layout = \
  html.Div(
    className="row",
    style={'fontFamily': 'monospace'},
    children=[
      dcc.Location(id="url"),
      # Sidebar HTML, containing route links and project title
      html.Div(
        className="col-12 col-lg-2 bg-black text-white py-4 sidebar",
        children=[
          html.Div(
            children=[
              html.Div(
                className='text-center pb-4',
                children=[
                html.H4('Airbnb Predictive Model'),
                html.A(
                  children="Web Portal GitHub Link", 
                  href="https://github.com/marked01one/rio-airbnb-web-portal", 
                  style={'fontStyle': 'italic', 'fontWeight': 600}, 
                  className="text-decoration-none text-black btn btn-light btn-border-dark github-link"
                )
              ]),
              html.Div(
                className='px-3',
                children=[
                  html.H4('Contents'),
                  html.Div(
                    className='row',
                    children=[
                      html.Div(
                        className='col-6 col-lg-12',
                        children=[
                          html.Div(
                            className="literature-content",
                            children=[
                              html.A("Acknowledgements", href="/acknowledgments", id={"type":"link-navbar", "index": "/acknowledgments"})
                            ]
                          ),
                          html.P('Literature Analysis', className='bg-light text-black display-block overflow-auto mt-2 px-2'),
                          html.Div(
                            className='literature-content',
                            children=[
                              html.A(
                                children=page['name'], 
                                href=page['relative_path'],
                                id={"type":"link-navbar", "index": page["relative_path"]}
                              )
                              for page in filter_page('literature')
                            ]
                          )
                        ]  
                      ),
                      html.Div(
                        className='col-6 col-lg-12',
                        children=[
                          html.P('Dataset (in progress)', className='bg-light text-black display-block overflow-auto mt-2 px-2'),
                          html.Div(
                            className='dataset-content',
                            children=[
                              html.A(children='Price', href='/literature'),
                              html.A(children='Listings', href='/literature/features'),
                              html.A(children='Hosts', href='/literature/models'),
                              html.A(children='Amenities', href='/literature/other')
                            ]
                          )
                        ]
                      )
                    ]
                  )
                ]
              ),
              html.P(id="url_callback")
            ]
          )
        ]
      ),
        
      # Main content container
      html.Div(
        className="col-12 col-lg-10 main-body",
        children=[
          dash.page_container,
          footer.Footer(
            statement="""
              This web portal is created to support the predictive modeling project initiated by Dr. Sonya Zhang from the 
              Computer Information Systems department of California Polytechnic State University, Pomona
            """,
            hyperlink_text='For more info on the project, click on this link',
            github_link='https://github.com/marked01one/rio-airbnb-predictive-model#-web-portals-',
            className="container mb-4"
          ).create()
        ]
      )
    ]
  )

@app.callback(Output({"type":"link-navbar", "index":ALL}, "className"), 
[Input("url", "pathname"),Input({"type":"link-navbar", "index":ALL}, "id")])
def callback_func(pathname, link_elements):
    return ["border border-white active" if val["index"] == pathname else "not-active" for val in link_elements]


# Run server
if __name__ == '__main__':
  app.run(debug=True, port=os.getenv("PORT", 5000))