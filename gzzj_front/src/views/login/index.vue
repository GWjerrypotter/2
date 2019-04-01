<template>
  <div>
    <div class="homepage-hero-module">
      <div class="video-container">
        <div :style="fixStyle" class="filter">
          <div class="title">
            <h1 style="color: #3AB2DA">Work Summary System</h1>
          </div>
          <div class="login">
            <el-input v-model="user" placeholder="请输入用户名"></el-input>
            <el-input v-model="password" placeholder="请输入密码"></el-input>
            <el-button type="success" style="width: 300px;">登录</el-button>
          </div>
        </div>
        <video :style="fixStyle" autoplay loop class="fillWidth" v-on:canplay="canplay">
          <source src="../../assets/video/Magic-Mouse-Scroll.mp4" type="video/mp4">
        </video>
        <div class="poster hidden" v-if="!vedioCanPlay">
          <img :style="fixStyle" src="../../assets/img/Magic-Mouse-Scroll.jpg" alt>
        </div>
      </div>
    </div>
  </div>
</template>

</style>

<script>
export default {
  name: "login",
  data() {
    return {
      vedioCanPlay: false,
      fixStyle: "",
      user: "",
      password: "",
    };
  },

  mounted() {
    this.startup();
  },
  methods: {
    canplay() {
      this.vedioCanPlay = true;
    },
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
  background-color: transparent !important;
}
</style>