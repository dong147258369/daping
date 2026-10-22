<script setup lang="ts">
import ItemWrap from "@/components/item-wrap";
import LeftTop from "./left-top.vue";
import LeftCenter from "./left-center.vue";
import LeftBottom from "./left-bottom.vue";
import CenterMap from "./center-map.vue";
import CenterBottom from "./center-bottom.vue";
import RightTop from "./right-top.vue";
import RightCenter from "./right-center.vue";
import RightBottom from "./right-bottom.vue";
</script>

<template>
  <div class="index-box">
    <div class="contetn_left">
      <!-- <div class="pagetab">
        <div class="item">实时监测</div>
        <div class="item">统计分析</div>
      </div> -->
      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="急救通道与出车动态"
        style="padding: 0 10px 16px 10px"
      >
        <LeftBottom />
      </ItemWrap>
      <ItemWrap class="contetn_left-top contetn_lr-item" title="医疗设备运行监控">
        <LeftTop />
      </ItemWrap>
      <ItemWrap class="contetn_left-center contetn_lr-item" title="患者就诊分类态势">
        <LeftCenter />
      </ItemWrap>
    </div>
    <div class="contetn_center">
      <CenterMap class="contetn_center_top" title="医联体与医疗协作网" />
      <ItemWrap class="contetn_center-bottom" title="重点科室床位使用率">
        <CenterBottom />
      </ItemWrap>
    </div>
    <div class="contetn_right">
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="重症监护危急值预警">
        <RightBottom />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="门急诊与危急值走势">
        <RightTop />
      </ItemWrap>
      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="科室就诊负荷(TOP8)"
        style="padding: 0 10px 16px 10px"
      >
        <RightCenter />
      </ItemWrap>
    </div>
  </div>
</template>

<style scoped lang="scss">
.index-box {
  width: 100%;
  display: flex;
  min-height: calc(100% - 64px);
  justify-content: space-between;
}
//左边 右边 结构一样
.contetn_left,
.contetn_right {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  width: 540px;
  box-sizing: border-box;
  flex-shrink: 0;
}
.contetn_center {
  flex: 1;
  margin: 0 54px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  .contetn_center-bottom {
    height: 315px;
  }
}

.contetn_lr-item {
  height: 310px;
}
</style>
