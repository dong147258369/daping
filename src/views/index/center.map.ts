//mapData数据结构
export interface MapdataType {
  name: string;
  value: [number, number, number]; //x,y,value  第一个x 第二个y  第三个value
}
export const optionHandle = (regionCode: string, list: object[], mapData: MapdataType[]) => {
  let top = 45;
  let zoom = ["china"].includes(regionCode) ? 1.05 : 1;

  // 构建全国远程医疗支援飞线
  const linesData: any[] = [];
  if (["china"].includes(regionCode) && mapData.length > 1) {
    const hub = mapData.find((m) => m.name.includes("北京") || m.name.includes("四川")) || mapData[0];
    mapData.forEach((item) => {
      if (item.name !== hub.name) {
        linesData.push({
          fromName: hub.name,
          toName: item.name,
          coords: [
            [hub.value[0], hub.value[1]],
            [item.value[0], item.value[1]],
          ],
        });
      }
    });
  }

  return {
    backgroundColor: "rgba(0,0,0,0)",
    tooltip: {
      show: false,
    },
    legend: {
      show: false,
    },
    visualMap: {
      seriesIndex: 0,
      left: 20,
      bottom: 20,
      pieces: [
        { gte: 1000, label: "1000家以上" },
        { gte: 600, lte: 999, label: "600-999家" },
        { gte: 200, lte: 599, label: "200-599家" },
        { gte: 50, lte: 199, label: "50-199家" },
        { gte: 10, lte: 49, label: "10-49家" },
        { lte: 9, label: "1-9家" },
      ],
      inRange: {
        color: [
          "rgba(20, 50, 100, 0.6)",
          "rgba(14, 85, 150, 0.75)",
          "rgba(22, 120, 200, 0.85)",
          "rgba(0, 180, 240, 0.85)",
          "rgba(0, 230, 255, 0.9)",
          "rgba(80, 255, 230, 0.95)",
        ],
      },
      textStyle: {
        color: "#fff",
      },
    },
    geo: [
      {
        map: regionCode,
        roam: false,
        selectedMode: false,
        zoom: zoom,
        top: top,
        aspectScale: 0.78,
        show: false,
      },
    ],
    series: [
      // 基础地图
      {
        name: "MAP",
        type: "map",
        map: regionCode,
        aspectScale: 0.78,
        data: list,
        showLegendSymbol: false,
        selectedMode: false,
        zoom: zoom,
        geoIndex: 2,
        top: top,
        tooltip: {
          show: true,
          formatter: function (params: any) {
            if (params.data) {
              return params.name + " 协作医院：" + params.data["value"] + " 家";
            } else {
              return params.name;
            }
          },
          backgroundColor: "rgba(10, 24, 52, 0.9)",
          borderColor: "#00f7f6",
          borderWidth: 1,
          textStyle: {
            color: "#FFF",
          },
        },
        label: {
          color: "#e2e8f0",
          formatter: function (val: any) {
            if (val.data !== undefined) {
              return val.name.slice(0, 2);
            } else {
              return "";
            }
          },
          rich: {},
        },
        emphasis: {
          show: false,
          label: {
            show: true,
            color: "#00f7f6",
            fontWeight: "bold",
          },
          itemStyle: {
            areaColor: "rgba(0, 242, 254, 0.4)",
            borderColor: "#00f7f6",
            borderWidth: 2,
            shadowColor: "rgba(0, 242, 254, 0.8)",
            shadowBlur: 15,
          },
        },
        itemStyle: {
          borderColor: "rgba(0, 247, 246, 0.6)",
          borderWidth: 1.2,
          areaColor: "rgba(15, 38, 77, 0.6)",
          shadowColor: "rgba(0, 180, 255, 0.35)",
          shadowOffsetX: -2,
          shadowOffsetY: 4,
          shadowBlur: 12,
        },
      },
      // 远程医疗飞线流光
      {
        type: "lines",
        coordinateSystem: "geo",
        zlevel: 3,
        effect: {
          show: true,
          period: 4.5,
          trailLength: 0.3,
          color: "#00F7F6",
          symbol: "arrow",
          symbolSize: 6,
        },
        lineStyle: {
          color: "rgba(0, 247, 246, 0.35)",
          width: 1.5,
          opacity: 0.6,
          curveness: 0.25,
        },
        data: linesData,
        silent: true,
      },
      // 协作医院核心发光辐射散点
      {
        data: mapData,
        type: "effectScatter",
        coordinateSystem: "geo",
        zlevel: 4,
        symbolSize: function (val: any) {
          return Math.max(6, Math.min(14, (val[2] || 100) / 90));
        },
        legendHoverLink: true,
        showEffectOn: "render",
        rippleEffect: {
          period: 3.5,
          scale: 4.5,
          color: "#00FFFF",
          brushType: "stroke",
        },
        tooltip: {
          show: true,
          formatter: function (params: any) {
            if (params.data) {
              return params.name + " 协作医院：" + params.data["value"][2] + " 家";
            } else {
              return params.name;
            }
          },
          backgroundColor: "rgba(10, 24, 52, 0.9)",
          borderColor: "#00f7f6",
          borderWidth: 1,
          textStyle: {
            color: "#FFF",
          },
        },
        label: {
          formatter: (param: any) => {
            return param.name.slice(0, 2);
          },
          fontSize: 11,
          offset: [0, 4],
          position: "bottom",
          textBorderColor: "#051124",
          textBorderWidth: 2,
          color: "#00FFFF",
          fontWeight: "600",
          show: true,
        },
        itemStyle: {
          color: "#00F7F6",
          borderColor: "#FFFFFF",
          borderWidth: 2,
          shadowColor: "#00FFFF",
          shadowBlur: 14,
        },
      },
    ],
  };
};

