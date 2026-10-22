<script setup lang="ts">
import { ref, onMounted } from "vue";
import ItemWrap from "@/components/item-wrap";
import { graphic } from "echarts/core";

// 左中：多维雷达图
const radarOption = ref({});
// 左下：医保基金监控
const fundOption = ref({});
// 中下：住院日与周转走势
const stayTrendOption = ref({});
// 右中：耗材与药房流速
const pharmacyOption = ref({});

// 右上：手术室16间实时矩阵
const surgeryRooms = ref([
  { id: "01", name: "心外杂交手术室", doctor: "赵主任", op: "冠脉搭桥术", status: "手术中", color: "#FF3366", duration: "145min" },
  { id: "02", name: "神外达芬奇室", doctor: "钱主任", op: "脑动脉瘤夹闭", status: "手术中", color: "#FF3366", duration: "210min" },
  { id: "03", name: "骨科洁净手术室", doctor: "孙主任", op: "全髋置换术", status: "接台准备", color: "#FFB300", duration: "准备中" },
  { id: "04", name: "普外内镜手术室", doctor: "李主任", op: "腹腔镜胆囊", status: "麻醉复苏", color: "#00F2FE", duration: "复苏室" },
  { id: "05", name: "胸外一体化手术室", doctor: "周主任", op: "肺结节切除", status: "手术中", color: "#FF3366", duration: "85min" },
  { id: "06", name: "妇产急诊手术室", doctor: "吴主任", op: "剖宫产术", status: "手术中", color: "#FF3366", duration: "40min" },
  { id: "07", name: "泌尿外科手术室", doctor: "郑主任", op: "输尿管软镜", status: "已消毒", color: "#07F7A8", duration: "空闲" },
  { id: "08", name: "眼耳鼻喉手术室", doctor: "王主任", op: "人工耳蜗植入", status: "手术中", color: "#FF3366", duration: "60min" },
]);

// 楼宇孪生数据
const buildings = ref([
  { name: "门急诊综合大楼", floors: "12层", people: 1680, energy: "88 kW·h", status: "高负荷", tagColor: "#FF3366" },
  { name: "第一临床住院楼", floors: "24层", people: 2150, energy: "142 kW·h", status: "正常", tagColor: "#00F2FE" },
  { name: "第二外科大楼", floors: "18层", people: 1420, energy: "115 kW·h", status: "手术高峰", tagColor: "#FFB300" },
  { name: "医技与检验实验中心", floors: "8层", people: 620, energy: "95 kW·h", status: "正常", tagColor: "#07F7A8" },
]);

// 质控流水
const qualityLogs = ref([
  { time: "15:40:12", dept: "消化内科", event: "高敏肌钙蛋白I危急值闭环", status: "已处置", stateColor: "#07F7A8" },
  { time: "15:36:55", dept: "呼吸重症科", event: "有创呼吸机气道高压报警排查", status: "处置中", stateColor: "#FFB300" },
  { time: "15:32:10", dept: "骨科三病区", event: "术后深静脉血栓高危风险干预", status: "已闭环", stateColor: "#07F7A8" },
  { time: "15:28:40", dept: "中心药房", event: "麻醉精神药品智能核销完成", status: "正常", stateColor: "#00F2FE" },
  { time: "15:22:18", dept: "心内科重症", event: "恶性心律失常报警复查处置", status: "已闭环", stateColor: "#07F7A8" },
]);

