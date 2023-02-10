import dash
from dash import html, dcc


dash.register_page(__name__, path='/acknowledgments')

layout = html.Div(
  className='container acknowledgements',
  children=[
    html.H1(children='Acknowledgements', className="text-center"),
    dcc.Markdown("""
    ## Purpose of Research
    Our research aims to create price predictive models for Airbnb properties in Los Angeles using a set of key features. To set the context for our investigation, 
    we reviewed recent literature related to these features and methods, paying particular attention to their frequency, importance, and usage. 
    
    ## Faculty Mentor:
    * **Sonya Zhang**
      * Developing the lit review and coding structure, reviewing articles, coding, advising on data collection, methodologies, data analysis, and visualization, revising, proofreading, and formatting the report.
    
    ## Student Researchers:
    * **Jin Im**
      * Reviewing articles, coding, preliminary analysis and visualization on Listing Attributes, Clustering, and Text Mining.
    * **Minh Khoi Tran**
      * Reviewing articles, coding, preliminary analysis and visualization on overall variables, Regression models, Classification models, Clustering, and Text Mining.
    * **Christine Pugay**
      * Reviewing articles, coding, preliminary analysis and visualization on Policy Attributes, Neighborhood Attributes, POIs.
    * **Kelly Lee**
      * Reviewing articles, coding, preliminary analysis and visualization on Review Attributes, Host Attributes.
    """
    )
  ]
)