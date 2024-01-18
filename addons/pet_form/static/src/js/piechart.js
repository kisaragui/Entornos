/** @odoo-module **/

export function runChart() {
    
    // local.HomePage = instance.Widget.extend({
    //     start: function() {
    //         console.log("pet store home page loaded");
    //     },
    // });

    // instance.web.client_actions.add(
    //     'petstore.homepage', 'instance.oepetstore.HomePage');

        // Initialize the echarts instance based on the prepared dom
    var myChart = echarts.init(document.getElementById('chart_view'));

    // Specify the configuration items and data for the chart
    var option = {
        title: {
        text: 'ECharts Getting Started Example'
        },
        tooltip: {},
        legend: {
        data: ['sales']
        },
        xAxis: {
        data: ['Shirts', 'Cardigans', 'Chiffons', 'Pants', 'Heels', 'Socks']
        },
        yAxis: {},
        series: [
        {
            name: 'sales',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
        }
        ]
    };

// Display the chart using the configuration items and data just specified.
    return myChart.setOption(option);
}