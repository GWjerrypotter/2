<template>
  <el-container>
    <el-row>
      <el-col :span="3" class="sidebar">
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          style="height: 100%"
        >
          <router-link to="/gzzjxt" style="text-decoration: none">
            <el-menu-item>
              <i class="el-icon-edit-outline"></i>
              <span slot="title">工作总结系统</span>
            </el-menu-item>
          </router-link>
          <router-link to="/gzzjxt/gzzjlist" style="text-decoration: none">
            <el-menu-item>
              <i class="el-icon-menu"></i>
              <span slot="title">工作总结管理</span>
            </el-menu-item>
          </router-link>
          <router-link v-if="logininfo.is_manager" to="/gzzjxt/user" style="text-decoration: none">
            <el-menu-item>
              <i class="el-icon-setting"></i>
              <span slot="title">用户管理</span>
            </el-menu-item>
          </router-link>
        </el-menu>
      </el-col>
      <el-col :span="21" class="main">
        <div class="userinfo" style="float:right;height: 50px;margin-right:20px">
          <p style="float: left;margin-right: 20px;color: #fff">你好, {{ logininfo.user_name }}</p>
          <el-dropdown trigger="click" style="height: 50px;float: right">
            <span class="el-dropdown-link">
              <img src="@/assets/img/Magic-Mouse-Scroll.jpg" class="user-avatar">
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item icon="el-icon-sort">
                <span @click="changePassword">修改密码</span>
              </el-dropdown-item>
              <el-dropdown-item icon="el-icon-circle-close">
                <span @click="handleLogout">退出登录</span>
              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <router-view></router-view>
      </el-col>
    </el-row>

    <!-- 改密码 -->
    <el-dialog :visible.sync="passwordVisible" title="密码修改">
      <el-form ref="passwordform" :model="passwordform" :rules="rules_password" label-width="100px">
        <el-form-item label="原密码" prop="oldpassword">
          <el-input
            v-model="passwordform.oldpassword"
            :type="passwordform.pwdType"
            class="inputwidth"
          >
            <i slot="suffix" class="el-input__icon el-icon-view" @click="showPwd"/>
          </el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="newpassword">
          <el-input
            v-model="passwordform.newpassword"
            type="password"
            placeholder="请输入新密码"
            class="inputwidth"
          >
            <i slot="suffix" class="el-input__icon el-icon-view" @click="showPwd"/>
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="passwordVisible = false">取 消</el-button>
        <el-button type="primary" @click="updatapassword('passwordform')">确 定</el-button>
      </div>
    </el-dialog>
  </el-container>
</template>

<script>
import { mapGetters } from "vuex";
import { userpassword } from "@/api/index";
export default {
  data() {
    return {
      passwordform: {
        oldpassword: "",
        newpassword: "",
        pwdType: "password"
      },
      rules_password: {
        oldpassword: [
          { required: true, message: "请输入原密码", trigger: "blur" }
        ],
        newpassword: [
          {
            required: true,
            min: 6,
            message: "请输入至少8位的新密码",
            trigger: "blur"
          }
        ]
      },
      passwordVisible: false //修改密码界面是否显示
    };
  },
  computed: {
    ...mapGetters(["user_name", "userinfo", "logininfo"])
  },
  methods: {
    changePassword() {
      this.passwordVisible = true;
    },
    showPwd() {
      this.passwordform.pwdType === "password"
        ? (this.passwordform.pwdType = "text")
        : (this.passwordform.pwdType = "password");
    },
    updatapassword() {
      this.$refs.passwordform.validate(valid => {
        if (valid) {
          userpassword(this.logininfo.user_id, {
            oldpassword: this.passwordform.oldpassword,
            newpassword: this.passwordform.newpassword
          })
            .then(res => {
              this.$refs["passwordform"].resetFields();
              this.$message({
                message: "密码修改成功",
                type: "success"
              });
              this.passwordVisible = false;
            })
            .catch(err => {
              this.$message({
                message: err.response.data,
                type: "error"
              });
            });
        }
      });
    },
    handleLogout() {
      this.$store.dispatch("Logout").then(() => {});
      this.$store.dispatch("FedLogOut").then(location.reload(),sessionStorage.clear(),() => {
        this.$router.push({ path: "/" })
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
