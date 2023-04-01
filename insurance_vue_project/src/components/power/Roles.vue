<template>
    <div>
    <!-- 面包屑导航 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item></el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片试图 -->
    <el-card v-if="fyjlist.length != 0? true: false">
    <!-- 历史列表区域 -->
      <h3>福佑金生年金保险</h3>
      <el-table :data="fyjlist" stripe style="width: 100%">
        <el-table-column prop="username" label="用户名" width="180"></el-table-column>
        <el-table-column prop="sex" label="性别" width="180"> </el-table-column>
        <el-table-column prop="insurantJob" label="承保职业"></el-table-column>
        <el-table-column prop="insurantDateLimit" label="保障期限"></el-table-column>
        <el-table-column prop="paymentType" label="缴费类型"></el-table-column>
        <el-table-column prop="insureAgeLimit" label="缴费年限"></el-table-column>
        <el-table-column prop="premium" label="保费"></el-table-column>
        <el-table-column prop="coverageAreaName" label="投保地区"></el-table-column>
        <el-table-column prop="insurance_money" label="缴费总额"></el-table-column>
      </el-table>
    </el-card>
    <el-card  v-if="tpylist.length != 0? true: false">
      <h3>太平财富智赢年金保险+荣耀金账户终身寿险</h3>
      <el-table :data="tpylist" stripe style="width: 100%">
        <el-table-column prop="username" label="用户名" width="180"></el-table-column>
        <el-table-column prop="sex" label="性别" width="180"> </el-table-column>
        <el-table-column prop="insurantJob" label="承保职业"></el-table-column>
        <el-table-column prop="insurantDateLimit" label="保障期限"></el-table-column>
        <el-table-column prop="paymentType" label="缴费类型"></el-table-column>
        <el-table-column prop="insureAgeLimit" label="缴费年限"></el-table-column>
        <el-table-column prop="premium" label="年交保费"></el-table-column>
        <el-table-column prop="isInsure" label="荣耀金万能账户"></el-table-column>
        <el-table-column prop="insurance_money" label="缴费总额"></el-table-column>
      </el-table>
    </el-card>
    <el-card v-if="zabblist.length != 0? true: false">
      <h3>珍爱宝贝教育年金保险计划</h3>
      <el-table :data="zabblist" stripe style="width: 100%">
        <el-table-column prop="username" label="用户名" width="180"></el-table-column>
        <el-table-column prop="policyholderExemption" label="投保人保费豁免" width="180"></el-table-column>
        <el-table-column prop="additionalInsureAgeLimit" label="投保人保费豁免缴费年限" width="180"> </el-table-column>
        <el-table-column prop="vesterSex" label="投保人性别"></el-table-column>
        <el-table-column prop="sex" label="被保险人性别"></el-table-column>
        <el-table-column prop="province" label="投保地区"></el-table-column>
        <el-table-column prop="leastamount" label="基本保额"></el-table-column>
        <el-table-column prop="insurantDateLimit" label="保障期限"></el-table-column>
        <el-table-column prop="insureAgeLimit" label="缴费年限"></el-table-column>
        <el-table-column prop="paymentType" label="缴费类型"></el-table-column>
        <el-table-column prop="seniorUniversityEdu" label="高中大学教育年金保额"></el-table-column>
        <el-table-column prop="seriousIllness" label="重大疾病保险保额"></el-table-column>
        <el-table-column prop="hospitalAllowance" label="长期住院津贴保额"></el-table-column>
        <el-table-column prop="accidentalInjury" label="长期意外伤害医疗保险保额"></el-table-column>
        <el-table-column prop="regular" label="臻爱定期寿险保额"></el-table-column>
        <el-table-column prop="additionalRiskPeriod" label="高中大学教育年金保障期限"></el-table-column>
        <el-table-column prop="insurance_money" label="缴费总额"></el-table-column>
      </el-table>
    </el-card>
    </div>
</template>

<script>
export default {
  data () {
    return {
      // 历史数据
      rolelist: [],
      setRightDialogVisible: false,
      fyjlist: [],
      tpylist: [],
      zabblist: []
    }
  },
  created () {
    this.getRolesList()
  },
  methods: {
    // 获取历史数据列表
    async getRolesList () {
      const { data: res } = await this.$http.get('historyForm/' + window.sessionStorage.getItem('login_token'))
      if (res.status === 402) return this.$message.success('登录过期,请重新登录!')
      if (res.status !== 200) {
        return this.$message.error('获取历史数据错误, 请稍后尝试!')
      }
      this.rolelist = JSON.parse(JSON.stringify(res.message))
      this.fyjlist = JSON.parse(this.rolelist[0])
      this.tpylist = JSON.parse(this.rolelist[1])
      this.zabblist = JSON.parse(this.rolelist[2])
      console.log(this.fyjlist)
      console.log(this.tpylist)
      console.log(this.zabblist)
    }
  }
}
</script>

<style lang="less" scoped>
.el-tag {
  margin: 7px;
}
.bdtop {
  border-top: 1px solid #eee;
}
.bdbottom {
  border-bottom: 1px solid #eee;
}
.vcenter {
  display: flex;
  align-items: center;
}
.el-card {
  margin-bottom: 20px;
}
</style>
