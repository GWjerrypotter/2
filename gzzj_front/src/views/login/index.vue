<template>
  <div>
    <div class="homepage-hero-module">
      <div class="video-container">
        <div :style="fixStyle" class="filter">
          <div class="title">
            <h1 style="color: #3AB2DA">工作总结系统</h1>
          </div>
          <div class="login">
            <el-form
              ref="loginForm"
              :model="loginForm"
              :rules="loginRules"
              class="login-form"
              label-position="left"
            >
              <el-form-item prop="username" class="logininput">
                <el-input
                  v-model="loginForm.username"
                  name="username"
                  type="text"
                  placeholder="请输入用户名"
                  class="logininput"
                />
              </el-form-item>
              <el-form-item prop="password">
                <el-input
                  type="password"
                  v-model="loginForm.password"
                  class="logininput"
                  name="password"
                  show-password
                  placeholder="请输入密码"
                  @keyup.enter.native="handleLogin"
                />
              </el-form-item>
              <el-form-item>
                <el-button
                  :loading="loading"
                  type="primary"
                  style="width:100%;"
                  @click.native.prevent="handleLogin"
                >登录</el-button>
              </el-form-item>
            </el-form>
            <!-- <el-input v-model="user" placeholder="请输入用户名" style="background-color: transparent"></el-input>
            <el-input type="password" show-password v-model="password" placeholder="请输入密码" @keyup.enter.native="handleLogin"></el-input>
            <el-button type="success" style="width: 300px;margin-top: 30px;" @click.native.prevent="handleLogin">登录</el-button>-->
          </div>
        </div>
        <video :style="fixStyle" autoplay loop class="fillWidth">
          <source src="../../assets/video/Sketch.mp4" type="video/mp4">
        </video>
        <!-- <div class="poster hidden" v-if="!vedioCanPlay">
          <img :style="fixStyle" src="../../assets/img/Magic-Mouse-Scroll.jpg" alt>
        </div>-->
      </div>
    </div>
  </div>
</template>

</style>

<script>
export default {
  name: "Login",
  data() {
    const validatePass = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码不能小于6位'))
      } else {
        callback()
      }
    }
    return {
      fixStyle: "",
      user: "",
      password: "",
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, trigger: 'blur', validator: validatePass }]
      },
      loading: false,
      redirect: undefined
    };
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  mounted() {
    this.startup();
  },
  methods: {
    startup() {
      window.onresize = () => {
        const windowWidth = document.body.clientWidth;
        const windowHeight = document.body.clientHeight;
        const windowAspectRatio = windowHeight / windowWidth;
        let videoWidth;
        let videoHeight;
        if (windowAspectRatio < 0.5625) {
          videoWidth = windowWidth;
          videoHeight = videoWidth * 0.5625;
          this.fixStyle = {
            height: windowWidth * 0.5625 + "px",
            width: windowWidth + "px",
            "margin-bottom": (windowHeight - videoHeight) / 2 + "px",
            "margin-left": "initial"
          };
        } else {
          videoHeight = windowHeight;
          videoWidth = videoHeight / 0.5625;
          this.fixStyle = {
            height: windowHeight + "px",
            width: windowHeight / 0.5625 + "px",
            "margin-left": (windowWidth - videoWidth) / 2 + "px",
            "margin-bottom": "initial"
          };
        }
      };
      window.onresize();
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('Login', this.loginForm).then(() => {
            this.loading = false
            this.$router.push({ path: '/gzzjxt/' })
          }).catch(() => {
            this.loading = false
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
};
</script>

<style scoped>

.homepage-hero-module,
.video-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.video-container .poster img,
.video-container video {
  z-index: 0;
  position: absolute;
}

.video-container .filter {
  z-index: 1;
  position: absolute;
  background: rgba(0, 0, 0, 0.4);
}
.title {
  margin-top: 300px;
  text-align: center;
}
.login {
  margin: 50px auto;
  width: 300px;
  text-align: center;
}
.el-input {
  margin: 5% auto;
  width: 300px;
}
</style>