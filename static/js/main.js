
$(document).ready(function() {

Highcharts.createElement('link', {
   href: 'https://fonts.googleapis.com/css?family=Signika:400,700',
   rel: 'stylesheet',
   type: 'text/css'
}, null, document.getElementsByTagName('head')[0]);

// Add the background image to the container
Highcharts.wrap(Highcharts.Chart.prototype, 'getContainer', function (proceed) {
   proceed.call(this);
   this.container.style.background =
      'url(http://www.highcharts.com/samples/graphics/sand.png)';
});


Highcharts.theme = {
   colors: ['#f45b5b', '#8085e9', '#8d4654', '#7798BF', '#aaeeee',
      '#ff0066', '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
   chart: {
      backgroundColor: null,
      style: {
         fontFamily: 'Signika, serif'
      }
   },
   title: {
      style: {
         color: 'black',
         fontSize: '16px',
         fontWeight: 'bold'
      }
   },
   subtitle: {
      style: {
         color: 'black'
      }
   },
   legend: {
      itemStyle: {
         fontWeight: 'bold',
         fontSize: '13px'
      }
   },
   xAxis: {
      labels: {
         style: {
            color: '#6e6e70'
         }
      }
   },
   yAxis: {
      labels: {
         style: {
            color: '#6e6e70'
         }
      }
   },
   plotOptions: {
      series: {
         shadow: true
      },
      candlestick: {
         lineColor: '#404048'
      },
      map: {
         shadow: false
      }
   },

   // Highstock specific
   navigator: {
      xAxis: {
         gridLineColor: '#D0D0D8'
      }
   },
   rangeSelector: {
      buttonTheme: {
         fill: 'white',
         stroke: '#C0C0C8',
         'stroke-width': 1,
         states: {
            select: {
               fill: '#D0D0D8'
            }
         }
      }
   },
   scrollbar: {
      trackBorderColor: '#C0C0C8'
   },

   // General
   background2: '#E0E0E8'

};

// Apply the theme
Highcharts.setOptions(Highcharts.theme);


Highcharts.chart('container', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Power Price Over Time for Index' + index+ '<br>Longitude: '+ lon.toFixed(3) + '    Latitude: '+ lat.toFixed(3) +'      Location:'+ loc+'<br>',
            style : { "color": "#1B5E20", "fontSize": "25px" }


        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                    'Click and drag in the plot area to zoom in, click the legend to hide the data' : 'Pinch the chart to zoom in'
        },
        xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: { // don't display the dummy year
            month: '%b. %e',
            year: '%b'
        },
        title: {
            text: 'Date'
        }
    },
        tooltip: {
        shared: true,
        crosshairs: true,
        headerFormat: '<b>{point.x:%b. %e}</b><br>',
        pointFormat: '{series.name}: ${point.y:.2f}<br>'
    },
        yAxis: {
            title: {
                text: 'Power Price'
            }
        },
        legend: {
            align: 'left',
            verticalAlign: 'top',
            borderWidth: 0
        },

        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: series

 });

});
