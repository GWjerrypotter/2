<template>
  <section>
    <el-col :span="22" class="toolbar">
      <el-row :gutter="20">
        <el-col :span="4" style="min-width: 200px">
          <el-input
            suffix-icon="el-icon-edit"
            placeholder="用户名查询"
            v-model="listQuery.username"
            @keyup.enter.native="handleFilter"
          ></el-input>
        </el-col>
        <el-col :span="4" style="min-width: 200px">
          <el-input
            suffix-icon="el-icon-edit"
            placeholder="姓名查询"
            v-model="listQuery.user_name"
            @keyup.enter.native="handleFilter"
          ></el-input>
        </el-col>
        <el-col :span="2" style="min-width: 100px">
          <el-button type="primary" round @click="handleFilter">查询</el-button>
        </el-col>
        <el-col :span="4" style="min-width: 200px">
          <el-button type="danger" round icon="el-icon-refresh" @click="clearAll">清除全部筛选条件</el-button>
        </el-col>
        <el-button type="primary" @click="handleAdd" style="float: right">新增</el-button>
      </el-row>
    </el-col>
    <!-- 列表 -->
    <el-table :data="users" highlight-current-row v-loading="listLoading" style="width: 100%;">
      <el-table-column type="selection" width="100"></el-table-column>
      <el-table-column type="index" width="100"></el-table-column>
      <el-table-column prop="username" label="用户名" sortable width="180"></el-table-column>
      <el-table-column prop="user_name" label="姓名" sortable width="180"></el-table-column>
      <el-table-column prop="dept.dept" label="部门" sortable min-width="200"></el-table-column>
      <el-table-column prop="user_remark" label="备注" sortable min-width="200"></el-table-column>
      <el-table-column prop="is_manager" label="是否部门管理员" width="180" align="center" sortable>
        <template slot-scope="scope">
          <el-tag
            :type="scope.row.is_manager === true ? 'primary' : 'success'"
            disable-transitions
          >{{ scope.row.is_manager === true ? '√' : '×' }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200">
        <template slot-scope="scope">
          <el-button type="success" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            type="danger"
            size="small"
            :disabled="scope.row.user_name === logininfo.user_name"
            @click="handleDel(scope.row)"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form :model="addForm" label-width="80px" ref="addForm" :rules="rules">
        <el-form-item label="用户名" prop="username" >
          <el-input
            type="text"
            v-model="addForm.username"
            placeholder="请输入用户名"
            maxlength="32"
          ></el-input>
        </el-form-item>
        <el-form-item label="部门" prop="dept" style="text-align: left">
          <span>{{ logininfo.dept }}</span>
        </el-form-item>
        <el-form-item label="姓名" prop="user_name" >
          <el-input
            type="text"
            v-model="addForm.user_name"
            placeholder="请输入姓名"
            maxlength="16"
          ></el-input>
        </el-form-item>
        <el-form-item label="是否部门管理员" prop="is_manager" label-width="120">
          <el-switch v-model="addForm.is_manager"></el-switch>
        </el-form-item>
        <el-form-item label="用户备注" prop="user_remark" style="line-height: 3">
          <el-input
            type="textarea"
            v-model="addForm.user_remark"
            placeholder="内容不能超过128个字"
            @input="descInput"
            :autosize="{ minRows: 3, maxRows: 6}"
            maxlength="128"
          ></el-input>
          <span
            class="text"
            style="float: right;color: #909399;margin-right: 55px;"
          >已输入{{remnant}}字,剩余{{128-remnant}}字</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handleCancel">取消</el-button>
        <el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
      </div>
      <el-alert
      :closable="false"
      class="readme"
      title="关于密码"
      type="warning"
      description="新用户密码自动设置为:ab12345678 ,请告知用户登录后尽快修改密码."
      show-icon />
    </el-dialog>

    <!-- 修改 -->
    <el-dialog :visible.sync="dialogFormVisible" title="用户修改">
      <el-form ref="userform" :model="userform" :rules="rules" label-width="100px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="userform.username" class="inputwidth"/>
        </el-form-item>
        <el-form-item label="姓名" prop="user_name" >
          <el-input v-model="userform.user_name" class="inputwidth"/>
        </el-form-item>
        <el-form-item label="是否部门管理员" prop="is_manager" label-width="120">
          <el-switch v-model="userform.is_manager"></el-switch>
        </el-form-item>
        <el-form-item label="用户备注" prop="user_remark" style="line-height: 3">
          <el-input
            type="textarea"
            v-model="userform.user_remark"
            placeholder="内容不能超过128个字"
            @input="descInput2"
            :autosize="{ minRows: 3, maxRows: 6}"
            maxlength="128"
          ></el-input>
          <span
            class="text"
            style="float: right;color: #909399;margin-right: 55px;"
          >已输入{{remnant}}字,剩余{{128-remnant}}字</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="updataUserInfo('userform')">确 定</el-button>
      </div>
    </el-dialog>

    

    <!-- 工具条 -->
    <el-col class="toolbar">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[2, 10, 20, 30, 40]"
        :page-size="pagesize"
        :total="total"
        layout="total, sizes, prev, pager, next, jumper"
        style="float:left;"
      ></el-pagination>
    </el-col>
  </section>
</template>

<script>
import { getuserlist, adduser, updateuser, deleteuser } from "@/api/index";
import { mapGetters } from "vuex";
import { Message } from 'element-ui'
export default {
  data() {
    return {
      users: [],
      total: undefined,
      currentPage: 1,
      pagesize: 10,
      listQuery: {
        username: undefined,
        user_name: undefined
      },
      listLoading: false,
      addLoading: false,
      addFormVisible: false, //新增界面是否显示
      dialogFormVisible: false, //编辑界面是否显示
      
      addForm: {
        username: '',
        password: '',
        user_name: '',
        dept: undefined,
        is_manager: undefined,
        user_remark: '',
      },
      userform: {
        username: '',
        user_name: '',
        is_manager: undefined,
        user_remark: '',
        id: '',
      },
      
      depts: [],
      checked: false,
      remnant: 0,
      remnant2: 0,
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 256, message: "长度在 1 到 256 之间（含）" }
        ],
        user_name: [ 
          { required: true, message: "请输入姓名", trigger: "blur" },
          { min: 1, max: 16, message: "长度在 1 到 16 之间（含）" }
        ],
        // is_manager: [ 
        //   { required: true, message: "请选择", trigger: "blur" },
        // ],
        user_remark: [ 
          { max: 128, message: "长度不能大于128（含）" }
        ],
      },
      
    };
  },
  mounted() {
    this.getusers();
  },
  computed: {
    ...mapGetters(["logininfo"])
  },
  methods: {
    handleSizeChange(val) {
      this.pagesize = val;
      this.getusers({ p: this.currentPage, page_size: this.pagesize, ...this.listQuery });
    },
    handleCurrentChange(page) {
      this.currentPage = page;
      this.getusers({ p: this.currentPage, ...this.listQuery });
    },
    getusers(params) {
      let dept = this.$store.getters.dept.dept;
      this.listLoading = true;
      getuserlist({
        p: this.currentPage,
        page_size: this.pagesize,
        dept, 
        ...this.listQuery
      })
        .then(response => {
          const d = response.results;
          this.users = d;
          this.total = response.count;
          this.listLoading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    handleFilter() {
      this.currentPage = 1
      this.getusers(this.listQuery)
    },
    clearAll() {
      this.currentPage = 1;
      this.pagesize = undefined;
      this.listQuery.username = undefined;
      this.listQuery.user_name = undefined;
      this.getusers(this.listQuery);
    },
    //显示新增界面
    handleAdd() {
      this.addFormVisible = true;
      this.addForm = {
        username: '',
        password: '',
        user_name: '',
        dept: this.logininfo.dept_id,
        is_manager: false,
        user_remark: '',
      };
    },
    // 提示输入字数
    descInput() {
      var txtVal = this.addForm.user_remark.length;
      this.remnant = txtVal;
    },
    descInput2() {
      var txtVal = this.userform.user_remark.length;
      this.remnant2 = txtVal;
    },
    //新增
    addSubmit: function() {
      this.$refs.addForm.validate(valid => {
        if (valid) {
          this.$confirm("确认提交吗？", "提示", {}).then(() => {
            this.addLoading = true;
            let para = this.addForm;
            adduser({
              username: this.addForm.username,
              user_name: this.addForm.user_name,
              password: 'ab12345678',
              dept: this.addForm.dept,
              is_manager: this.addForm.is_manager,
              user_remark: this.addForm.user_remark,
            }).then(res => {
              this.addLoading = false;
              this.$message({
                message: "提交成功",
                type: "success"
              });
              this.addForm = {};
              this.addFormVisible = false;
              this.getusers();
            });
          });
        }
      });
    },
    // 取消新增
    handleCancel() {
      this.addFormVisible = false;
    },
    handleEdit(index, row) {
      this.dialogFormVisible = true
      this.userform.username = row.username
      this.userform.user_name = row.user_name
      this.userform.is_manager = row.is_manager
      this.userform.user_remark = row.user_remark
      this.userform.id = row.id
    },
    // 编辑
    updataUserInfo(userform) {
      updateuser(this.userform.id, {
        username: this.userform.username,
        user_name: this.userform.user_name,
        is_manager: this.userform.is_manager,
        user_remark: this.userform.user_remark
      }).then(() => {
        Message({
          message: '更新成功!',
          type: 'success'
        })
        this.dialogFormVisible = false
        this.getusers()
        
      }).catch(err => {
        Message({
          message: err.response.data,
          type: 'error'
        })
      })
    },
    handleDel(row) {
      this.$confirm("注意：删除用户会同时删除该用户录入的工作总结！确认删除该记录吗?", "警告", {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: "warning"
      })
        .then(() => {
          this.listLoading = true;
          let para = row.id;
          deleteuser(para).then(res => {
            this.listLoading = false;
            this.$message({
              message: "删除成功",
              type: "success"
            });
            this.getusers();
          })
        })
        .catch(err => {
          Message({
            message: err,
            type: 'error'
          })
        });
    },
    
  }
};
</script>

<style lang="scss" scoped>
.toolbar {
  padding-bottom: 0px;
  margin-top: 20px;
  margin-left: 20px
}
</style>
