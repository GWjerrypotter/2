<template>
  <el-container>
    <el-row>
      <el-col :span="3" class="sidebar">
        <el-menu
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          style="height: 100%"
        >
          <router-link to="/gzzj" style="text-decoration: none">
            <el-menu-item index="5">
              <i class="el-icon-edit-outline"></i>
              <span slot="title">工作总结系统</span>
            </el-menu-item>
          </router-link>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <template slot="title">选项4</template>
              <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <router-link to="/gzzj/gzzjlist" style="text-decoration: none">
            <el-menu-item index="2">
              <i class="el-icon-menu"></i>
              <span slot="title">工作总结管理</span>
            </el-menu-item>
          </router-link>
          <el-menu-item index="3" disabled>
            <i class="el-icon-document"></i>
            <span slot="title">导航三</span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">导航四</span>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="21" class="main">
        <el-breadcrumb separator="/" style="width: 50%;float: left">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>
            <a href="/">活动管理</a>
          </el-breadcrumb-item>
          <el-breadcrumb-item>活动列表</el-breadcrumb-item>
          <el-breadcrumb-item>活动详情</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="userinfo" style="float:right;height: 50px;margin-right:20px">
          <p style="float: left;margin-right: 20px;color: #fff">nihao, {{ logininfo.user_name }}</p>
          <el-dropdown trigger="click" style="height: 50px;float: right">
            <span class="el-dropdown-link">
              <img src="@/assets/img/Magic-Mouse-Scroll.jpg" class="user-avatar">
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item icon="el-icon-plus">黄金糕</el-dropdown-item>
              <el-dropdown-item icon="el-icon-circle-plus">狮子头</el-dropdown-item>
              <el-dropdown-item icon="el-icon-circle-plus-outline">螺蛳粉</el-dropdown-item>
              <el-dropdown-item icon="el-icon-check">双皮奶</el-dropdown-item>
              <el-dropdown-item icon="el-icon-circle-check-outline"><span  @click="handleLogout">退出登录</span></el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <router-view></router-view>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data() {
    return {};
  },
  computed: {
    ...mapGetters([
      'user_name',
      'userinfo',
      'logininfo'
    ])
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleLogout() {
      this.$store.dispatch('Logout').then(() => {
        this.$router.push({name: 'login'})
      })
    }
  }
  
};
</script>

<style lang="scss" scoped>
body {
  height: 100%;
  padding: 0;
  margin: 0;
}
.el-container {
  height: 1000px;
  width: 100%;
  padding: 0;
  margin: 0;
}
.el-row {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}
.el-col {
  height: 100%;
  padding: 0;
  margin: 0;
}
.el-col-21 {
  height: 50px;
  background-color: #545c64;
  padding: 0;
  margin: 0;
}
.el-breadcrumb {
  font-size: 16px;
  line-height: 3;
  height: 100%;
  vertical-align: middle;
}
.el-breadcrumb__item {
  height: 100%;
  vertical-align: middle;
}
.el-breadcrumb__inner.is_link {
  height: 100%;
  vertical-align: middle;
  color: white !important;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.demonstration {
  display: block;
  color: #8492a6;
  font-size: 14px;
  margin-bottom: 20px;
}
.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50px;
  margin-top: 5px;
}
// .sidebar {
//   width: 10%;
//   min-width: 10rem;
// }
</style>