const initCharts = () => {
  // 左中：多维雷达图
  radarOption.value = {
    tooltip: { backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    radar: {
      indicator: [
        { name: "心血管科", max: 100 },
        { name: "急诊中心", max: 100 },
        { name: "神经外科", max: 100 },
        { name: "骨科中心", max: 100 },
        { name: "呼吸重症", max: 100 },
        { name: "儿科中心", max: 100 },
        { name: "妇产重症", max: 100 },
      ],
      shape: "polygon",
      splitNumber: 4,
      axisName: { color: "#99bfe8", fontSize: 11 },
      splitLine: { lineStyle: { color: ["rgba(0,247,246,0.1)", "rgba(0,247,246,0.2)", "rgba(0,247,246,0.3)", "rgba(0,247,246,0.5)"] } },
      splitArea: { show: false },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    series: [
      {
        name: "科室负荷指数",
        type: "radar",
        symbol: "circle",
        symbolSize: 6,
        data: [
          {
            value: [92, 98, 85, 78, 88, 76, 82],
            name: "实际负荷指数",
            itemStyle: { color: "#00F2FE" },
            lineStyle: { width: 2, color: "#00F2FE" },
            areaStyle: { color: "rgba(0,242,254,0.35)" },
          },
          {
            value: [80, 80, 80, 80, 80, 80, 80],
            name: "额定标准基线",
            itemStyle: { color: "#FFB300" },
            lineStyle: { width: 1.5, type: "dashed", color: "#FFB300" },
          },
        ],
      },
    ],
  };

  // 左下：医保基金监控柱状图
  fundOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    grid: { left: "14%", right: "8%", top: "16%", bottom: "16%" },
    xAxis: {
      type: "category",
      data: ["1月", "2月", "3月", "4月", "5月", "6月"],
      axisLabel: { color: "#99bfe8" },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    yAxis: {
      type: "value",
      name: "结算额(万元)",
      nameTextStyle: { color: "#00F2FE", fontSize: 11 },
      axisLabel: { color: "#99bfe8" },
      splitLine: { lineStyle: { color: "rgba(255,255,255,0.06)", type: "dashed" } },
    },
    series: [
      {
        name: "医保结算额",
        type: "bar",
        barWidth: 16,
        itemStyle: {
          borderRadius: [6, 6, 0, 0],
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#956FD4" },
            { offset: 1, color: "rgba(62,172,229,0.2)" },
          ]),
          shadowColor: "rgba(149,111,212,0.6)",
          shadowBlur: 8,
        },
        data: [1280, 1420, 1680, 1590, 1780, 1920],
      },
    ],
  };

  // 中下：平均住院日走势
  stayTrendOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    legend: { data: ["全院平均住院日", "床位周转率"], top: 0, textStyle: { color: "#FFF" } },
    grid: { left: "45px", right: "45px", top: "35px", bottom: "25px" },
    xAxis: {
      type: "category",
      data: ["2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06"],
      axisLabel: { color: "#99bfe8" },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    yAxis: [
      {
        type: "value",
        name: "住院日(天)",
        nameTextStyle: { color: "#00F2FE", fontSize: 11 },
        min: 4,
        max: 10,
        axisLabel: { color: "#99bfe8" },
        splitLine: { lineStyle: { color: "rgba(255,255,255,0.06)", type: "dashed" } },
      },
      {
        type: "value",
        name: "周转率(次/床)",
        nameTextStyle: { color: "#07F7A8", fontSize: 11 },
        axisLabel: { color: "#07F7A8" },
        splitLine: { show: false },
      },
    ],
    series: [
      {
        name: "全院平均住院日",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 7,
        lineStyle: { color: "#00F2FE", width: 3, shadowBlur: 10, shadowColor: "#00F2FE" },
        itemStyle: { color: "#FFF", borderColor: "#00F2FE", borderWidth: 2 },
        areaStyle: {
          color: new graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "rgba(0,242,254,0.35)" },
            { offset: 1, color: "rgba(0,242,254,0)" },
          ]),
        },
        data: [7.8, 7.5, 7.2, 6.9, 6.6, 6.4],
      },
      {
        name: "床位周转率",
        type: "line",
        yAxisIndex: 1,
        smooth: true,
        symbol: "circle",
        symbolSize: 7,
        lineStyle: { color: "#07F7A8", width: 3, shadowBlur: 10, shadowColor: "#07F7A8" },
        itemStyle: { color: "#FFF", borderColor: "#07F7A8", borderWidth: 2 },
        data: [3.8, 4.1, 4.3, 4.6, 4.9, 5.2],
      },
    ],
  };

  // 右中：耗材流速
  pharmacyOption.value = {
    tooltip: { trigger: "axis", backgroundColor: "rgba(10,24,52,0.9)", borderColor: "#00f7f6" },
    grid: { left: "22%", right: "10%", top: "10%", bottom: "10%" },
    xAxis: {
      type: "value",
      axisLabel: { color: "#99bfe8" },
      splitLine: { lineStyle: { color: "rgba(255,255,255,0.06)", type: "dashed" } },
    },
    yAxis: {
      type: "category",
      data: ["冠脉支架", "人工关节", "吻合器", "介入导管", "心脏起搏器"],
      axisLabel: { color: "#99bfe8", fontSize: 11 },
      axisLine: { lineStyle: { color: "rgba(0,247,246,0.3)" } },
    },
    series: [
      {
        name: "今日领用数",
        type: "bar",
        barWidth: 12,
        itemStyle: {
          borderRadius: [0, 6, 6, 0],
          color: new graphic.LinearGradient(1, 0, 0, 0, [
            { offset: 0, color: "#00F2FE" },
            { offset: 1, color: "#4FACFE" },
          ]),
        },
        data: [42, 28, 65, 84, 16],
      },
    ],
  };
};

onMounted(() => {
  initCharts();
});
</script>

