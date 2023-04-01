<template>
    <div class="login_container">
        <!-- 登录盒子 -->
        <div class="login_box">
            <!-- 头像 -->
            <div class="avatar_box">
                <img src="../assets/logo.png" alt="">
            </div>
            <!-- 表单区域 -->
            <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input v-model="loginForm.username"  prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input type="password" v-model="loginForm.password"  prefix-icon="el-icon-s-claim"></el-input>
                </el-form-item>
                <!-- 按钮 -->
                <el-form-item class="btns">
                    <el-button type="primary" @click="login">登录</el-button>
                    <el-button type="info" @click="resetLoginForm">重置</el-button>
                    <el-button type="primary" @click="setRoleDialogVisible = true">注册</el-button>
                </el-form-item>
            </el-form>
        </div>

        <!-- 注册弹窗 -->
        <el-dialog
          title="注册"
          :visible.sync="setRoleDialogVisible"
          width="50%">
          <div>
            <!-- 表单区域 -->
            <el-form ref="loginFormRef" :model="userform" :rules="loginFormRules" label-width="0px">
                <!-- 用户名 -->
                <el-form-item prop="username">
                    <el-input v-model="userform.username"  prefix-icon="el-icon-user-solid"></el-input>
                </el-form-item>
                <!-- 密码 -->
                <el-form-item prop="password">
                    <el-input type="password" v-model="userform.password"  prefix-icon="el-icon-s-claim"></el-input>
                </el-form-item>
                <!-- 手机号 -->
                <el-form-item prop="mobile">
                    <el-input v-model="userform.mobile"  prefix-icon="el-icon-phone"></el-input>
                </el-form-item>
            </el-form>
          </div>
          <span slot="footer" class="dialog-footer">
            <el-button @click="setRoleDialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="saveuser">确 定</el-button>
          </span>
        </el-dialog>

    </div>
</template>

<script>
export default {
  data () {
    // 自定义手机号验证
    var checkPhone = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('手机号不能为空'))
      } else {
        const reg = /^1[3|4|5|7|8][0-9]\d{8}$/
        console.log(reg.test(value))
        if (reg.test(value)) {
          callback()
        } else {
          return callback(new Error('请输入正确的手机号'))
        }
      }
    }
    return {
      setRoleDialogVisible: false,
      // 登录表单数据
      loginForm: {
        username: '',
        password: ''
      },
      userform: {
        username: '',
        password: '',
        mobile: ''
      },
      // 表单验证规则
      loginFormRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 5, max: 10, message: '长度在5到10个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入登陆密码', trigger: 'blur' },
          { min: 6, max: 15, message: '长度在6到15个字符', trigger: 'blur' }
        ],
        mobile: [
          { validator: checkPhone, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 重置登录表单
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('users/' + this.loginForm.username + '/' + this.loginForm.password)
        if (res.status !== 200) return this.$message.error(res.message)
        this.$message.success(res.message)
        // 1.登录成功将token，保存到客户端的sessionStorage中
        window.sessionStorage.setItem('login_token', res.login_token)
        // 2.跳转后台主页
        this.$router.push('/home', onComplete => { }, onAbort => { })
      })
    },
    // 注册
    async saveuser () {
      const { data: res } = await this.$http.get('zusers/' + this.userform.username + '/' + this.userform.password + '/' + this.userform.mobile)
      if (res.status !== 200) return this.$message.error(res.message)
      this.$message.success(res.message)
      this.setRoleDialogVisible = false
    }
  }
}
</script>

<style long="less" scoped>
.login_container {
    background-color: #85DCF2;
    height: 100%;
}
/* 登录盒子 */
.login_box {
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

/* 头像 */
.avatar_box {
    width: 130px;
    height: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color:  #fff;
}
.avatar_box img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
}

.login_form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
}

.btns {
    display: flex;
    justify-content: flex-end;
}

</style>
