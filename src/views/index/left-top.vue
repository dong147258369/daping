<script setup lang="ts">
import { reactive, ref } from "vue";
import { countDeviceNum } from "@/api";
import CountUp from "@/components/count-up";
import { ElMessage } from "element-plus";

const duration = ref(2);
const state = reactive({
  alarmNum: 0,
  offlineNum: 0,
  onlineNum: 0,
  totalNum: 0,
});

const getData = () => {
  countDeviceNum()
    .then((res) => {
      if (res.success) {
        state.alarmNum = res.data.alarmNum;
        state.offlineNum = res.data.offlineNum;
        state.onlineNum = res.data.onlineNum;
        state.totalNum = res.data.totalNum;
      } else {
        ElMessage.error(res.msg);
      }
    })
    .catch((err) => {
      ElMessage.error(err);
    });
};
getData();
</script>

<template>
  <ul class="user_Overview flex">
    <li class="user_Overview-item item-lan">
      <div class="user_Overview_nums allnum bgdonghua">
        <CountUp :endVal="state.totalNum" :duration="duration" />
      </div>
      <p>设备总数</p>
    </li>
    <li class="user_Overview-item item-lv">
      <div class="user_Overview_nums online bgdonghua">
        <CountUp :endVal="state.onlineNum" :duration="duration" />
      </div>
      <p>在用正常</p>
    </li>
    <li class="user_Overview-item item-huang">
      <div class="user_Overview_nums offline bgdonghua">
        <CountUp :endVal="state.offlineNum" :duration="duration" />
      </div>
      <p>维护停机</p>
    </li>
    <li class="user_Overview-item item-hong">
      <div class="user_Overview_nums laramnum bgdonghua">
        <CountUp :endVal="state.alarmNum" :duration="duration" />
      </div>
      <p>质控预警</p>
    </li>
  </ul>
</template>

<style scoped lang="scss">
@keyframes rotating {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.user_Overview {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;

  li {
    flex: 1;

    p {
      text-align: center;
      height: 20px;
      line-height: 20px;
      font-size: 15px;
      font-weight: 500;
      letter-spacing: 1px;
    }

    .user_Overview_nums {
      width: 102px;
      height: 102px;
      text-align: center;
      line-height: 102px;
      font-size: 24px;
      font-weight: bold;
      margin: 40px auto 20px;
      position: relative;
      cursor: pointer;
      transition: transform 0.3s;

      &:hover {
        transform: scale(1.08);
      }

      &::before {
        content: "";
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-size: 100% 100%;
        background-position: center center;
        background-repeat: no-repeat;
      }

      &.bgdonghua::before {
        animation: rotating 14s linear infinite;
      }
    }

    &.item-lan {
      color: #00fdfa;
      .user_Overview_nums {
        text-shadow: 0 0 10px rgba(0, 253, 250, 0.8);
      }
      .allnum::before {
        background-image: url("@/assets/img/left_top_lan.png");
        filter: drop-shadow(0 0 8px rgba(0, 253, 250, 0.5));
      }
    }

    &.item-lv {
      color: #07f7a8;
      .user_Overview_nums {
        text-shadow: 0 0 10px rgba(7, 247, 168, 0.8);
      }
      .online::before {
        background-image: url("@/assets/img/left_top_lv.png");
        filter: drop-shadow(0 0 8px rgba(7, 247, 168, 0.5));
      }
    }

    &.item-huang {
      color: #ffd04b;
      .user_Overview_nums {
        text-shadow: 0 0 10px rgba(255, 208, 75, 0.8);
      }
      .offline::before {
        background-image: url("@/assets/img/left_top_huang.png");
        filter: drop-shadow(0 0 8px rgba(255, 208, 75, 0.5));
      }
    }

    &.item-hong {
      color: #ff3366;
      .user_Overview_nums {
        text-shadow: 0 0 10px rgba(255, 51, 102, 0.8);
      }
      .laramnum::before {
        background-image: url("@/assets/img/left_top_hong.png");
        filter: drop-shadow(0 0 8px rgba(255, 51, 102, 0.6));
      }
    }
  }
}
</style>
