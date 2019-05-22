<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item timestamp="Step 1" icon="el-icon-bottom" color="blue" size="large" placement="top">
        <el-card>
          <h4>修改密码</h4>
          <p>初次登录请点击右上角头像修改密码</p>
        </el-card>
      </el-timeline-item>
      <el-timeline-item timestamp="Step 2" icon="el-icon-bottom" color="blue" size="large" placement="top">
        <el-card>
          <h4>添加工作总结</h4>
          <p>请点击左侧菜单栏“工作总结管理”进入并新增总作总结</p>
        </el-card>
      </el-timeline-item>
      <el-timeline-item timestamp="Step 3" icon="el-icon-bottom" color="blue" size="large" placement="top">
        <el-card>
          <h4>Tips</h4>
          <p>已支持修改工作总结，如发现添加有误可自行删除并重新添加或直接进行修改</p>
        </el-card>
      </el-timeline-item>
        <el-timeline-item v-if="logininfo.is_manager" timestamp="Step 4" icon="el-icon-bottom" color="blue" size="large" placement="top">
          <el-card>
            <h4>导出（仅限部门管理员）</h4>
            <p>提供EXCEL和WORD导出</p>
          </el-card>
        </el-timeline-item>
        <el-timeline-item v-if="logininfo.is_manager" timestamp="Step 5" icon="el-icon-bottom" color="blue" size="large" placement="top">
          <el-card>
            <h4>用户管理（仅限部门管理员）</h4>
            <p>请点击左侧菜单栏“用户管理”进入并新增、编辑或删除用户</p>
          </el-card>
        </el-timeline-item>
      <el-timeline-item placement="top" icon="el-icon-user" color="#67C23A" size="large">
        <el-card>
          <h4>与君共勉</h4>
          <p>不积跬步，无以至千里；不积小流，无以成江海。</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      
    };
  },
  computed: {
    ...mapGetters(["user_name", "userinfo", "logininfo"])
  }
}
</script>

<style lang="scss" scoped>
.block {
  margin-top: 80px;
}
.el-card {
  width: 450px;
  height: 100px;
}
h4 {
  margin: 5px;
}
</style>
