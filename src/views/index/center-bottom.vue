<script setup lang="ts">
import { ref, onMounted } from "vue";
import { installationPlan } from "@/api";
import { graphic } from "echarts/core";
import { ElMessage } from "element-plus";

const option = ref({});
const getData = () => {
  installationPlan()
    .then((res) => {
      if (res.success) {
        setOption(res.data);
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

const setOption = async (newData: any) => {
  option.value = {
    tooltip: {
      trigger: "axis",
      backgroundColor: "rgba(10, 24, 52, 0.88)",
      borderColor: "#00f7f6",
      borderWidth: 1,
      padding: [10, 16],
      textStyle: {
        color: "#FFF",
      },
      axisPointer: {
        type: "shadow",
        shadowStyle: {
          color: "rgba(0, 247, 246, 0.08)",
        },
      },
      formatter: function (params: any) {
        let result = `<div style="font-weight:bold;margin-bottom:4px;color:#00f7f6;">${params[0].name}</div>`;
        params.forEach(function (item: any) {
          if (item.value !== undefined && !item.seriesName.includes("Top")) {
            if (item.seriesName === "床位使用率") {
              result += `${item.marker} <span style="color:#ddd">${item.seriesName}</span>: <b style="color:#F02FC2">${item.value}%</b><br/>`;
            } else if (item.seriesName === "在用床位") {
              result += `${item.marker} <span style="color:#ddd">${item.seriesName}</span>: <b style="color:#00F2FE">${item.value} 张</b><br/>`;
            } else if (item.seriesName === "编制床位") {
              result += `${item.marker} <span style="color:#ddd">${item.seriesName}</span>: <b style="color:#B372CF">${item.value} 张</b><br/>`;
            }
          }
        });
        return result;
      },
    },
    legend: {
      data: ["在用床位", "编制床位", "床位使用率"],
      textStyle: {
        color: "rgba(255, 255, 255, 0.85)",
        fontSize: 12,
      },
      top: "4",
      itemGap: 24,
    },
    grid: {
      left: "50px",
      right: "45px",
      bottom: "35px",
      top: "38px",
    },
    xAxis: {
      data: newData.category,
      axisLine: {
        lineStyle: {
          color: "rgba(0, 242, 254, 0.3)",
        },
      },
      axisTick: {
        show: false,
      },
      axisLabel: {
        color: "#99bfe8",
        fontSize: 12,
        interval: 0,
      },
    },
    yAxis: [
      {
        name: "床位数(张)",
        nameTextStyle: {
          color: "rgba(255, 255, 255, 0.6)",
          fontSize: 11,
          padding: [0, 0, 4, -20],
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: "rgba(255, 255, 255, 0.06)",
            type: "dashed",
          },
        },
        axisLine: {
          lineStyle: {
            color: "rgba(0, 242, 254, 0.3)",
          },
        },
        axisLabel: {
          color: "#99bfe8",
        },
      },
      {
        name: "使用率(%)",
        nameTextStyle: {
          color: "rgba(255, 255, 255, 0.6)",
          fontSize: 11,
          padding: [0, -20, 4, 0],
        },
        splitLine: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(240, 47, 194, 0.3)",
          },
        },
        axisLabel: {
          color: "#f472b6",
          formatter: "{value}%",
        },
      },
    ],
    series: [
      // 编制床位（底层阴影发光柱）
      {
        name: "编制床位",
        type: "bar",
        barGap: "-100%",
        barWidth: 14,
        itemStyle: {
          borderRadius: [6, 6, 0, 0],
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(168, 85, 247, 0.5)" },
            { offset: 0.5, color: "rgba(147, 51, 234, 0.25)" },
            { offset: 1, color: "rgba(126, 34, 206, 0.05)" },
          ]),
          borderWidth: 1,
          borderColor: "rgba(192, 132, 252, 0.4)",
        },
        z: 1,
        data: newData.lineData,
      },
      // 在用床位（亮丽发光立体水晶柱）
      {
        name: "在用床位",
        type: "bar",
        barWidth: 14,
        itemStyle: {
          borderRadius: [6, 6, 0, 0],
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#00F2FE" },
            { offset: 0.5, color: "#0072FF" },
            { offset: 1, color: "rgba(0, 114, 255, 0.2)" },
          ]),
          shadowColor: "rgba(0, 242, 254, 0.6)",
          shadowBlur: 10,
        },
        z: 2,
        data: newData.barData,
      },
      // 在用床位顶部光帽 (3D 水晶效果)
      {
        name: "在用床位Top",
        type: "pictorialBar",
        symbol: "roundRect",
        symbolSize: [14, 4],
        symbolOffset: [0, -2],
        symbolPosition: "end",
        z: 3,
        itemStyle: {
          color: "#00FFFF",
          shadowColor: "#00FFFF",
          shadowBlur: 8,
        },
        silent: true,
        data: newData.barData,
      },
      // 床位使用率（荧光发光平滑脉冲线）
      {
        name: "床位使用率",
        type: "line",
        smooth: true,
        showAllSymbol: true,
        symbol: "circle",
        symbolSize: 8,
        yAxisIndex: 1,
        z: 5,
        lineStyle: {
          color: "#F02FC2",
          width: 3.5,
          shadowColor: "rgba(240, 47, 194, 0.8)",
          shadowBlur: 12,
        },
        itemStyle: {
          color: "#FFFFFF",
          borderColor: "#F02FC2",
          borderWidth: 2.5,
          shadowColor: "#F02FC2",
          shadowBlur: 10,
        },
        areaStyle: {
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(240, 47, 194, 0.4)" },
            { offset: 0.8, color: "rgba(240, 47, 194, 0.05)" },
            { offset: 1, color: "rgba(240, 47, 194, 0)" },
          ]),
        },
        data: newData.rateData,
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
