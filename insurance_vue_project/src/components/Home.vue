<template>
  <el-container class="home-container">
   <!-- 头部区域 -->
  <el-header>
      <div>
          <img src="../assets/logo.png" alt="">
          <span>保单</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
  </el-header>
  <el-container>
      <!-- 侧边栏 -->
    <el-aside :width="isCollapse ? '64px' : '200px'">
    <div class="toggle-button" @click="toggleCollapse">
      |||
    </div>
    <el-menu background-color="#333744"
    text-color="#fff" active-text-color="#409EFF"
    :unique-opened="true" :collapse="isCollapse"
    :collapse-transition="false" :router="true"
    :default-active="activePath">
      <!-- <el-menu-item  :index="'/' + item" v-for="item in menulist" :key="item.id">
        <i :class="iconsObj[103]"></i>
        <span> {{ item }} </span>
      </el-menu-item> -->
      <el-menu-item  :index="'/rights'">
        <i :class="iconsObj[108]"></i>
        <span> 保单列表 </span>
      </el-menu-item>
      <el-menu-item  :index="'/roles'">
        <i :class="iconsObj[103]"></i>
        <span> 历史数据 </span>
      </el-menu-item>
    </el-menu>
    </el-aside>

    <!-- 右侧主区域 -->
    <el-main>
        <router-view></router-view>
    </el-main>
  </el-container>
  </el-container>
</template>

<script>
export default {
  // 数据存储
  data () {
    return {
      menulist: [],
      // 图标数据
      iconsObj: {
        108: ' el-icon-user ',
        103: ' el-icon-help',
        101: ' el-icon-goods',
        102: ' el-icon-s-claim',
        145: ' el-icon-menu'
      },
      isCollapse: false,
      activePath: ''
    }
  },

  // 加载时调用
  created () {
    this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },

  // 函数功能
  methods: {
    logout () {
      // 退出登录
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // 获取所有菜单
    async getMenuList () {
      // const { data: res } = await this.$http.get('historyForm/' + window.sessionStorage.getItem('login_token'))
      // if (res.status !== 200) return this.$message.error(res.meta.msg)
    },
    // 菜单折叠
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    },
    // 保存激活高亮区域
    saveMavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    }
  }
}
</script>

<style lang='less' scoped>
.home-container {
    height: 100%;
}

.el-header {
    background-color: aqua;
    display: flex;
    justify-content: space-between;
    padding-left: 0;
    align-items: center;
    color: #fff;
    font-size: 20px;
    > div {
        display: flex;
        align-items: center;
        span {
            margin-left: 15px;
        }
    }
}

.el-aside{
    background-color: #333744;
    .el-menu {
      border-right: none;
    }
}

.el-main {
    background-color: #fff;
}

img {
    width: 45px;
    height: 45px;
    border-left: 20px;
}

i{
  margin-right: 10px;
}

.toggle-button {
  background-color: aqua;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}
</style>
