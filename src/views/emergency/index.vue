<script setup lang="ts">
import { ref, onMounted } from "vue";
import ItemWrap from "@/components/item-wrap";
import { graphic } from "echarts/core";
import CountUp from "@/components/count-up";

// 左上：急救车状态分布
const carStatusOption = ref({});
// 左中：绿色通道时效达成率
const greenChannelOption = ref({});
// 左下：急救病种分类玫瑰图
const diseaseOption = ref({});
// 中下：24小时急救出车走势
const trendOption = ref({});
// 右中：响应达成率走势
const responseRateOption = ref({});

// 右上：抢救床位实时数据
const emergencyBeds = ref([
  { bed: "抢救-01", patient: "王*明 (62岁)", type: "急性心梗", hr: 118, spo2: "92%", bp: "158/96", status: "抢救中", color: "#FF3366" },
  { bed: "抢救-02", patient: "李*华 (45岁)", type: "重度脑卒中", hr: 88, spo2: "97%", bp: "172/108", status: "溶栓中", color: "#FFB300" },
  { bed: "抢救-03", patient: "张*强 (33岁)", type: "多发性创伤", hr: 125, spo2: "90%", bp: "95/60", status: "紧急会诊", color: "#FF3366" },
  { bed: "抢救-04", patient: "陈*芳 (58岁)", type: "急性哮喘重度", hr: 102, spo2: "94%", bp: "135/85", status: "雾化平喘", color: "#00F2FE" },
  { bed: "抢救-05", patient: "周*国 (71岁)", type: "心源性休克", hr: 135, spo2: "86%", bp: "82/50", status: "升压抢救", color: "#FF0844" },
  { bed: "抢救-06", patient: "黄*莉 (29岁)", type: "急腹症待查", hr: 84, spo2: "99%", bp: "120/78", status: "完善检查", color: "#07F7A8" },
]);

// 右下：实时流水
const streamLogs = ref([
  { time: "15:42:10", car: "粤A·6982", loc: "天河区天府路88号", dept: "胸痛急救中心", state: "出车途中" },
  { time: "15:39:05", car: "粤A·3210", loc: "越秀区东风东路205号", dept: "脑卒中急救部", state: "接诊转运中" },
  { time: "15:35:48", car: "粤A·8831", loc: "海珠区新港中路12号", dept: "多发创伤抢救", state: "已送达抢救室" },
  { time: "15:31:22", car: "粤A·5412", loc: "黄埔区科学大道66号", dept: "危重孕产妇通道", state: "接诊转运中" },
  { time: "15:26:40", car: "粤A·9102", loc: "白云区机场路302号", dept: "儿科危重急救", state: "已送达抢救室" },
  { time: "15:20:15", car: "粤A·1120", loc: "荔湾区中山八路78号", dept: "心搏骤停CPR", state: "已送达EICU" },
]);

