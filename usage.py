from random import randint, sample

import dash_chartjs
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

COLOURS = [
    ('Red', '#FF6384'),
    ('Blue', '#36A2EB'),
    ('Yellow', '#FFCE56')
]

app.layout = html.Div(style={"maxWidth": "50%"}, children=[
    html.H1('Doughnut Chart'),
    dash_chartjs.ChartJS(
        id='example-doughnut-chart',
        type='doughnut',
        data={
            "labels": [c[0] for c in COLOURS],
            "datasets": [{
                "data": [300, 50, 100],
                "backgroundColor": [c[1] for c in COLOURS],
                "hoverBackgroundColor": [c[1] for c in COLOURS]
            }]
        }
    ),
    html.Button(id='swap-colours', children='Swap colours'),
    html.H1('Bar Chart'),
    dash_chartjs.ChartJS(
        id='example-bar-chart',
        type='horizontalBar',
        data={
            "labels": [c[0] for c in COLOURS],
            "datasets": [{
                "label": "Oranges sold",
                "data": [300000, 50000, 100],
                "backgroundColor": [c[1] for c in COLOURS],
                "hoverBackgroundColor": [c[1] for c in COLOURS]
            }]
        }
    ),
    html.Button(id='reset-values', children='Reset values'),
    html.Button(id='toggle-log', children='Toggle logarithmic/linear axis'),
])

@app.callback(
    Output(component_id='example-doughnut-chart', component_property='data'),
    [Input(component_id='swap-colours', component_property='n_clicks')],
    [State(component_id='example-doughnut-chart', component_property='data')]
)
def reset_(_, data):
    new_colours = sample(COLOURS, k=len(COLOURS))
    data['labels'] = [c[0] for c in new_colours]
    data['datasets'][0]['backgroundColor'] = [c[1] for c in new_colours]
    data['datasets'][0]['hoverBackgroundColor'] = [c[1] for c in new_colours]
    return data

@app.callback(
    Output(component_id='example-bar-chart', component_property='data'),
    [Input(component_id='reset-values', component_property='n_clicks')],
    [State(component_id='example-bar-chart', component_property='data')]
)
def reset_(_, data):
    data['datasets'][0]['data'] = [randint(1,10000000), randint(1,10000000), randint(1,10000000)]
    return data

@app.callback(
    Output(component_id='example-bar-chart', component_property='options'),
    [Input(component_id='toggle-log', component_property='n_clicks')],
    [State(component_id='example-bar-chart', component_property='options')]
)
def reset_(_, options):
    scale_type = options.get('scales', {}).get('xAxes', [{}])[0].get('type') if options else None
    new_options = {
        'scales': {
            'xAxes': [{
                'type': 'logarithmic' if scale_type == 'linear' else 'linear',
                'ticks': {'min': 1 if scale_type == 'linear' else 0, 'max': 10000000}
            }]
        }
    }
    return new_options


if __name__ == '__main__':
    app.run_server(debug=True)
