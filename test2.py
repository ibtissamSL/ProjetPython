import dash  # version 1.13.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Callbacks/Pattern%20Matching%20Callbacks/Caste.csv")
df.rename(columns={'under_trial': 'under trial', 'state_name': 'state'}, inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Button('Add Chart', id='add-chart', n_clicks=0),
    ]),
    html.Div(id='container', children=[])
])


@app.callback(
    Output('container', 'children'),
    [Input('add-chart', 'n_clicks')],
    [State('container', 'children')]
)
def display_graphs(n_clicks, div_children):
    new_child = html.Div(
        style={'width': '45%', 'display': 'inline-block', 'outline': 'thin lightgrey solid', 'padding': 10},
        children=[
            dcc.Graph(
                id={
                    'type': 'dynamic-graph',
                    'index': n_clicks
                },
                figure={}
            ),
            dcc.RadioItems(
                id={
                    'type': 'dynamic-choice',
                    'index': n_clicks
                },
                options=[{'label': 'Bar Chart', 'value': 'bar'},
                         {'label': 'Line Chart', 'value': 'line'},
                         {'label': 'Pie Chart', 'value': 'pie'}],
                value='bar',
            ),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-s',
                    'index': n_clicks
                },
                options=[{'label': s, 'value': s} for s in np.sort(df['state'].unique())],
                multi=True,
                value=["Andhra Pradesh", "Maharashtra"],
            ),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-ctg',
                    'index': n_clicks
                },
                options=[{'label': c, 'value': c} for c in ['caste', 'gender', 'state']],
                value='state',
                clearable=False
            ),
            dcc.Dropdown(
                id={
                    'type': 'dynamic-dpn-num',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['detenues', 'under trial', 'convicts', 'others']],
                value='convicts',
                clearable=False
            )
        ]
    )
    div_children.append(new_child)
    return div_children


