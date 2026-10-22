<script setup lang="ts">
import { reactive, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import dayjs from "dayjs";
import type { DateDataType } from "./index.d";
import { useSettingStore } from "@/stores/index";

const route = useRoute();
const router = useRouter();

const dateData = reactive<DateDataType>({
  dateDay: "",
  dateYear: "",
  dateWeek: "",
  timing: null,
});

const { setSettingShow } = useSettingStore();
const weekday = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];
const timeFn = () => {
  dateData.timing = setInterval(() => {
    dateData.dateDay = dayjs().format("YYYY-MM-DD HH:mm:ss");
    dateData.dateWeek = weekday[dayjs().day()];
  }, 1000);
};
timeFn();

// 三大智慧医疗大屏导航配置
const screenList = [
  { name: "综合监控", path: "/index", title: "智慧医疗综合监控指挥大屏", icon: "🏥" },
  { name: "急救调度", path: "/emergency", title: "智慧急救与应急调度大屏", icon: "🚑" },
  { name: "全景运营", path: "/operation", title: "智慧医院全景运营监管大屏", icon: "📊" },
];

const currentTitle = computed(() => {
  const found = screenList.find((item) => item.path === route.path);
  return found ? found.title : "智慧医疗综合监控指挥大屏";
});

const navTo = (path: string) => {
  if (route.path !== path) {
    router.push(path);
  }
};
</script>

<template>
  <div class="d-flex jc-center title_wrap">
    <!-- 左侧大屏切换导航 Tab -->
    <div class="nav-switch-tabs">
      <div
        v-for="item in screenList"
        :key="item.path"
        class="tab-btn"
        :class="{ active: route.path === item.path }"
        @click="navTo(item.path)"
      >
        <span class="tab-icon">{{ item.icon }}</span>
        <span class="tab-label">{{ item.name }}</span>
        <span class="tab-light"></span>
      </div>
    </div>

    <div class="zuojuxing"></div>
    <div class="youjuxing"></div>
    <div class="guang"></div>
    <div class="d-flex jc-center">
      <div class="title">
        <span class="title-text">{{ currentTitle }}</span>
      </div>
    </div>
    <div class="timers">
      {{ dateData.dateWeek }} {{ dateData.dateDay }}

      <div class="setting_icon" @click="setSettingShow(true)" title="设置">
        <img src="@/assets/img/headers/setting.png" alt="设置" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.title_wrap {
  height: 60px;
  background-image: url("../assets/img/top.png");
  background-size: cover;
  background-position: center center;
  position: relative;
  margin-bottom: 4px;

  .nav-switch-tabs {
    position: absolute;
    left: 20px;
    top: 14px;
    display: flex;
    gap: 12px;
    z-index: 100;

    .tab-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 5px 14px;
      background: rgba(8, 24, 52, 0.7);
      border: 1px solid rgba(0, 247, 246, 0.3);
      border-radius: 4px;
      cursor: pointer;
      color: rgba(255, 255, 255, 0.8);
      font-size: 13px;
      font-weight: 500;
      letter-spacing: 1px;
      position: relative;
      overflow: hidden;
      transition: all 0.3s;

      .tab-icon {
        font-size: 14px;
      }

      &:hover {
        background: rgba(0, 247, 246, 0.15);
        border-color: #00f7f6;
        color: #fff;
        transform: translateY(-1px);
      }

      &.active {
        background: linear-gradient(135deg, rgba(0, 114, 255, 0.5), rgba(0, 234, 255, 0.35));
        border-color: #00f7f6;
        color: #00f7f6;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(0, 247, 246, 0.5), inset 0 0 6px rgba(0, 247, 246, 0.4);

        .tab-light {
          position: absolute;
          bottom: 0;
          left: 10%;
          width: 80%;
          height: 2px;
          background: #00f7f6;
          box-shadow: 0 0 6px #00f7f6;
        }
      }
    }
  }

  .guang {
    position: absolute;
    bottom: -26px;
    background-image: url("../assets/img/guang.png");
    background-position: 80px center;
    width: 100%;
    height: 56px;
  }

  .zuojuxing,
  .youjuxing {
    position: absolute;
    top: -2px;
    width: 140px;
    height: 6px;
    background-image: url("../assets/img/headers/juxing1.png");
  }

  .zuojuxing {
    left: 11%;
  }

  .youjuxing {
    right: 11%;
    transform: rotate(180deg);
  }

  .timers {
    position: absolute;
    right: 20px;
    top: 20px;
    font-size: 16px;
    color: rgba(255, 255, 255, 0.85);
    display: flex;
    align-items: center;
    z-index: 100;

    .setting_icon {
      width: 20px;
      height: 20px;
      cursor: pointer;
      margin-left: 14px;
      img {
        width: 100%;
        height: 100%;
      }
    }
  }
}

.title {
  position: relative;
  text-align: center;
  background-size: cover;
  color: transparent;
  height: 60px;
  line-height: 46px;

  .title-text {
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 5px;
    width: 100%;
    background: linear-gradient(
      92deg,
      #0072ff 0%,
      #00eaff 48.8525390625%,
      #01aaff 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    transition: all 0.3s;
  }
}
</style>
