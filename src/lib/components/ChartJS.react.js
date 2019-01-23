import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { Doughnut, Pie, Line, Bar, HorizontalBar,
         Radar, Polar, Bubble, Scatter } from 'react-chartjs-2';


/**
 * ChartJS renders charts using the ChartJS library
 */
export default class ChartJS extends Component {
    render() {
        switch(this.props.type) {
            case 'doughnut':
                return <Doughnut {...this.props} />
            case 'pie':
                return <Pie {...this.props} />
            case 'line':
                return <Line {...this.props} />
            case 'horizontalBar':
                return <HorizontalBar {...this.props} />
            case 'radar':
                return <Radar {...this.props} />
            case 'polar':
                return <Polar {...this.props} />
            case 'bubble':
                return <Bubble {...this.props} />
            case 'scatter':
                return <Scatter {...this.props} />
            case 'bar':
            default:
                return <Bar {...this.props} />
        }
    }
}

ChartJS.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * Type of chart to draw
     */
    type: PropTypes.oneOf([
        'scatter',
        'bubble',
        'polarArea',
        'radar',
        'horizontalBar',
        'bar',
        'line',
        'pie',
        'doughnut',
    ]),

    /**
     * Object holding the data to be displayed in the chart
     * eg <https://www.chartjs.org/docs/latest/charts/line.html#data-structure> for line charts
     */
    data: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.func
    ]).isRequired,

    /**
     * Height of chart
     */
    height: PropTypes.number,

    /**
     * Width of chart
     */
    width: PropTypes.number,

    /**
     * Legend configuration
     * See <https://www.chartjs.org/docs/latest/configuration/legend.html>
     */
    legend: PropTypes.object,

    /**
     * Configuration of the chart
     * See <https://www.chartjs.org/docs/latest/>
     */
    options: PropTypes.object,

    /**
     * Whether to redraw chart when it changes
     */
    redraw: PropTypes.bool
};

ChartJS.defaultProps = {
    legend: {
        display: true,
        position: 'bottom'
    },
    type: 'doughnut',
    height: 150,
    width: 300,
}