@app.callback(
    Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
    [Input(component_id={'type': 'dynamic-dpn-s', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-dpn-ctg', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'dynamic-dpn-num', 'index': MATCH}, component_property='value'),
     Input({'type': 'dynamic-choice', 'index': MATCH}, 'value')]
)
def update_graph(s_value, ctg_value, num_value, chart_choice):
    print(s_value)
    dff = df[df['state'].isin(s_value)]

    if chart_choice == 'bar':
        dff = dff.groupby([ctg_value], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
        fig = px.bar(dff, x=ctg_value, y=num_value)
        return fig
    elif chart_choice == 'line':
        if len(s_value) == 0:
            return {}
        else:
            dff = dff.groupby([ctg_value, 'year'], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
            fig = px.line(dff, x='year', y=num_value, color=ctg_value)
            return fig
    elif chart_choice == 'pie':
        fig = px.pie(dff, names=ctg_value, values=num_value)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)

    
    
# https://youtu.be/4gDwKYaA6ww





# # import dash
# # import dash_bootstrap_components as dbc
# # #import dash_core_components as dcc
# # #import dash_html_components as html
# # from dash.dependencies import Input, Output
# # import plotly.express as px
# # import pandas as pd
# # from dash import html,dcc

# # app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # df = pd.read_csv(r"https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Berlin_crimes.csv")
# # df = df.groupby('District')[['Street_robbery', 'Drugs']].median()

# # app.layout = html.Div([
# #         dbc.Row(dbc.Col(html.H3("Easy Date"),
# #                         width={'size': 6, 'offset': 5},
# #                         ),
# #                 ),
# #         dbc.Row(dbc.Col(html.Div("One column is all we need because there ain't no room for the "
# #                                  "both of us in this raggedy town"),
# #                         width=4
# #                         )
# #                 ),
# #         dbc.Row(
# #             [
# #                 dbc.Col(dcc.Dropdown(id='c_dropdown', placeholder='last dropdown',
# #                                      options=[{'label': 'Option A', 'value': 'optA'},
# #                                               {'label': 'Option B', 'value': 'optB'}]),
# #                         width={'size': 3, "offset": 2, 'order': 3}
# #                         ),
# #                 dbc.Col(dcc.Dropdown(id='a_dropdown', placeholder='first dropdown',
# #                                      options=[{'label': 'Option A', 'value': 'optA'},
# #                                               {'label': 'Option B', 'value': 'optB'}]),
# #                         width={'size': 4, "offset": 1, 'order': 1}
# #                         ),
# #                 dbc.Col(dcc.Dropdown(id='b_dropdown', placeholder='middle dropdown',
# #                                      options=[{'label': 'Option A', 'value': 'optA'},
# #                                               {'label': 'Option B', 'value': 'optB'}]),
# #                         width={'size': 2,  "offset": 0, 'order': 2}
# #                         ),
# #             ],# no_gutters=True
# #         ),
# #         dbc.Row(
# #             [
# #                 dbc.Col(dcc.Graph(id='pie_chart1', figure={}),
# #                         width=8, lg={'size': 6,  "offset": 0, 'order': 'first'}
# #                         ),
# #                 dbc.Col(dcc.Graph(id='pie_chart2', figure={}),
# #                         width=4, lg={'size': 6,  "offset": 0, 'order': 'last'}
# #                         ),
# #             ]
# #         )
# # ])

# # @app.callback(
# #     [Output('pie_chart1', 'figure'),
# #      Output('pie_chart2', 'figure')],
# #     [Input('a_dropdown', 'value'),
# #      Input('b_dropdown', 'value'),
# #      Input('c_dropdown', 'value')]
# # )
# # def update_graph(dpdn_a, dpdn_b, dpdn_c):
# #     dff = df[:200]
# #     if dpdn_a is None or dpdn_b is None or dpdn_c is None:
# #         pie_fig = px.pie(dff, names=dff.index, values='Street_robbery', title='Street Robbery Berlin')\
# #             .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside',  textinfo='label+percent')
# #         pie_fig2 = px.pie(dff, names=dff.index, values='Drugs', title='Drugs Berlin')\
# #             .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside', textinfo='label+percent')
# #         return pie_fig, pie_fig2
# #     else:
# #         raise dash.exceptions.PreventUpdate

# # if __name__ == "__main__":
# #     app.run_server(debug=True)


# # '''import dash
# # import dash_core_components as dcc
# # import dash_html_components as html
# # from dash.dependencies import Input, Output
# # import os 
# # from PIL import Image
# # import numpy as np
# # import plotly.express as px
# # from dash import Dash, dcc, html

# # #os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# # app = Dash(__name__, external_stylesheets=external_stylesheets)

# # app.layout = html.Div(
# #     [
# #         html.Img(src ='C:/Users/lhaton/Desktop/Dash/venv1/Scripts/logo.png')
# # ])

# # if __name__ == "__main__":
# #     app.run_server(debug=True)
# # '''


# import dash
# import dash_bootstrap_components as dbc
# #import dash_core_components as dcc
# #import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# from dash import html,dcc

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# df = pd.read_csv(r"https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Berlin_crimes.csv")
# df = df.groupby('District')[['Street_robbery', 'Drugs']].median()

# app.layout = html.Div([
#         dbc.Row(dbc.Col(html.H3("Easy Date"),
#                         width={'size': 6, 'offset': 5},
#                         ),
#                 ),
#         dbc.Row(dbc.Col(html.Div("One column is all we need because there ain't no room for the "
#                                  "both of us in this raggedy town"),
#                         width=4
#                         )
#                 ),
#         dbc.Row(
#             [
#                 dbc.Col(dcc.Dropdown(id='c_dropdown', placeholder='last dropdown',
#                                      options=[{'label': 'Option A', 'value': 'optA'},
#                                               {'label': 'Option B', 'value': 'optB'}]),
#                         width={'size': 3, "offset": 2, 'order': 3}
#                         ),
#                 dbc.Col(dcc.Dropdown(id='a_dropdown', placeholder='first dropdown',
#                                      options=[{'label': 'Option A', 'value': 'optA'},
#                                               {'label': 'Option B', 'value': 'optB'}]),
#                         width={'size': 4, "offset": 1, 'order': 1}
#                         ),
#                 dbc.Col(dcc.Dropdown(id='b_dropdown', placeholder='middle dropdown',
#                                      options=[{'label': 'Option A', 'value': 'optA'},
#                                               {'label': 'Option B', 'value': 'optB'}]),
#                         width={'size': 2,  "offset": 0, 'order': 2}
#                         ),
#             ],# no_gutters=True
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(dcc.Graph(id='pie_chart1', figure={}),
#                         width=8, lg={'size': 6,  "offset": 0, 'order': 'first'}
#                         ),
#                 dbc.Col(dcc.Graph(id='pie_chart2', figure={}),
#                         width=4, lg={'size': 6,  "offset": 0, 'order': 'last'}
#                         ),
#             ]
#         )
# ])

# @app.callback(
#     [Output('pie_chart1', 'figure'),
#      Output('pie_chart2', 'figure')],
#     [Input('a_dropdown', 'value'),
#      Input('b_dropdown', 'value'),
#      Input('c_dropdown', 'value')]
# )
# def update_graph(dpdn_a, dpdn_b, dpdn_c):
#     dff = df[:200]
#     if dpdn_a is None or dpdn_b is None or dpdn_c is None:
#         pie_fig = px.pie(dff, names=dff.index, values='Street_robbery', title='Street Robbery Berlin')\
#             .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside',  textinfo='label+percent')
#         pie_fig2 = px.pie(dff, names=dff.index, values='Drugs', title='Drugs Berlin')\
#             .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside', textinfo='label+percent')
#         return pie_fig, pie_fig2
#     else:
#         raise dash.exceptions.PreventUpdate

# if __name__ == "__main__":
#     app.run_server(debug=True)


# # '''import dash
# # import dash_core_components as dcc
# # import dash_html_components as html
# # from dash.dependencies import Input, Output
# # import os 
# # from PIL import Image
# # import numpy as np
# # import plotly.express as px
# # from dash import Dash, dcc, html

# # #os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# # app = Dash(__name__, external_stylesheets=external_stylesheets)

# # app.layout = html.Div(
# #     [
# #         html.Img(src ='C:/Users/lhaton/Desktop/Dash/venv1/Scripts/logo.png')
# # ])

# # if __name__ == "__main__":
# #     app.run_server(debug=True)
# # '''