const initCharts = () => {
  // 左上：急救车状态环形图
  carStatusOption.value = {
    tooltip: { trigger: "item", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    legend: { bottom: 0, textStyle: { color: "#FFF", fontSize: 11 }, itemGap: 10 },
    series: [
      {
        type: "pie",
        radius: ["45%", "68%"],
        center: ["50%", "42%"],
        itemStyle: { borderRadius: 6, borderColor: "rgba(10,24,52,0.8)", borderWidth: 2 },
        label: { show: false },
        data: [
          { value: 18, name: "出车抢救(18)", itemStyle: { color: "#FF3366" } },
          { value: 32, name: "待命就绪(32)", itemStyle: { color: "#00F2FE" } },
          { value: 6, name: "清洗消毒(6)", itemStyle: { color: "#07F7A8" } },
          { value: 4, name: "维保质检(4)", itemStyle: { color: "#FFB300" } },
        ],
      },
    ],
  };

  // 左中：绿色通道达标率柱状图
  greenChannelOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    grid: { left: "15%", right: "8%", top: "12%", bottom: "16%" },
    xAxis: {
      type: "category",
      data: ["胸痛中心", "卒中中心", "创伤中心", "高危孕产", "儿科急救"],
      axisLabel: { color: "#99bfe8", fontSize: 11, interval: 0 },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    yAxis: {
      type: "value",
      max: 100,
      axisLabel: { color: "#99bfe8", formatter: "{value}%" },
      splitLine: { lineStyle: { color: "rgba(255,255,255,0.06)", type: "dashed" } },
    },
    series: [
      {
        name: "时效达标率",
        type: "bar",
        barWidth: 16,
        itemStyle: {
          borderRadius: [6, 6, 0, 0],
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#00F2FE" },
            { offset: 1, color: "rgba(0,114,255,0.2)" },
          ]),
          shadowColor: "rgba(0,242,254,0.5)",
          shadowBlur: 8,
        },
        data: [96.8, 94.5, 92.0, 98.2, 95.6],
        label: {
          show: true,
          position: "top",
          formatter: "{c}%",
          color: "#00F2FE",
          fontSize: 11,
          fontWeight: "bold",
        },
      },
    ],
  };

  // 左下：急救病种分类玫瑰图
  diseaseOption.value = {
    tooltip: { trigger: "item", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    series: [
      {
        type: "pie",
        roseType: "radius",
        radius: ["25%", "72%"],
        center: ["50%", "50%"],
        itemStyle: { borderRadius: 6 },
        label: {
          show: true,
          formatter: "{b}\n{d}%",
          color: "#e2e8f0",
          fontSize: 11,
        },
        data: [
          { value: 168, name: "急性心血管", itemStyle: { color: "#FF3366" } },
          { value: 142, name: "脑血管卒中", itemStyle: { color: "#FFB300" } },
          { value: 125, name: "创伤骨折", itemStyle: { color: "#00F2FE" } },
          { value: 92, name: "急性中毒/感染", itemStyle: { color: "#B372CF" } },
          { value: 76, name: "呼吸衰竭", itemStyle: { color: "#07F7A8" } },
        ],
      },
    ],
  };

  // 中下：24小时急救出车走势
  trendOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    legend: { data: ["出车次数", "平均到达耗时(分)"], top: 0, textStyle: { color: "#FFF" } },
    grid: { left: "45px", right: "45px", top: "35px", bottom: "25px" },
    xAxis: {
      type: "category",
      data: ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"],
      axisLabel: { color: "#99bfe8" },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    yAxis: [
      {
        type: "value",
        name: "出车数(次)",
        nameTextStyle: { color: "#00F2FE", fontSize: 11 },
        axisLabel: { color: "#99bfe8" },
        splitLine: { lineStyle: { color: "rgba(255,255,255,0.06)", type: "dashed" } },
      },
      {
        type: "value",
        name: "到达耗时(分)",
        nameTextStyle: { color: "#F02FC2", fontSize: 11 },
        axisLabel: { color: "#f472b6" },
        splitLine: { show: false },
      },
    ],
    series: [
      {
        name: "出车次数",
        type: "bar",
        barWidth: 14,
        itemStyle: {
          borderRadius: [6, 6, 0, 0],
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#00F2FE" },
            { offset: 1, color: "rgba(0,114,255,0.1)" },
          ]),
        },
        data: [12, 8, 16, 32, 28, 35, 42, 26],
      },
      {
        name: "平均到达耗时(分)",
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        symbol: "circle",
        symbolSize: 6,
        lineStyle: { color: "#F02FC2", width: 3, shadowBlur: 10, shadowColor: "#F02FC2" },
        itemStyle: { color: "#FFF", borderColor: "#F02FC2", borderWidth: 2 },
        data: [9.2, 8.5, 9.8, 14.2, 13.5, 12.8, 15.6, 11.2],
      },
    ],
  };

  // 右中：响应达成率走势
  responseRateOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    grid: { left: "10%", right: "8%", top: "18%", bottom: "16%" },
    xAxis: {
      type: "category",
      data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
      axisLabel: { color: "#7EB7FD" },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    yAxis: {
      type: "value",
      min: 90,
      max: 100,
      axisLabel: { color: "#7EB7FD", formatter: "{value}%" },
      splitLine: { lineStyle: { color: "rgba(31,99,163,0.15)", type: "dashed" } },
    },
    series: [
      {
        name: "响应达标率",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 6,
        lineStyle: { color: "#07F7A8", width: 3, shadowBlur: 10, shadowColor: "#07F7A8" },
        itemStyle: { color: "#FFFFFF", borderColor: "#07F7A8", borderWidth: 2 },
        areaStyle: {
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(7,247,168,0.4)" },
            { offset: 1, color: "rgba(7,247,168,0)" },
          ]),
        },
        data: [96.2, 97.5, 95.8, 98.1, 96.9, 98.7, 99.2],
      },
    ],
  };
};

