<template>
    <div>
    <!-- 面包屑导航 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
    <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item><a @click="getformda(0)">福佑金生年金保险</a></el-breadcrumb-item>
    <el-breadcrumb-item><a @click="getformda(1)">太平财富智赢年金保险+荣耀金账户终身寿险</a></el-breadcrumb-item>
    <el-breadcrumb-item><a @click="getformda(2)">珍爱宝贝教育年金保险计划</a></el-breadcrumb-item>
    <el-breadcrumb-item></el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 级联选择器 -->
    <el-cascader
    v-model="value"
    size="medium"
    :options="options"
    :props="{ expandTrigger: 'hover' }"
    @change="handleChange"></el-cascader>

    <!-- 标签栏 -->
    <el-card v-if="this.fyjx">
        <!-- 表单 -->
        <h1 align="center">福佑金生年金保险</h1>
        <h4>1. 用户拥有权力</h4>
        <h5 v-for="item in this.fyj.equity" :key="item">{{item}}</h5>
        <h4>2. 投保须知</h4>
        <h5 v-for="item in this.fyj.notice" :key="item">{{item}}</h5>
        <img class="images" v-for="item in this.fyj.image_url" :key="item" :src="item" alt="获取图片失败!">
        <h4>表单</h4>
        <el-form ref="fyjsizeForm" :model="fyjsizeForm" label-width="150px" size="mini">
          <el-form-item label="性别">
            <el-select v-model="fyjsizeForm.sex" placeholder="请选择">
              <el-option value="男"></el-option>
              <el-option value="女"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="承保职业">
            <el-form-item label="1-6类"></el-form-item>
          </el-form-item>
          <el-form-item label="保障期限">
            <el-select v-model="fyjsizeForm.insurantDateLimit" placeholder="请选择">
              <el-option value="10年"></el-option>
              <el-option value="15年"></el-option>
              <el-option value="20年"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="缴费类型">
            <el-select v-model="fyjsizeForm.paymentType" placeholder="请选择">
              <el-option value="一次性"></el-option>
              <el-option value="年交"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="缴费年限">
            <el-select v-model="fyjsizeForm.insureAgeLimit" placeholder="请选择">
              <el-option value="趸交"></el-option>
              <el-option value="3年"></el-option>
              <el-option value="5年"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="保费">
            <el-input v-model="fyjsizeForm.premium"></el-input>
            <p>最大10000000元，需为1000的倍数</p>
          </el-form-item>
          <el-form-item label="投保地区">
            <el-form-item label="海南省"></el-form-item>
          </el-form-item>
          <!-- 提交按钮 -->
          <el-form-item>
            <el-button type="primary" @click="onSubmit(0)" :disabled="this.fyjxbo">{{this.fyjxtext}}</el-button>
          </el-form-item>
        </el-form>
    </el-card>

    <el-card v-if="this.tpyx">
        <!-- 表单 -->
        <h1  align="center">太平财富智赢年金保险+荣耀金账户终身寿险</h1>
        <h4>1. 用户拥有权力</h4>
        <h5 v-for="item in this.tpy.equity" :key="item">{{item}}</h5>
        <h4>2. 投保须知</h4>
        <h5 v-for="item in this.tpy.notice" :key="item">{{item}}</h5>
        <img v-for="item in this.tpy.image_url" :key="item" :src="item" alt="获取图片失败!">
        <h4>表单</h4>
        <el-form ref="tpysizeForm" :model="tpysizeForm" label-width="150px" size="mini">
          <el-form-item label="性别">
            <el-select v-model="tpysizeForm.sex" placeholder="请选择">
              <el-option value="男"></el-option>
              <el-option value="女"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="承保职业">
            <el-form-item label="1-6类"></el-form-item>
          </el-form-item>
          <el-form-item label="保障期限">
            <el-form-item label="10"></el-form-item>
          </el-form-item>
          <el-form-item label="缴费类型">
            <el-form-item label="年交"></el-form-item>
          </el-form-item>
          <el-form-item label="缴费年限">
            <el-select v-model="tpysizeForm.insureAgeLimit" placeholder="请选择">
              <el-option value="3年"></el-option>
              <el-option value="5年"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="年交保费">
            <el-select v-model="tpysizeForm.premium" placeholder="请选择">
              <el-option v-for="item in (50, 100)" :value="item*1000" :key="item">{{item*1000}}元</el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="荣耀金万能账户">
            <el-select v-model="tpysizeForm.isInsure" placeholder="请选择">
              <el-option value="不含"></el-option>
              <el-option value="含"></el-option>
            </el-select>
          </el-form-item>
          <!-- 提交按钮 -->
          <el-form-item>
            <el-button type="primary" @click="onSubmit(1)" :disabled="this.tpyxbo">{{tpyxtext}}</el-button>
          </el-form-item>
        </el-form>
    </el-card>

    <el-card v-if="this.zabbx">
        <h1  align="center">珍爱宝贝教育年金保险计划</h1>
        <h4>1. 用户拥有权力</h4>
        <!-- 表单 -->
        <h5 v-for="item in this.zabb.equity" :key="item">{{item}}</h5>
        <h4>2. 投保须知</h4>
        <h5 v-for="item in this.zabb.notice" :key="item">{{item}}</h5>
        <img class="images"  v-for="item in this.zabb.image_url" :key="item" :src="item" alt="获取图片失败!">
        <h4>表单</h4>
        <el-form ref="zabbsizeForm" :model="zabbsizeForm" label-width="150px" size="mini">
          <el-form-item label="投保人保费豁免">
            <el-select v-model="zabbsizeForm.policyholderExemption" placeholder="请选择">
              <el-option value="不含"></el-option>
              <el-option value="含"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="投保人保费豁免缴费年限">
            <el-select v-model="zabbsizeForm.additionalInsureAgeLimit" placeholder="请选择">
              <el-option value="不投保"></el-option>
              <el-option value="5年"></el-option>
              <el-option value="10年"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="投保人性别">
            <el-select v-model="zabbsizeForm.vesterSex" placeholder="请选择">
              <el-option value="男"></el-option>
              <el-option value="女"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="被保险人性别">
            <el-select v-model="zabbsizeForm.sex" placeholder="请选择">
              <el-option value="男"></el-option>
              <el-option value="女"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="投保地区">
            <el-select v-model="zabbsizeForm.province" placeholder="请选择">
              <el-option value="北京市"></el-option>
              <el-option value="福建省"></el-option>
              <el-option value="广东省"></el-option>
              <el-option value="河南省"></el-option>
              <el-option value="湖北省"></el-option>
              <el-option value="湖南省"></el-option>
              <el-option value="江苏省"></el-option>
              <el-option value="江西省"></el-option>
              <el-option value="辽宁省"></el-option>
              <el-option value="山东省"></el-option>
              <el-option value="陕西省"></el-option>
              <el-option value="上海市"></el-option>
              <el-option value="四川省"></el-option>
              <el-option value="天津市"></el-option>
              <el-option value="浙江省"></el-option>
              <el-option value="重庆市"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="基本保额">
            <el-select v-model="zabbsizeForm.leastamount" placeholder="请选择">
              <el-option v-for="item in 50" :value="item+'万元'" :key="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="保障期限">
            <el-form-item label="至25岁"></el-form-item>
          </el-form-item>
          <el-form-item label="缴费年限">
            <el-select v-model="zabbsizeForm.insureAgeLimit" placeholder="请选择">
              <el-option value="5年"></el-option>
              <el-option value="10年"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="缴费类型">
            <el-form-item label="年交"></el-form-item>
          </el-form-item>
          <el-form-item label="高中大学教育年金保额">
            <el-form-item label="不投保"></el-form-item>
          </el-form-item>
          <el-form-item label="重大疾病保险保额">
            <el-select v-model="zabbsizeForm.seriousIllness" placeholder="请选择">
              <el-option value="不投保"></el-option>
              <el-option v-for="item in 50" :value="item+'万元'" :key="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="长期住院津贴保额">
            <el-select v-model="zabbsizeForm.hospitalAllowance" placeholder="请选择">
              <el-option value="不投保"></el-option>
              <el-option v-for="item in 3" :value="item*50+'元'" :key="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="长期意外伤害医疗保险保额">
            <el-select v-model="zabbsizeForm.accidentalInjury" placeholder="请选择">
              <el-option value="不投保"></el-option>
              <el-option v-for="item in 4" :value="item*5000+'元'" :key="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="臻爱定期寿险保额">
            <el-select v-model="zabbsizeForm.regular" placeholder="请选择">
              <el-option value="不投保"></el-option>
              <el-option v-for="item in 6" :value="item*5+'万元'" :key="item"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="高中大学教育年金保障期限">
            <el-form-item label="至21"></el-form-item>
          </el-form-item>
          <!-- 提交按钮 -->
          <el-form-item>
            <el-button type="primary" @click="onSubmit(2)" :disabled="this.zabbxbo">{{zabbxtext}}</el-button>
          </el-form-item>
        </el-form>
    </el-card>

    </div>
