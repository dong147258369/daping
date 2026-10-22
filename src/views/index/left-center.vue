<script setup lang="ts">
import { ref, reactive } from "vue";
import { graphic } from "echarts/core";
import { countUserNum } from "@/api";
import { ElMessage } from "element-plus";

const option = ref({});
const state = reactive({
  lockNum: 0,
  offlineNum: 0,
  onlineNum: 0,
  alarmNum: 0,
  totalNum: 0,
});

const getData = () => {
  countUserNum().then((res) => {
    if (res.success) {
      state.lockNum = res.data.lockNum;
      state.offlineNum = res.data.offlineNum;
      state.onlineNum = res.data.onlineNum;
      state.totalNum = res.data.totalNum;
      state.alarmNum = res.data.alarmNum;
      setOption();
    } else {
      ElMessage.error(res.msg);
    }
  }).catch((err) => {
    ElMessage.error(err);
  });
};
getData();

const setOption = () => {
  const chartData = [
    {
      value: state.onlineNum,
      name: "门急诊",
      itemStyle: {
        color: new graphic.LinearGradient(0, 0, 1, 1, [
          { offset: 0, color: "#00F2FE" },
          { offset: 1, color: "#4FACFE" },
        ]),
        shadowColor: "rgba(0, 242, 254, 0.6)",
        shadowBlur: 12,
      },
    },
    {
      value: state.offlineNum,
      name: "普通住院",
      itemStyle: {
        color: new graphic.LinearGradient(0, 0, 1, 1, [
          { offset: 0, color: "#7F00FF" },
          { offset: 1, color: "#E100FF" },
        ]),
        shadowColor: "rgba(225, 0, 255, 0.6)",
        shadowBlur: 12,
      },
    },
    {
      value: state.lockNum,
      name: "重症监护",
      itemStyle: {
        color: new graphic.LinearGradient(0, 0, 1, 1, [
          { offset: 0, color: "#FFB300" },
          { offset: 1, color: "#F77737" },
        ]),
        shadowColor: "rgba(255, 179, 0, 0.6)",
        shadowBlur: 12,
      },
    },
    {
      value: state.alarmNum,
      name: "危急病患",
      itemStyle: {
        color: new graphic.LinearGradient(0, 0, 1, 1, [
          { offset: 0, color: "#FF0844" },
          { offset: 1, color: "#FF4E50" },
        ]),
        shadowColor: "rgba(255, 8, 68, 0.7)",
        shadowBlur: 14,
      },
    },
  ];

  option.value = {
    title: {
      top: "center",
      left: "center",
      text: [`{value|${state.totalNum}}`, "{name|今日就诊}"].join("\n"),
      textStyle: {
        rich: {
          value: {
            color: "#00f7f6",
            fontSize: 26,
            fontWeight: "bold",
            lineHeight: 28,
            textShadowColor: "rgba(0, 247, 246, 0.8)",
            textShadowBlur: 10,
          },
          name: {
            color: "rgba(255, 255, 255, 0.85)",
            fontSize: 13,
            lineHeight: 20,
          },
        },
      },
    },
    tooltip: {
      trigger: "item",
      backgroundColor: "rgba(8, 20, 48, 0.85)",
      borderColor: "#00f7f6",
      borderWidth: 1,
      padding: [8, 14],
      textStyle: {
        color: "#FFF",
      },
      formatter: "{b}<br/>就诊人数: <b>{c}</b> 人 ({d}%)",
    },
    series: [
      // 内部科技虚线圆环
      {
        type: "pie",
        radius: ["30%", "32%"],
        center: ["50%", "50%"],
        silent: true,
        label: { show: false },
        data: [{ value: 1 }],
        itemStyle: {
          color: "transparent",
          borderColor: "rgba(0, 247, 246, 0.35)",
          borderWidth: 1,
          borderType: "dashed",
        },
      },
      // 外部科技点状刻度环
      {
        type: "pie",
        radius: ["82%", "83%"],
        center: ["50%", "50%"],
        silent: true,
        label: { show: false },
        data: [{ value: 1 }],
        itemStyle: {
          color: "transparent",
          borderColor: "rgba(30, 144, 255, 0.25)",
          borderWidth: 1,
        },
      },
      // 核心南丁格尔玫瑰图
      {
        name: "患者分类态势",
        type: "pie",
        roseType: "radius",
        radius: ["36%", "75%"],
        center: ["50%", "50%"],
        itemStyle: {
          borderRadius: 8,
          borderColor: "rgba(10, 25, 50, 0.6)",
          borderWidth: 3,
        },
        label: {
          show: true,
          formatter: "{b}\n{c|{c}人} {per|{d}%}",
          rich: {
            b: {
              color: "#e2e8f0",
              fontSize: 12,
              lineHeight: 20,
            },
            c: {
              color: "#00F2FE",
              fontSize: 13,
              fontWeight: "bold",
            },
            per: {
              color: "#F6D365",
              fontSize: 12,
              fontWeight: "600",
            },
          },
        },
        emphasis: {
          scale: true,
          scaleSize: 8,
          itemStyle: {
            shadowBlur: 25,
          },
        },
        labelLine: {
          show: true,
          length: 12,
          length2: 24,
          smooth: 0.2,
          lineStyle: {
            color: "rgba(0, 242, 254, 0.6)",
            width: 1.5,
          },
        },
        data: chartData,
      },
    ],
  };
};
</script>

<template>
  <div class="pie-chart-wrap">
    <v-chart class="chart" :option="option" :autoresize="true" />
  </div>
</template>

<style scoped lang="scss">
.pie-chart-wrap {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;

  .chart {
    width: 100%;
    height: 100%;
  }
}
</style>