export const regionCodes: any = {
  中国: {
    adcode: "100000",
    level: "country",
    name: "中华人民共和国",
  },
  新疆维吾尔自治区: {
    adcode: "650000",
    level: "province",
    name: "新疆维吾尔自治区",
  },
  湖北省: {
    adcode: "420000",
    level: "province",
    name: "湖北省",
  },
  辽宁省: {
    adcode: "210000",
    level: "province",
    name: "辽宁省",
  },
  广东省: {
    adcode: "440000",
    level: "province",
    name: "广东省",
  },
  内蒙古自治区: {
    adcode: "150000",
    level: "province",
    name: "内蒙古自治区",
  },
  黑龙江省: {
    adcode: "230000",
    level: "province",
    name: "黑龙江省",
  },
  河南省: {
    adcode: "410000",
    level: "province",
    name: "河南省",
  },
  山东省: {
    adcode: "370000",
    level: "province",
    name: "山东省",
  },
  陕西省: {
    adcode: "610000",
    level: "province",
    name: "陕西省",
  },
  贵州省: {
    adcode: "520000",
    level: "province",
    name: "贵州省",
  },
  上海市: {
    adcode: "310000",
    level: "province",
    name: "上海市",
  },
  重庆市: {
    adcode: "500000",
    level: "province",
    name: "重庆市",
  },
  西藏自治区: {
    adcode: "540000",
    level: "province",
    name: "西藏自治区",
  },
  安徽省: {
    adcode: "340000",
    level: "province",
    name: "安徽省",
  },
  福建省: {
    adcode: "350000",
    level: "province",
    name: "福建省",
  },
  湖南省: {
    adcode: "430000",
    level: "province",
    name: "湖南省",
  },
  海南省: {
    adcode: "460000",
    level: "province",
    name: "海南省",
  },
  江苏省: {
    adcode: "320000",
    level: "province",
    name: "江苏省",
  },
  青海省: {
    adcode: "630000",
    level: "province",
    name: "青海省",
  },
  广西壮族自治区: {
    adcode: "450000",
    level: "province",
    name: "广西壮族自治区",
  },
  宁夏回族自治区: {
    adcode: "640000",
    level: "province",
    name: "宁夏回族自治区",
  },
  浙江省: {
    adcode: "330000",
    level: "province",
    name: "浙江省",
  },
  河北省: {
    adcode: "130000",
    level: "province",
    name: "河北省",
  },
  香港特别行政区: {
    adcode: "810000",
    level: "province",
    name: "香港特别行政区",
  },
  台湾省: {
    adcode: "710000",
    level: "province",
    name: "台湾省",
  },
  澳门特别行政区: {
    adcode: "820000",
    level: "province",
    name: "澳门特别行政区",
  },
  甘肃省: {
    adcode: "620000",
    level: "province",
    name: "甘肃省",
  },
  四川省: {
    adcode: "510000",
    level: "province",
    name: "四川省",
  },
  天津市: {
    adcode: "120000",
    level: "province",
    name: "天津市",
  },
  江西省: {
    adcode: "360000",
    level: "province",
    name: "江西省",
  },
  云南省: {
    adcode: "530000",
    level: "province",
    name: "云南省",
  },
  山西省: {
    adcode: "140000",
    level: "province",
    name: "山西省",
  },
  北京市: {
    adcode: "110000",
    level: "province",
    name: "北京市",
  },
  吉林省: {
    adcode: "220000",
    level: "province",
    name: "吉林省",
  },
};
