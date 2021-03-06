# Dash ChartJS

Dash ChartJS is a Dash component which allows you to use [ChartJS](https://www.chartjs.org/samples/latest/) charts in Dash.

It uses [react-chartjs-2](https://github.com/jerairrest/react-chartjs-2) to render the charts, and
is basically a wrapper around that.

This project was generated by the [dash-component-boilerplate](https://github.com/plotly/dash-component-boilerplate) it contains the minimal set of code required to create your own custom Dash component.

## Usage

### 1. Create a simple chart

```python
import dash_chartjs
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
)
```

### 2. Use a callback to randomise the data

```python
@app.callback(
    Output(component_id='example-doughnut-chart', component_property='data'),
    [Input(component_id='reset-values', component_property='n_clicks')],
    [State(component_id='example-doughnut-chart', component_property='data')]
)
def reset_values(_, data):
    data['datasets'][0]['data'] = [randint(1,300), randint(1,300), randint(1,300)]
    return data
```
