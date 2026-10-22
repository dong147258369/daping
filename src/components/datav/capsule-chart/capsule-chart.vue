<script setup lang="ts">
import { onMounted, reactive, ref, watch } from "vue";
import type { DefaultConfigType } from "./index.d";
import { cloneDeep, merge } from "lodash-es";

const mergedConfig = ref<any>(null);
const capsuleLength = ref<number[]>([]);
const capsuleValue = ref<number[]>([]);
const labelData = ref<number[]>([]);

const defaultConfig = reactive<DefaultConfigType>({
  colors: [
    "linear-gradient(90deg, #00f2fe 0%, #4facfe 100%)",
    "linear-gradient(90deg, #43e97b 0%, #38f9d7 100%)",
    "linear-gradient(90deg, #fa709a 0%, #fee140 100%)",
    "linear-gradient(90deg, #30cfd0 0%, #330867 100%)",
    "linear-gradient(90deg, #a18cd1 0%, #fbc2eb 100%)",
    "linear-gradient(90deg, #f093fb 0%, #f5576c 100%)",
    "linear-gradient(90deg, #4facfe 0%, #00f2fe 100%)",
    "linear-gradient(90deg, #5ee7df 0%, #b490ca 100%)",
  ],
  unit: "",
  showValue: true,
});

const props = withDefaults(
  defineProps<{
    config: object | any;
    data: Array<{
      name: string;
      value: string | number;
    }>;
  }>(),
  {
    config: () => ({}),
    data: () => [],
  }
);

const calcData = () => {
  mergeConfig();
  calcCapsuleLengthAndLabelData();
};

const mergeConfig = () => {
  mergedConfig.value = merge(cloneDeep(defaultConfig), props.config || {});
};

const calcCapsuleLengthAndLabelData = () => {
  if (!props.data.length) return;
  const newcapsuleValue = props.data.map((item: any) => Number(item.value));
  const maxValue = Math.max(...newcapsuleValue);
  capsuleValue.value = newcapsuleValue;
  capsuleLength.value = newcapsuleValue.map((v: any) =>
    maxValue ? v / maxValue : 0
  );
  const oneFifth = maxValue / 5;
  const newlabelData = Array.from(
    new Set(new Array(6).fill(0).map((v, i) => Math.ceil(i * oneFifth)))
  );
  labelData.value = newlabelData;
};

watch(() => props.data, () => calcData(), { deep: true });
watch(() => props.config, () => calcData(), { deep: true });

onMounted(() => {
  calcData();
});
</script>

<template>
  <div class="dv-capsule-chart">
    <template v-if="mergedConfig">
      <div class="capsule-list">
        <div class="capsule-row" v-for="(item, index) in data" :key="item.name">
          <!-- 排名序号角标 -->
          <span
            class="rank-badge"
            :class="{
              'rank-top1': index === 0,
              'rank-top2': index === 1,
              'rank-top3': index === 2,
            }"
          >
            0{{ index + 1 }}
          </span>

          <!-- 科室名称 -->
          <div class="row-name" :title="item.name">{{ item.name }}</div>

          <!-- 发光胶囊主体 -->
          <div class="row-track">
            <div
              class="row-bar"
              :style="{
                width: `${(capsuleLength[index] || 0) * 100}%`,
                background: mergedConfig.colors[index % mergedConfig.colors.length],
              }"
            >
              <div class="bar-shine"></div>
            </div>
          </div>

          <!-- 数值与单位 -->
          <div class="row-value">
            <span class="value-num">{{ item.value }}</span>
            <span class="unit-span" v-if="mergedConfig.unit">{{ mergedConfig.unit }}</span>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped lang="scss">
.dv-capsule-chart {
  position: relative;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;

  .capsule-list {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    height: 100%;
    padding: 2px 0;
  }

  .capsule-row {
    display: flex;
    align-items: center;
    margin: 3px 0;

    .rank-badge {
      width: 22px;
      height: 18px;
      line-height: 18px;
      text-align: center;
      font-size: 11px;
      font-weight: bold;
      border-radius: 4px;
      margin-right: 8px;
      background: rgba(255, 255, 255, 0.08);
      color: rgba(255, 255, 255, 0.6);
      flex-shrink: 0;

      &.rank-top1 {
        background: linear-gradient(135deg, #ffd700, #ff8c00);
        color: #fff;
        box-shadow: 0 0 8px rgba(255, 215, 0, 0.6);
      }
      &.rank-top2 {
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        color: #fff;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.6);
      }
      &.rank-top3 {
        background: linear-gradient(135deg, #b372cf, #e0c3fc);
        color: #fff;
        box-shadow: 0 0 8px rgba(179, 114, 207, 0.6);
      }
    }

    .row-name {
      width: 90px;
      font-size: 13px;
      color: rgba(255, 255, 255, 0.88);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex-shrink: 0;
    }

    .row-track {
      flex: 1;
      height: 10px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      margin: 0 10px;
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(0, 247, 246, 0.2);

      .row-bar {
        height: 100%;
        border-radius: 6px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);

        .bar-shine {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: linear-gradient(
            90deg,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.5) 50%,
            rgba(255, 255, 255, 0) 100%
          );
          opacity: 0.6;
          border-radius: 6px;
        }
      }
    }

    .row-value {
      width: 65px;
      text-align: right;
      flex-shrink: 0;

      .value-num {
        font-size: 14px;
        font-weight: bold;
        color: #00f7f6;
        text-shadow: 0 0 6px rgba(0, 247, 246, 0.6);
      }

      .unit-span {
        font-size: 11px;
        color: rgba(255, 255, 255, 0.6);
        margin-left: 3px;
      }
    }
  }
}
</style>
