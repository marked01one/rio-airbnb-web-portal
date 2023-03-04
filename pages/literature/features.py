import dash
from dash import html, dcc, Input, Output
import pandas as pd 
import plotly.express as px
from constants import SECTION_FONT 
from components.charts import overview, categories_pie

dash.register_page(__name__, path='/literature/features')


df_freq = pd.read_csv('./figures/lit_overview_frequency.csv')
df_impact = pd.read_csv('./figures/lit_overview_impact.csv')


# ! ************************ Features page switch between impact & frequency ************************


@dash.callback(Output("features_overview_freq", "figure"), [Input("features_view_type_freq", "value")])
def feature_view_types(view_types: str):
  
  df: pd.DataFrame = df_freq if (view_types == "Frequency") else df_impact
  return overview(
    df_filtered=df[df['Category'] == 'Features'],
    height=1600,
    title=f'Most popular Airbnb ({view_types.lower()})',
    labels={
      'Index': 'Airbnb Features',
      'Total': 'Number of articles' if view_types == 'Frequency' else 'Impact score',
      'Subcategory': 'Category'
    }
  )
  
  pass


# ! ************************ Features page layout ************************

layout = html.Div(
  className='container my-4',
  children=[
    html.Div(
      className='text-center',
      children=[
        html.H1(children='Literature Analysis - Features'),
        html.Div(children='''
            Visualizations involving quantitative/qualitative features of Airbnb listings used in the reviewed literature
        ''')
      ]
    ),
    
    # Overview graphs
    html.H2("Overview:", style=SECTION_FONT),
    html.Div([
      dcc.Graph(id="features_overview_freq"),
      html.Div([
        html.P("Graph Options:"),
        dcc.Dropdown(
          id="features_view_type_freq",
          options=["Frequency", "Impact"],
          value="Frequency", 
          clearable=False
        )
      ], className='mx-5 px-5')
    ], className='mb-5 pb-5')
  ]
)