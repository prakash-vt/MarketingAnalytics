function engagements_chart(chart_data) {

    try {
        var engagement_chart_dom = document.getElementById("engagement_chart_container");
        var engagement_chart_obj = echarts.init(engagement_chart_dom);
        engagement_chart_option = {
            //color: ['#4FDAD5', '#FBB738'],
            color: social_eng_color,
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    // type: 'shadow',
                    label:{show:true}
                }
            },

            // legend: {
            //     top: '0%',
            //     right: '5%'
            // },
            grid: {
                top: grid_size[0],
                bottom: grid_size[1],
                right: grid_size[2],
                left: grid_size[3],
                
            },
            xAxis: {
                name: "Period",
                boundaryGap: false,
                nameLocation: "center",
                nameTextStyle: {
                    fontSize: 9,
                    padding: 12,
                    color: axis_color
                },
                type: 'category',
                axisLabel: {
                    fontSize: 9,
                    interval: 0,
                    formatter: function (value) {
                        return value.slice(label_length[0], label_length[1])
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: axis_color,
                        opacity: axis_opacity
                    }
                },
                axisTick: {
                    show: true,
                    alignWithLabel: true
                },
                data: chart_data['x_axis_data']
            },
            yAxis: {
                name: 'Count',
                nameLocation: "center",
                nameTextStyle: {
                    fontSize: 9,
                    padding: 15,
                    color: axis_color
                },
                axisLabel: {
                    fontSize: 9,
                },
                axisLine: {
                    lineStyle: {
                        color: axis_color,
                        opacity: axis_opacity
                    }
                },
                type: 'value'
            },
            series: [{
                name: "Facebook",
                data: chart_data['facebook_data'],
                type: 'line',
                smooth: true,
                symbol: 'emptyCircle',
                symbolSize: symbol_size,
                lineStyle: {
                    width: 3
                },
            },
            {
                name: "Instagram",
                data: chart_data['instagram_data'],
                type: 'line',
                smooth: true,
                symbol: 'emptyCircle',
                symbolSize: symbol_size,
                lineStyle: {
                    width: 3
                },
            },
            {
                name: "Twitter",
                data: chart_data['twitter_data'],
                type: 'line',
                smooth: true,
                symbol: 'emptyCircle',
                symbolSize: symbol_size,
                lineStyle: {
                    width: 3
                },
            }] 
        };
        if (engagement_chart_option && typeof engagement_chart_option === "object") {
            engagement_chart_obj.setOption(engagement_chart_option, true);
            removeLoader("engagement_chart_container")
        }

        $(window).on('resize', function () {
            engagement_chart_obj.resize();
        })
    }
    catch (e) { }
}