</template>

<script>
export default {
  data () {
    return {
      fyjxbo: false,
      tpyxbo: false,
      zabbxbo: false,
      fyjxtext: '提交',
      tpyxtext: '提交',
      zabbxtext: '提交',
      fyjx: false,
      tpyx: false,
      zabbx: false,
      value: [],
      options: [
        {
          value: 'haibao',
          label: '海保人寿',
          children: [{
            value: '0',
            label: '成人保险'
          }]
        }, {
          value: 'taiping',
          label: '太平人寿 ',
          children: [{
            value: '1',
            label: '养老年金'
          }]
        }, {
          value: 'zhaoshang',
          label: '招商信诺',
          children: [{
            value: '2',
            label: '儿童保险'
          }]
        }
      ],
      // fyj表单
      fyjsizeForm: {
        sex: '',
        insurantJob: '1-6类',
        insurantDateLimit: '',
        paymentType: '',
        insureAgeLimit: '',
        premium: '',
        coverageAreaName: '海南省'
      },
      // tpy表单
      tpysizeForm: {
        sex: '',
        insurantJob: '1-6类',
        insurantDateLimit: '10',
        paymentType: '年交',
        insureAgeLimit: '',
        premium: '',
        isInsure: ''
      },
      // zabb表单
      zabbsizeForm: {
        policyholderExemption: '',
        additionalInsureAgeLimit: '',
        vesterSex: '',
        sex: '',
        province: '',
        leastamount: '',
        insurantDateLimit: '至25岁',
        insureAgeLimit: '',
        paymentType: '年交',
        seniorUniversityEdu: '不投保',
        seriousIllness: '',
        hospitalAllowance: '',
        accidentalInjury: '',
        regular: '',
        additionalRiskPeriod: '至21'
      },
      // 获取表单列表
      rightsList: [],
      fyj: [],
      tpy: [],
      zabb: [],
      // 提交数据
      numberValidateForm: [],
      rolelist: [],
      fyjlist: [],
      tpylist: [],
      zabblist: []
    }
  },
  async created () {
    this.getformda(0)
    this.getformda(1)
    this.getformda(2)
    const { data: res } = await this.$http.get('historyForm/' + window.sessionStorage.getItem('login_token'))
    if (res.status === 402) return this.$message.success('登录过期,请重新登录!')
    if (res.status !== 200) {
      return this.$message.error('获取历史数据错误, 请稍后尝试!')
    }
    this.rolelist = JSON.parse(JSON.stringify(res.message))
    this.fyjlist = JSON.parse(this.rolelist[0])
    this.tpylist = JSON.parse(this.rolelist[1])
    this.zabblist = JSON.parse(this.rolelist[2])
    if (this.fyjlist != null) {
      this.fyjxtext = '已提交'
      this.fyjxbo = true
    } if (this.tpylist != null) {
      this.tpyxtext = '已提交'
      this.tpyxbo = true
    } if (this.zabblist != null) {
      this.zabbxtext = '已提交'
      this.zabbxbo = true
    }
  },
  methods: {
    // 获取保险
    async getformda (id) {
      if (id === 0) {
        const { data: res } = await this.$http.get('commitForm/' + id + '/' + window.sessionStorage.getItem('login_token'))
        if (res.status === 201) return this.$message.success(res.message)
        if (res.status !== 200) return this.$message.error('获取保单数据失败, 请稍后尝试!')
        this.fyj = JSON.parse(JSON.parse(JSON.stringify(res.message)))
      } else if (id === 1) {
        const { data: res } = await this.$http.get('commitForm/' + id + '/' + window.sessionStorage.getItem('login_token'))
        if (res.status === 201) return this.$message.success(res.message)
        if (res.status !== 200) return this.$message.error('获取保单数据失败, 请稍后尝试!')
        this.tpy = JSON.parse(JSON.parse(JSON.stringify(res.message)))
      } else if (id === 2) {
        const { data: res } = await this.$http.get('commitForm/' + id + '/' + window.sessionStorage.getItem('login_token'))
        if (res.status === 201) return this.$message.success(res.message)
        if (res.status !== 200) return this.$message.error('获取保单数据失败, 请稍后尝试!')
        this.zabb = JSON.parse(JSON.parse(JSON.stringify(res.message)))
      }
    },
    // 提交数据
    async onSubmit (nameId) {
      var dataf
      if (nameId === 0) dataf = this.fyjsizeForm
      else if (nameId === 1) dataf = this.tpysizeForm
      else if (nameId === 2) dataf = this.zabbsizeForm
      for (var key in dataf) {
        if (dataf[key] == null || dataf[key] === '') return this.$message.success('值不能为空!')
      }
      const { data: res } = await this.$http.post('dataForm/' + nameId + '/' + window.sessionStorage.getItem('login_token'), dataf)
      if (res.status !== 200) return this.$message.error(res.message)
      this.$message.success(res.message)
    },
    handleChange () {
      console.log(this.value)
      if (this.value[1] === '0') {
        this.fyjx = true
        this.tpyx = false
        this.zabbx = false
      } else if (this.value[1] === '1') {
        this.fyjx = false
        this.tpyx = true
        this.zabbx = false
      } else if (this.value[1] === '2') {
        this.fyjx = false
        this.tpyx = false
        this.zabbx = true
      }
    }
  }
}

</script>

<style lang="less" scoped>
.el-card {
  margin-bottom: 20px;
}
.el-input {
  width: 200px;
}
.el-card {
  margin-top: 20px;
}
</style>
