// vue-echarts
import ECharts from 'vue-echarts'
import { use } from "echarts/core"
import {
    CanvasRenderer
  } from 'echarts/renderers'
  import {
    BarChart, PieChart, MapChart, EffectScatterChart, LineChart, PictorialBarChart, LinesChart, RadarChart
  } from 'echarts/charts'
  import {
    GridComponent,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    DatasetComponent,
    VisualMapComponent,
    GeoComponent,
    MarkPointComponent,
    RadarComponent
  } from 'echarts/components'

  use([
    CanvasRenderer,
    BarChart, PieChart, MapChart, EffectScatterChart, LineChart, PictorialBarChart, LinesChart, RadarChart,
    GridComponent,
    LegendComponent,
    TooltipComponent,
    TitleComponent,
    DatasetComponent,
    VisualMapComponent,
    GeoComponent,
    MarkPointComponent,
    RadarComponent
  ])

  export const registerEcharts= (app:any)=>{
    app.component('v-chart', ECharts)
  }