<template>
  <div class="operation-dashboard">
    <!-- 左侧列 -->
    <div class="col-left">
      <!-- 左上：全院核心运营指标透视 -->
      <ItemWrap class="col-item" title="全院核心运营指标透视">
        <div class="kpi-grid">
          <div class="kpi-box box-cyan">
            <span class="kpi-label">今日门急诊量</span>
            <span class="kpi-val"><b class="c-cyan">4,680</b> 人次</span>
            <span class="kpi-sub">环比昨日 +5.8%</span>
          </div>
          <div class="kpi-box box-green">
            <span class="kpi-label">今日入院人数</span>
            <span class="kpi-val"><b class="c-green">286</b> 人</span>
            <span class="kpi-sub">出院 272 人</span>
          </div>
          <div class="kpi-box box-yellow">
            <span class="kpi-label">全院在院病患</span>
            <span class="kpi-val"><b class="c-yellow">2,850</b> 人</span>
            <span class="kpi-sub">重症占比 14.2%</span>
          </div>
          <div class="kpi-box box-pink">
            <span class="kpi-label">全院床位使用率</span>
            <span class="kpi-val"><b class="c-pink">94.6%</b></span>
            <span class="kpi-sub">高效运营区间</span>
          </div>
        </div>
      </ItemWrap>

      <!-- 左中：多维雷达图 -->
      <ItemWrap class="col-item" title="重点科室就诊负荷多维雷达">
        <v-chart class="chart" :option="radarOption" :autoresize="true" />
      </ItemWrap>

      <!-- 左下：医保基金智能监控 -->
      <ItemWrap class="col-item" title="医保基金结算与智能监控">
        <v-chart class="chart" :option="fundOption" :autoresize="true" />
      </ItemWrap>
    </div>

    <!-- 中央核心列 -->
    <div class="col-center">
      <!-- 院区数字孪生楼宇透视图 -->
      <div class="building-twin-box">
        <div class="twin-header">
          <div class="twin-title">成都市第二人民医院 · 院区三维数字孪生全景</div>
          <div class="twin-tags">
            <span class="tag">今日总能耗: <b>2,850 kWh</b></span>
            <span class="tag">全院在岗医护: <b>1,420 人</b></span>
          </div>
        </div>

        <div class="buildings-canvas">
          <div class="building-card" v-for="(b, i) in buildings" :key="i">
            <div class="b-header">
              <span class="b-name">{{ b.name }}</span>
              <span class="b-status" :style="{ color: b.tagColor, borderColor: b.tagColor }">{{ b.status }}</span>
            </div>
            <div class="b-body">
              <div class="b-metric">
                <span class="lbl">空间规模:</span>
                <span class="val">{{ b.floors }}</span>
              </div>
              <div class="b-metric">
                <span class="lbl">实时人流:</span>
                <span class="val c-cyan">{{ b.people }} 人</span>
              </div>
              <div class="b-metric">
                <span class="lbl">能耗负载:</span>
                <span class="val c-yellow">{{ b.energy }}</span>
              </div>
            </div>
            <div class="b-ground-light"></div>
          </div>
        </div>
      </div>

      <!-- 中下：全院平均住院日走势 -->
      <ItemWrap class="center-bottom" title="全院平均住院日与床位周转率走势">
        <v-chart class="chart" :option="stayTrendOption" :autoresize="true" />
      </ItemWrap>
    </div>

    <!-- 右侧列 -->
    <div class="col-right">
      <!-- 右上：中心手术室实时运行看板 -->
      <ItemWrap class="col-item" title="全院中心手术室实时运行看板">
        <div class="surgery-grid">
          <div class="surgery-card" v-for="s in surgeryRooms" :key="s.id">
            <div class="s-top">
              <span class="s-id">室{{ s.id }}</span>
              <span class="s-badge" :style="{ color: s.color, borderColor: s.color }">{{ s.status }}</span>
            </div>
            <div class="s-name" :title="s.name">{{ s.name }}</div>
            <div class="s-meta">
              <span>{{ s.doctor }}</span>
              <span class="s-dur">{{ s.duration }}</span>
            </div>
          </div>
        </div>
      </ItemWrap>

      <!-- 右中：耗材流速 -->
      <ItemWrap class="col-item" title="重点高值耗材流转监测">
        <v-chart class="chart" :option="pharmacyOption" :autoresize="true" />
      </ItemWrap>

      <!-- 右下：医疗质控流水 -->
      <ItemWrap class="col-item" title="全院医疗质控与不良事件实时播报">
        <div class="quality-list beautify-scroll-def">
          <div class="q-item" v-for="(q, idx) in qualityLogs" :key="idx">
            <span class="q-idx">0{{ idx + 1 }}</span>
            <div class="q-body">
              <div class="q-row1">
                <span class="q-dept">【{{ q.dept }}】</span>
                <span class="q-time">{{ q.time }}</span>
                <span class="q-state" :style="{ color: q.stateColor }">{{ q.status }}</span>
              </div>
              <div class="q-row2">{{ q.event }}</div>
            </div>
          </div>
        </div>
      </ItemWrap>
    </div>
  </div>
