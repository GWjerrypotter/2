<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
.el-input__inner {
  background-color: transparent;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 1px solid #DCDFE6;
  color: #fff;
  letter-spacing: 2px;
}
</style>
