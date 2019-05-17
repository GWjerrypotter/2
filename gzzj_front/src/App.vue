<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App",
  // 解决刷新页面store数据丢失的问题
  created() {
    if (sessionStorage.getItem("store")) {
      this.$store.replaceState(
        Object.assign(
          {},
          this.$store.state,
          JSON.parse(sessionStorage.getItem("store"))
        )
      )
    }
    window.addEventListener("beforeunload", () => {
      sessionStorage.setItem("store", JSON.stringify(this.$store.state))
    })
  },
  mounted() {
    // 关闭浏览器窗口的时候清空浏览器缓存在localStorage的数据
    window.onbeforeunload = function () {
      this.$cookies.remove('li')
      this.$cookies.remove('token')
      this.$cookies.remove('username')
      var lstorage = window.localStorage
      var sstorage = window.sessionStorage
      lstorage.clear()
      sstorage.clear()
    } 
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}
body {
  margin: 0;
}
.cell {
  white-space: nowrap !important;
  overflow: hidden;
  text-overflow: ellipsis;
}
.el-textarea__inner {
  line-height: 3;
}
.logininput .el-input__inner {
  background-color: transparent;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 1px solid #dcdfe6;
  letter-spacing: 2px;
  color: white;
}
.demo-table-expand .el-form-item__label {
  width: 100px;
  color: #99a9bf;
}
</style>