onMounted(() => {
  initCharts();
});
</script>

<template>
  <div class="emergency-dashboard">
    <!-- 左侧列 -->
    <div class="col-left">
      <ItemWrap class="col-item" title="120急救车辆实时态势">
        <v-chart class="chart" :option="carStatusOption" :autoresize="true" />
      </ItemWrap>
      <ItemWrap class="col-item" title="五大专科绿色通道达标率">
        <v-chart class="chart" :option="greenChannelOption" :autoresize="true" />
      </ItemWrap>
      <ItemWrap class="col-item" title="今日急救病种分类占比">
        <v-chart class="chart" :option="diseaseOption" :autoresize="true" />
      </ItemWrap>
    </div>

    <!-- 中央核心列 -->
    <div class="col-center">
      <!-- 智慧急救车GPS与热力调度中枢 -->
      <div class="center-radar-box">
        <div class="radar-header">
          <div class="radar-title">120急救智慧指挥网格实时调度大屏</div>
          <div class="stats-pills">
            <span class="pill"><b class="c-cyan">60</b> 辆全网在线</span>
            <span class="pill"><b class="c-red">18</b> 辆紧急出车</span>
            <span class="pill"><b class="c-green">11.8</b> 分钟平均到院</span>
          </div>
        </div>

        <!-- 模拟雷达网格地图效果 -->
        <div class="radar-map-sim">
          <div class="radar-sweep"></div>
          <div class="circle-layer c1"></div>
          <div class="circle-layer c2"></div>
          <div class="circle-layer c3"></div>
          <div class="hub-center">
            <div class="hub-core"></div>
            <span>总院区急救中心</span>
          </div>

          <!-- 急救车辆实时发光浮动点 -->
          <div class="car-point p1">
            <div class="car-icon pulse-red">🚑</div>
            <div class="car-tag">急救-粤A·6982 (胸痛D2B 18m)</div>
          </div>
          <div class="car-point p2">
            <div class="car-icon pulse-red">🚑</div>
            <div class="car-tag">急救-粤A·3210 (脑卒中溶栓)</div>
          </div>
          <div class="car-point p3">
            <div class="car-icon pulse-green">🚑</div>
            <div class="car-tag">急救-粤A·5412 (高危孕产转运)</div>
          </div>
          <div class="car-point p4">
            <div class="car-icon pulse-yellow">🚑</div>
            <div class="car-tag">急救-粤A·8831 (多发创伤待命)</div>
          </div>
        </div>
      </div>

      <!-- 中下：24小时急救出车走势 -->
      <ItemWrap class="center-bottom" title="24小时急救出车频次与平均到达时效走势">
        <v-chart class="chart" :option="trendOption" :autoresize="true" />
      </ItemWrap>
    </div>

    <!-- 右侧列 -->
    <div class="col-right">
      <!-- 右上：急诊抢救室床位状态卡片 -->
      <ItemWrap class="col-item" title="急诊抢救室与EICU床位监护">
        <div class="beds-grid">
          <div class="bed-card" v-for="bed in emergencyBeds" :key="bed.bed">
            <div class="bed-top">
              <span class="bed-name">{{ bed.bed }}</span>
              <span class="bed-status" :style="{ color: bed.color, borderColor: bed.color }">{{ bed.status }}</span>
            </div>
            <div class="bed-patient">{{ bed.patient }} · {{ bed.type }}</div>
            <div class="bed-vitals">
              <span>HR: <b :style="{ color: bed.hr > 110 ? '#FF3366' : '#00F2FE' }">{{ bed.hr }}</b></span>
              <span>SpO2: <b :style="{ color: bed.spo2 < '90%' ? '#FF0844' : '#07F7A8' }">{{ bed.spo2 }}</b></span>
              <span>BP: <b>{{ bed.bp }}</b></span>
            </div>
          </div>
        </div>
      </ItemWrap>

      <!-- 右中：急救响应达成率走势 -->
      <ItemWrap class="col-item" title="急救响应达标率走势 (7天)">
        <v-chart class="chart" :option="responseRateOption" :autoresize="true" />
      </ItemWrap>

      <!-- 右下：实时流水滚动 -->
      <ItemWrap class="col-item" title="120急救出车实时流水播报">
        <div class="stream-list beautify-scroll-def">
          <div class="stream-item" v-for="(item, idx) in streamLogs" :key="idx">
            <span class="idx-tag">0{{ idx + 1 }}</span>
            <div class="stream-content">
              <div class="s-row1">
                <span class="s-car">{{ item.car }}</span>
                <span class="s-time">{{ item.time }}</span>
                <span class="s-state" :class="{ 'state-red': item.state.includes('途') || item.state.includes('转'), 'state-green': item.state.includes('送达') }">
                  {{ item.state }}
                </span>
              </div>
              <div class="s-row2">
                <span class="s-dept">【{{ item.dept }}】</span>
                <span class="s-loc">{{ item.loc }}</span>
              </div>
            </div>
          </div>
        </div>
      </ItemWrap>
    </div>
  </div>
