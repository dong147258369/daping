import Mock from "mockjs";
//处理路径传参
import { parameteUrl } from "@/utils/query-param";

function ArrSet(Arr: any[], id: string): any[] {
  let obj: any = {};
  const arrays = Arr.reduce((setArr, item) => {
    obj[item[id]] ? "" : (obj[item[id]] = true && setArr.push(item));
    return setArr;
  }, []);
  return arrays;
}

/**
 * @description: min ≤ r ≤ max 随机数
 */
function RandomNumBoth(Min: any, Max: any) {
  var Range = Max - Min;
  var Rand = Math.random();
  var num = Min + Math.round(Rand * Range);
  return num;
}

// 智慧医疗科室与专科定义
const medicalDepartments = [
  "心血管内科",
  "急诊医学中心",
  "重症医学科(ICU)",
  "神经外科",
  "呼吸与危重症科",
  "骨科创伤中心",
  "普通外科",
  "消化内科",
  "胸心外科",
  "妇产重症中心",
  "儿科重症病房(PICU)",
  "神经内科",
  "肾病透析中心",
  "肿瘤中心",
  "血液内科",
  "感染控制科"
];

// 医疗设备类型
const deviceTypes = [
  "多参数生理监护仪",
  "无创/有创呼吸机",
  "床旁血滤CRRT机",
  "全自动体外除颤仪",
  "体外膜肺氧合(ECMO)",
  "智能输液泵",
  "便携式超声诊断仪",
  "血气生化分析仪"
];

// 危急值与医疗警报类型
const alertCases = [
  { name: "持续低氧血症报警", detail: "SpO2跌至81%，伴随呼吸窘迫", value: "81%" },
  { name: "恶性室性心动过速", detail: "HR飙升至162bpm，室速律", value: "162bpm" },
  { name: "重度高钾血症危急值", detail: "血清钾检测值为6.9mmol/L", value: "6.9mmol/L" },
  { name: "高敏肌钙蛋白超标", detail: "TnI值达到18.6ng/mL，提示心梗", value: "18.6ng/mL" },
  { name: "气道峰压过高告警", detail: "呼吸机气道峰压达到45cmH2O", value: "45cmH2O" },
  { name: "急性严重酸中毒", detail: "动脉血pH值低至7.12，高乳酸", value: "pH 7.12" },
  { name: "严重低血糖危急值", detail: "微量血糖检测值为1.8mmol/L", value: "1.8mmol/L" },
  { name: "重度心动过缓预警", detail: "HR降至38bpm，房室阻滞", value: "38bpm" }
];

// 急救出车事件与专科通道
const emergencyChannels = [
  "胸痛绿色通道",
  "卒中中心急救",
  "多发创伤抢救",
  "危重孕产妇救治",
  "儿科危急重症",
  "呼吸衰竭急救",
  "急性消化道大出血",
  "心搏骤停CPR转运"
];

const hospitalBranches = [
  "总院区·急诊抢救中心",
  "东院区·胸痛救治部",
  "西院区·创伤急救中心",
  "南院区·综合ICU",
  "国际医疗部·急诊科",
  "儿童医学中心·PICU",
  "心血管病医院·CCU",
  "脑科医院·神经重症"
];

