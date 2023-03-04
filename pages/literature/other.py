import dash
from dash import html, dcc, Output, Input
from components.charts import overview
import pandas as pd

from constants import SECTION_FONT, VIEW_TYPES


dash.register_page(__name__, path='/literature/other')

df_freq = pd.read_csv('./figures/lit_overview_frequency.csv')
df_impact = pd.read_csv('./figures/lit_overview_impact.csv')


# ! ************ Callback functions for models overview bar charts ************

@dash.callback(Output("text_mining_overview_freq", "figure"), [Input("text_mining_view_type_freq", "value")])
def text_mining_types(view_types: str):
  '''Callback function for "text mining overview" bar chart
  
  ### Input:
  - `view_type: value`: View types available for choosing
  
  ### Output:
  - `overview_freq: figure`: A bar chart of all models' frequency
  '''
  df: pd.DataFrame = df_freq if (view_types == "Frequency") else df_impact
  return overview(
    df_filtered=df[df['Category'] == 'Text Mining'],
    height=600,
    title=f'Most popular text mining libraries/algorithms ({view_types.lower()})',
    labels={
      'Index': 'Models',
      'Total': 'Number of articles' if view_types == 'Frequency' else 'Impact score',
      'Subcategory': 'Category'
    }
  )


def feature_selection():
  return overview(
    df_filtered=df_freq[df_freq['Category'] == 'Selection'],
    height=600,
    title=f'Most popular feature selection techniques/algorithms',
    labels={
      'Index': 'Models',
      'Total': 'Number of articles',
      'Subcategory': ''
    }
  )


# @dash.callback(Output("model_overview_impact", "figure"), Input("model_view_type_impact", "value"))
# def feature_selection_types(view_types: str):
#   '''Callback function for "model overview (frequency)" bar chart
  
#   ### Input:
#   - `model_type: value`: View types available for choosing
  
#   ### Output:
#   - `overview_freq: figure`: A bar chart of all models' frequency
#   '''
#   return overview(
#     df_filtered=df_impact[df_impact['Category'] == 'Models'],
#     height=600,
#     title='Most popular models (weighted by impact)',
#     labels={
#       'Index': 'Models',
#       'Total': 'Impact score',
#       'Subcategory': 'Category'
#     },
#     barmode=view_types
#   )




layout = html.Div(
  className='container my-4',
  children=[
    html.Div(
      className="text-center",
      children=[
        html.H1(children='Literature Analysis - Other Visualizations'),
        html.P(children='Other visualizations related to our literature analysis')
      ]
    ),
    
    # Overview for text mining
    html.H2("Text Mining",style=SECTION_FONT),
    html.Div([
      dcc.Graph(id="text_mining_overview_freq"),
      html.Div([
        html.P("Graph Options:"),
        dcc.Dropdown(
          id="text_mining_view_type_freq",
          options=["Frequency", "Impact"],
          value="Frequency", 
          clearable=False
        )
      ], className='mx-5 px-5')
    ], className='mb-5 pb-5'),
    
    html.H2("Feature Selection",style=SECTION_FONT),
    dcc.Graph(figure=feature_selection())
  ]
)