</template>

<style scoped lang="scss">
.operation-dashboard {
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

  .building-twin-box {
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

    .twin-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;

      .twin-title {
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 2px;
        background: linear-gradient(92deg, #0072ff, #00eaff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }

      .twin-tags {
        display: flex;
        gap: 12px;
        .tag {
          background: rgba(255, 255, 255, 0.08);
          border: 1px solid rgba(0, 247, 246, 0.3);
          border-radius: 12px;
          padding: 4px 12px;
          color: #fff;
          font-size: 13px;
          b { color: #00F2FE; }
        }
      }
    }

    .buildings-canvas {
      flex: 1;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      padding: 10px;

      .building-card {
        background: radial-gradient(circle at center, rgba(16, 45, 90, 0.7) 0%, rgba(6, 18, 42, 0.9) 100%);
        border: 1px solid rgba(0, 247, 246, 0.25);
        border-radius: 8px;
        padding: 14px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s, border-color 0.3s;

        &:hover {
          transform: translateY(-4px);
          border-color: #00F2FE;
          box-shadow: 0 0 16px rgba(0, 242, 254, 0.3);
        }

        .b-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          .b-name { font-size: 15px; font-weight: bold; color: #fff; }
          .b-status { font-size: 11px; border: 1px solid; border-radius: 4px; padding: 1px 6px; }
        }

        .b-body {
          display: flex;
          flex-direction: column;
          gap: 6px;
          margin: 12px 0;
          .b-metric {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            .lbl { color: rgba(255, 255, 255, 0.6); }
            .val { font-weight: bold; color: #fff; }
            .c-cyan { color: #00F2FE; }
            .c-yellow { color: #FFB300; }
          }
        }

        .b-ground-light {
          position: absolute;
          bottom: 0;
          left: 0;
          right: 0;
          height: 3px;
          background: linear-gradient(90deg, transparent, #00F2FE, transparent);
        }
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

// KPI 卡片网格
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  height: 100%;
  padding: 4px 0;

  .kpi-box {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 8px 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;

    .kpi-label { font-size: 12px; color: rgba(255, 255, 255, 0.7); }
    .kpi-val {
      font-size: 18px;
      font-weight: bold;
      color: #fff;
      b { font-size: 22px; }
      .c-cyan { color: #00F2FE; }
      .c-green { color: #07F7A8; }
      .c-yellow { color: #FFB300; }
      .c-pink { color: #F02FC2; }
    }
    .kpi-sub { font-size: 11px; color: rgba(255, 255, 255, 0.45); }
  }
}

// 手术室矩阵
.surgery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  height: 100%;
  padding: 6px 0;

  .surgery-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(0, 247, 246, 0.2);
    border-radius: 6px;
    padding: 6px 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .s-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      .s-id { font-size: 11px; font-weight: bold; color: #00F2FE; }
      .s-badge { font-size: 10px; border: 1px solid; border-radius: 4px; padding: 0 3px; }
    }
    .s-name { font-size: 11px; color: #fff; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin: 2px 0; }
    .s-meta {
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      color: rgba(255, 255, 255, 0.6);
      .s-dur { color: #FFB300; }
    }
  }
}

// 质控列表
.quality-list {
  height: 100%;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 6px;

  .q-item {
    display: flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 4px;
    padding: 6px 8px;
    border: 1px solid rgba(255, 255, 255, 0.06);

    .q-idx {
      width: 20px;
      height: 20px;
      line-height: 20px;
      text-align: center;
      font-size: 11px;
      font-weight: bold;
      color: #00F2FE;
      background: rgba(0, 242, 254, 0.15);
      border-radius: 4px;
      margin-right: 8px;
      flex-shrink: 0;
    }

    .q-body {
      flex: 1;
      .q-row1 {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        .q-dept { color: #00F2FE; font-weight: bold; }
        .q-time { color: rgba(255, 255, 255, 0.45); font-size: 11px; }
        .q-state { font-size: 11px; font-weight: bold; }
      }
      .q-row2 {
        font-size: 11px;
        color: rgba(255, 255, 255, 0.75);
        margin-top: 2px;
      }
    }
  }
}
</style>
