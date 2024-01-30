import echarts from "https://esm.sh/echarts";
const runChart = () => {
    const chart = echarts.init(document.getElementById('main'), null, {
        renderer: 'canvas',
        useDirtyRect: false,
      });
    const option = {
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
        yAxis: {
            type: 'value'
            },
            series: [
                {
                    data: [120, 200, 150, 80, 70, 110, 130],
                    type: 'bar'
                }
            ]
        };

    chart.setOption(option);
    window.addEventListener('resize', function() {
        chart.resize();
    });
    
};

runChart()