<script setup lang="ts">
import { ref, onMounted } from "vue";
import { alarmNum } from "@/api";
import { graphic } from "echarts/core";
import { ElMessage } from "element-plus";

const option = ref({});
const getData = () => {
  alarmNum()
    .then((res) => {
      if (res.success) {
        setOption(res.data.dateList, res.data.numList, res.data.numList2);
      } else {
        ElMessage({
          message: res.msg,
          type: "warning",
        });
      }
    })
    .catch((err) => {
      ElMessage.error(err);
    });
};

const setOption = async (xData: any[], yData: any[], yData2: any[]) => {
  option.value = {
    tooltip: {
      trigger: "axis",
      backgroundColor: "rgba(10, 24, 52, 0.9)",
      borderColor: "#00f7f6",
      borderWidth: 1,
      padding: [10, 16],
      textStyle: {
        color: "#FFF",
      },
      axisPointer: {
        type: "cross",
        lineStyle: {
          color: "rgba(0, 247, 246, 0.4)",
          type: "dashed",
        },
        crossStyle: {
          color: "rgba(0, 247, 246, 0.4)",
        },
      },
      formatter: function (params: any) {
        let res = `<div style="font-weight:bold;margin-bottom:6px;color:#00f7f6;">时段: ${params[0].name}</div>`;
        params.forEach((item: any) => {
          const unit = item.seriesName.includes("急诊") ? "人次" : "次";
          res += `${item.marker} <span style="color:#ddd">${item.seriesName}</span>: <b style="color:#fff">${item.value}</b> ${unit}<br/>`;
        });
        return res;
      },
    },
    legend: {
      data: ["急诊接诊量", "危急值预警量"],
      textStyle: {
        color: "rgba(255, 255, 255, 0.85)",
        fontSize: 12,
      },
      top: 4,
      right: 20,
      itemGap: 20,
    },
    grid: {
      left: "15px",
      right: "30px",
      bottom: "12px",
      top: "40px",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      data: xData,
      boundaryGap: false,
      splitLine: {
        show: true,
        lineStyle: {
          color: "rgba(31, 99, 163, 0.15)",
          type: "dashed",
        },
      },
      axisLine: {
        lineStyle: {
          color: "rgba(0, 247, 246, 0.3)",
        },
      },
      axisLabel: {
        color: "#7EB7FD",
        fontWeight: "500",
      },
    },
    yAxis: [
      {
        type: "value",
        name: "急诊(人)",
        nameTextStyle: {
          color: "rgba(0, 245, 212, 0.8)",
          fontSize: 11,
          padding: [0, 0, 4, 10],
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: "rgba(31, 99, 163, 0.15)",
            type: "dashed",
          },
        },
        axisLine: {
          lineStyle: {
            color: "rgba(0, 245, 212, 0.3)",
          },
        },
        axisLabel: {
          color: "#7EB7FD",
        },
      },
      {
        type: "value",
        name: "危急值(次)",
        nameTextStyle: {
          color: "rgba(255, 42, 109, 0.8)",
          fontSize: 11,
          padding: [0, 10, 4, 0],
        },
        splitLine: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(255, 42, 109, 0.3)",
          },
        },
        axisLabel: {
          color: "#f87171",
        },
      },
    ],
    series: [
      // 曲线1：急诊接诊量（高饱和青碧霓虹光）
      {
        data: yData,
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 7,
        name: "急诊接诊量",
        lineStyle: {
          color: "#00F5D4",
          width: 3.5,
          shadowColor: "rgba(0, 245, 212, 0.8)",
          shadowBlur: 14,
        },
        itemStyle: {
          color: "#FFFFFF",
          borderColor: "#00F5D4",
          borderWidth: 2,
          shadowColor: "#00F5D4",
          shadowBlur: 8,
        },
        areaStyle: {
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(0, 245, 212, 0.45)" },
            { offset: 0.6, color: "rgba(0, 245, 212, 0.15)" },
            { offset: 1, color: "rgba(0, 245, 212, 0)" },
          ]),
        },
        markPoint: {
          data: [
            {
              name: "最大值",
              type: "max",
              valueDim: "y",
              symbol: "roundRect",
              symbolSize: [88, 28],
              symbolOffset: [0, -22],
              itemStyle: {
                color: "rgba(10, 30, 60, 0.85)",
                borderColor: "#00F5D4",
                borderWidth: 1.5,
                shadowColor: "#00F5D4",
                shadowBlur: 10,
              },
              label: {
                color: "#00F5D4",
                fontSize: 11,
                fontWeight: "bold",
                formatter: "急诊高峰:{c}人",
              },
            },
          ],
        },
      },
      // 曲线2：危急值预警量（火热警示霓虹）
      {
        data: yData2,
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        symbol: "circle",
        symbolSize: 7,
        name: "危急值预警量",
        lineStyle: {
          color: "#FF2A6D",
          width: 3,
          shadowColor: "rgba(255, 42, 109, 0.9)",
          shadowBlur: 14,
        },
        itemStyle: {
          color: "#FFFFFF",
          borderColor: "#FF2A6D",
          borderWidth: 2,
          shadowColor: "#FF2A6D",
          shadowBlur: 8,
        },
        areaStyle: {
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(255, 42, 109, 0.4)" },
            { offset: 0.6, color: "rgba(255, 42, 109, 0.1)" },
            { offset: 1, color: "rgba(255, 42, 109, 0)" },
          ]),
        },
        markPoint: {
          data: [
            {
              name: "最大值",
              type: "max",
              valueDim: "y",
              symbol: "roundRect",
              symbolSize: [84, 28],
              symbolOffset: [0, -22],
              itemStyle: {
                color: "rgba(10, 30, 60, 0.85)",
                borderColor: "#FF2A6D",
                borderWidth: 1.5,
                shadowColor: "#FF2A6D",
                shadowBlur: 10,
              },
              label: {
                color: "#FF2A6D",
                fontSize: 11,
                fontWeight: "bold",
                formatter: "预警峰值:{c}次",
              },
            },
          ],
        },
      },
    ],
  };
};

onMounted(() => {
  getData();
});
</script>

<template>
  <div class="chart-container">
    <v-chart class="chart" :option="option" :autoresize="true" v-if="JSON.stringify(option) != '{}'" />
  </div>
</template>

<style scoped lang="scss">
.chart-container {
  width: 100%;
  height: 100%;
  .chart {
    width: 100%;
    height: 100%;
  }
}
</style>