</template>

<style scoped lang="scss">
.emergency-dashboard {
  width: 100%;
  display: flex;
  min-height: calc(100% - 64px);
  justify-content: space-between;
}

.col-left,
.col-right {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 540px;
  box-sizing: border-box;
  flex-shrink: 0;
}

.col-center {
  flex: 1;
  margin: 0 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;

  .center-radar-box {
    height: 580px;
    background: rgba(10, 24, 52, 0.6);
    border: 1px solid rgba(0, 247, 246, 0.3);
    border-radius: 8px;
    padding: 16px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;

    .radar-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      z-index: 5;

      .radar-title {
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 2px;
        background: linear-gradient(92deg, #0072ff, #00eaff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }

      .stats-pills {
        display: flex;
        gap: 12px;
        .pill {
          background: rgba(255, 255, 255, 0.08);
          padding: 4px 12px;
          border-radius: 14px;
          font-size: 13px;
          color: #fff;
          border: 1px solid rgba(0, 247, 246, 0.3);
          .c-cyan { color: #00F2FE; }
          .c-red { color: #FF3366; }
          .c-green { color: #07F7A8; }
        }
      }
    }

    .radar-map-sim {
      flex: 1;
      position: relative;
      background: radial-gradient(circle, rgba(16, 40, 80, 0.8) 0%, rgba(4, 12, 28, 0.95) 100%);
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid rgba(0, 247, 246, 0.15);

      .circle-layer {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 1px dashed rgba(0, 247, 246, 0.25);
        border-radius: 50%;
        pointer-events: none;
        &.c1 { width: 160px; height: 160px; }
        &.c2 { width: 320px; height: 320px; }
        &.c3 { width: 480px; height: 480px; }
      }

      .radar-sweep {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 240px;
        height: 240px;
        transform-origin: 0 0;
        background: conic-gradient(from 0deg, rgba(0, 247, 246, 0.35) 0deg, transparent 60deg);
        animation: radarRotate 4s linear infinite;
        border-radius: 50%;
      }

      .hub-center {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 10;
        .hub-core {
          width: 18px;
          height: 18px;
          background: #00F2FE;
          border-radius: 50%;
          margin: 0 auto 4px;
          box-shadow: 0 0 15px #00F2FE;
          animation: pulse 2s infinite;
        }
        span {
          font-size: 12px;
          color: #00F2FE;
          font-weight: bold;
          text-shadow: 0 0 6px #000;
        }
      }

      .car-point {
        position: absolute;
        display: flex;
        align-items: center;
        gap: 6px;
        z-index: 10;
        cursor: pointer;
        transition: transform 0.3s;
        &:hover { transform: scale(1.1); }

        .car-icon {
          font-size: 18px;
          padding: 2px 4px;
          border-radius: 4px;
          background: rgba(0, 0, 0, 0.6);
          &.pulse-red { animation: pulseRed 1.5s infinite; }
          &.pulse-green { animation: pulseGreen 1.5s infinite; }
          &.pulse-yellow { animation: pulseYellow 1.5s infinite; }
        }

        .car-tag {
          font-size: 11px;
          background: rgba(10, 24, 52, 0.85);
          color: #fff;
          padding: 2px 8px;
          border-radius: 10px;
          border: 1px solid rgba(0, 247, 246, 0.4);
          white-space: nowrap;
        }

        &.p1 { top: 25%; left: 22%; }
        &.p2 { top: 68%; left: 30%; }
        &.p3 { top: 32%; left: 70%; }
        &.p4 { top: 75%; left: 68%; }
      }
    }
  }

  .center-bottom {
    height: 315px;
  }
}

.col-item {
  height: 310px;
}

.chart {
  width: 100%;
  height: 100%;
}

// 抢救床位网格
.beds-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  padding: 6px 2px;
  height: 100%;

  .bed-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(0, 247, 246, 0.2);
    border-radius: 6px;
    padding: 8px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .bed-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      .bed-name { font-weight: bold; color: #00F2FE; font-size: 13px; }
      .bed-status { font-size: 10px; border: 1px solid; padding: 1px 4px; border-radius: 4px; }
    }
    .bed-patient { font-size: 12px; color: rgba(255, 255, 255, 0.85); margin: 3px 0; }
    .bed-vitals {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: rgba(255, 255, 255, 0.6);
      b { margin-left: 2px; }
    }
  }
}

// 流水列表
.stream-list {
  height: 100%;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 4px 0;

  .stream-item {
    display: flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 4px;
    padding: 6px 8px;
    border: 1px solid rgba(255, 255, 255, 0.06);

    .idx-tag {
      width: 22px;
      height: 22px;
      line-height: 22px;
      text-align: center;
      font-size: 11px;
      font-weight: bold;
      color: #00F2FE;
      background: rgba(0, 242, 254, 0.15);
      border-radius: 4px;
      margin-right: 8px;
      flex-shrink: 0;
    }

    .stream-content {
      flex: 1;
      .s-row1 {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        .s-car { color: #fff; font-weight: bold; }
        .s-time { color: rgba(255, 255, 255, 0.5); font-size: 11px; }
        .s-state {
          font-size: 11px;
          font-weight: bold;
          &.state-red { color: #FF3366; }
          &.state-green { color: #07F7A8; }
        }
      }
      .s-row2 {
        display: flex;
        font-size: 11px;
        color: rgba(255, 255, 255, 0.65);
        margin-top: 2px;
        .s-dept { color: #00F2FE; margin-right: 4px; }
      }
    }
  }
}

@keyframes radarRotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(0, 247, 246, 0.7); }
  70% { box-shadow: 0 0 0 16px rgba(0, 247, 246, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 247, 246, 0); }
}

@keyframes pulseRed {
  0% { box-shadow: 0 0 0 0 rgba(255, 51, 102, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(255, 51, 102, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 51, 102, 0); }
}

@keyframes pulseGreen {
  0% { box-shadow: 0 0 0 0 rgba(7, 247, 168, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(7, 247, 168, 0); }
  100% { box-shadow: 0 0 0 0 rgba(7, 247, 168, 0); }
}

@keyframes pulseYellow {
  0% { box-shadow: 0 0 0 0 rgba(255, 179, 0, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(255, 179, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 179, 0, 0); }
}
</style>
