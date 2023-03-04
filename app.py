from importlib.resources import path
from dash import html, dcc, Input, Output, ALL, ctx
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
      try:
        if (page['path'].split('/')[1] == section and page['path'].split('/')[2] != ""):
          return_list.append(page)
      except(IndexError):
        pass
    
    if len(return_list) == 0:
      raise Exception("There are no pages under this relative path")
    

    return [page for page in sorted(return_list, key=lambda x: x['relative_path'])]



app.layout = \
  html.Div(
    style={'fontFamily': 'monospace'},
    children=[
      dcc.Location(id="url"),
      # Sidebar HTML, containing route links and project title
      html.Div(
        id="sidebar-id",
        className="bg-black text-white py-4 sidebar",
        children=[
          html.A(id="close-sidebar", className="close-btn btn", children="×"),
          html.Div(
            children=[
              html.Div(
                className="mt-5",
                children=[
                  html.H4('Contents'),
                  html.Div(
                    className='row',
                    children=[
                      html.Div(
                        children=[
                          html.Div(
                            className="literature-content",
                            children=[html.A("Acknowledgements", href="/acknowledgments", id={"type":"link-navbar", "index": "/acknowledgments"})]
                          ),
                          html.Div(
                            className="section-head",
                            children=[html.A('Literature Analysis', href="/literature", id={"type":"link-navbar", "index": "/literature"})]
                          ),
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
                      # NOTE: Commented out because we don't need it just yet
                      # html.Div(
                      #   children=[
                      #     html.P('Dataset (in progress)', className='bg-light text-black display-block overflow-auto mt-2 px-2'),
                      #     html.Div(
                      #       className='dataset-content',
                      #       children=[
                      #         html.A(children='Price', href='/literature'),
                      #         html.A(children='Listings', href='/literature/features'),
                      #         html.A(children='Hosts', href='/literature/models'),
                      #         html.A(children='Amenities', href='/literature/other')
                      #       ]
                      #     )
                      #   ]
                      # ),
                      html.Div(
                        className="section-head pt-4", style={"fontWeight": 600},
                        children=[html.A('Visit our GitHub!', href="https://github.com/marked01one/rio-airbnb-web-portal")]
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
        id="body-id",
        className="main-body",
        children=[
          html.Div(
            className="d-flex justify-content-between",
            children=[
              html.Button(className="open-btn", id="open-sidebar", children="☰ Contents"),
              html.P("Airbnb Predictive Model - Data Visualizations", className="my-4 mx-4")
            ]
          ),
          dash.page_container,
          footer.Footer(
            statement="""
              This web portal is created to support the predictive modeling project initiated by Dr. Sonya Zhang from the 
              Computer Information Systems department of California Polytechnic State University, Pomona
            """,
            hyperlink_text='For more info on the project, check our GitHub repository',
            github_link='https://github.com/marked01one/rio-airbnb-predictive-model#-web-portals-',
            className="container mb-4"
          ).create()
        ]
      )
    ]
  )



@app.callback(Output({"type":"link-navbar", "index":ALL}, "className"), 
              [Input("url", "pathname"),Input({"type":"link-navbar", "index":ALL}, "id")])
def highlight_current_page(pathname, link_elements):
    return ["border border-white bg-black text-white active" if val["index"] == pathname else "not-active" for val in link_elements]


@app.callback(Output("sidebar-id", "style"), 
              [Input("close-sidebar", "n_clicks"), Input("open-sidebar", "n_clicks")])
def change_sidebar(close_sidebar, open_sidebar):
  if ctx.triggered_id == "close-sidebar":
    return {"width": "0px", "paddingLeft" : "0px", "paddingRight": "0px"}
  
  if ctx.triggered_id == "open-sidebar":
    return {"width": "250px", "paddingLeft" : "15px", "paddingRight": "15px"}


@app.callback(Output("body-id", "style"), 
              [Input("close-sidebar", "n_clicks"), Input("open-sidebar", "n_clicks")])
def change_sidebar(close_sidebar, open_sidebar):
  if ctx.triggered_id == "close-sidebar":
    return {"marginLeft": "0px"}
  
  if ctx.triggered_id == "open-sidebar":
    return {"marginLeft": '250px'}



# Run server
if __name__ == '__main__':
  app.run(debug=True, port=os.getenv("PORT", 5000))