export default [
  // 左中：患者就诊分类态势（门急诊、普通住院、重症监护、危急病患）
  {
    url: "/bigscreen/countUserNum",
    type: "get",
    response: () => {
      const offlineNum = RandomNumBoth(950, 1150); // 普通住院
      const lockNum = RandomNumBoth(320, 430);     // 重症监护
      const alarmNum = RandomNumBoth(90, 160);     // 危急病患
      const totalNum = 3860;
      const onlineNum = totalNum - offlineNum - lockNum - alarmNum; // 门急诊

      return {
        success: true,
        data: {
          offlineNum,
          alarmNum,
          lockNum,
          totalNum,
          onlineNum
        }
      };
    }
  },

  // 左上：医疗设备运行监控（设备总数、在用正常、维护停机、质控预警）
  {
    url: "/bigscreen/countDeviceNum",
    type: "get",
    response: () => {
      const totalNum = 3680;
      const offlineNum = RandomNumBoth(40, 95);  // 检修停机
      const alarmNum = RandomNumBoth(18, 55);    // 质控告警
      const onlineNum = totalNum - offlineNum;   // 正常在用

      return {
        success: true,
        data: {
          totalNum,
          offlineNum,
          alarmNum,
          onlineNum
        }
      };
    }
  },

  // 左下：急救通道与出车动态（救护车号、时间、状态、急救专科/院区地点）
  {
    url: "/bigscreen/leftBottom",
    type: "get",
    response: () => {
      const list = [];
      const prefixes = ["粤A·", "粤B·", "京A·", "沪A·", "川A·", "鄂A·", "浙A·", "苏A·"];
      for (let i = 0; i < 20; i++) {
        const prefix = prefixes[i % prefixes.length];
        const carNo = prefix + (1000 + RandomNumBoth(100, 8999));
        const channel = emergencyChannels[i % emergencyChannels.length];
        const hospital = hospitalBranches[i % hospitalBranches.length];
        const onlineState = Math.random() > 0.4 ? 1 : 0; // 1: 已送达/接诊中, 0: 紧急转运中

        list.push({
          provinceName: hospital.split("·")[0],
          cityName: hospital.split("·")[1],
          countyName: channel,
          createTime: Mock.mock("@datetime('yyyy-MM-dd HH:mm:ss')"),
          deviceId: carNo,
          gatewayno: carNo,
          onlineState: onlineState
        });
      }
      return {
        success: true,
        data: { list }
      };
    }
  },

  // 右上：门急诊接诊与危急值走势
  {
    url: "/bigscreen/alarmNum",
    type: "get",
    response: () => {
      return {
        success: true,
        data: {
          dateList: ["02:00", "06:00", "10:00", "14:00", "18:00", "22:00"],
          numList: [680, 520, 1680, 1890, 1420, 980],  // 急诊接诊人次
          numList2: [45, 32, 128, 145, 112, 76]        // 危急值上报数
        }
      };
    }
  },

  // 右中：重点科室就诊负荷TOP8
  {
    url: "/bigscreen/ranking",
    type: "get",
    response: () => {
      const topDepts = [
        { name: "心血管内科", value: 1680 },
        { name: "急诊医学中心", value: 1540 },
        { name: "呼吸危重症科", value: 1390 },
        { name: "神经外科中心", value: 1260 },
        { name: "骨科关节病区", value: 1120 },
        { name: "重症医学(ICU)", value: 980 },
        { name: "儿科重症中心", value: 870 },
        { name: "消化内科病房", value: 760 }
      ];
      return {
        success: true,
        data: topDepts
      };
    }
  },

  // 右下：重症监护危急值实时预警记录
  {
    url: "/bigscreen/rightBottom",
    type: "get",
    response: () => {
      const list = [];
      const beds = [
        "ICU-02", "ICU-07", "CCU-05", "急救-01", "急救-04",
        "NICU-03", "PICU-02", "RICU-06", "神外ICU-08", "EICU-11"
      ];

      for (let i = 0; i < 30; i++) {
        const alertCase = alertCases[i % alertCases.length];
        const dept = medicalDepartments[i % medicalDepartments.length];
        const device = deviceTypes[i % deviceTypes.length];
        const bed = beds[i % beds.length];
        const branch = hospitalBranches[i % hospitalBranches.length];

        list.push({
          alertdetail: alertCase.detail,
          alertname: alertCase.name,
          alertvalue: alertCase.value,
          createtime: Mock.mock("@datetime('yyyy-MM-dd HH:mm:ss')"),
          deviceid: null,
          gatewayno: `床位: ${bed}`,
          phase: "紧急",
          sbInfo: `${dept} - ${device}`,
          terminalno: device,
          provinceName: branch.split("·")[0],
          cityName: dept,
          countyName: bed
        });
      }

      return {
        success: true,
        data: { list }
      };
    }
  },

  // 中下：重点科室床位使用率与接诊负荷
  {
    url: "/bigscreen/installationPlan",
    type: "get",
    response: () => {
      const depts = [
        "心血管内科", "急诊ICU", "神经内科", "呼吸重症",
        "骨科中心", "普通外科", "胸外科", "消化内科",
        "妇产科", "儿科重症", "肾内透析", "肿瘤病房"
      ];
      const barData = [186, 114, 152, 138, 164, 142, 98, 126, 110, 88, 92, 135]; // 在用床位
      const lineData = [200, 120, 160, 150, 180, 150, 110, 140, 120, 100, 100, 150]; // 编制床位
      const rateData = barData.map((val, idx) => ((val / lineData[idx]) * 100).toFixed(0)); // 床位使用率%

      return {
        success: true,
        data: {
          category: depts,
          barData,
          lineData,
          rateData
        }
      };
    }
  },

  // 中上：区域医联体与医疗协作网分布
  {
    url: "/bigscreen/centerMap",
    type: "get",
    response: (options: any) => {
      let params = parameteUrl(options.url);
      if (params.regionCode && !["china"].includes(params.regionCode)) {
        const a = Mock.mock({
          success: true,
          data: {
            "dataList|80": [
              {
                name: "@city()",
                value: "@integer(20, 680)"
              }
            ],
            regionCode: params.regionCode
          }
        });
        return a;
      } else {
        const provinces = [
          { name: "北京市", value: 890 },
          { name: "上海市", value: 820 },
          { name: "广东省", value: 1120 },
          { name: "四川省", value: 950 },
          { name: "湖北省", value: 860 },
          { name: "江苏省", value: 980 },
          { name: "浙江省", value: 910 },
          { name: "山东省", value: 870 },
          { name: "河南省", value: 830 },
          { name: "陕西省", value: 760 },
          { name: "湖南省", value: 740 },
          { name: "重庆市", value: 690 },
          { name: "辽宁省", value: 620 },
          { name: "安徽省", value: 580 },
          { name: "福建省", value: 610 }
        ];
        return {
          success: true,
          data: {
            dataList: provinces,
            regionCode: "china"
          }
        };
      }
    }
  }
];
