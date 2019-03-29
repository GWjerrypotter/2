<template>
  <section>
    <el-col :span="22" class="toolbar" style="padding-bottom: 0px;">
      <!-- <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getgzzj()">查询</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleAdd">新增</el-button>
        </el-form-item>
      </el-form> -->
      <el-row :gutter="20">
        <el-col :span="4" style="min-width: 200px">
          <el-input suffix-icon="el-icon-edit" placeholder="录入人查询" v-model="listQuery.user" @keyup.enter.native="handleFilter"></el-input>
        </el-col>
        <el-col :span="4" style="min-width: 200px">
          <el-input suffix-icon="el-icon-edit" placeholder="内容查询" v-model="listQuery.gzzj" @keyup.enter.native="handleFilter"></el-input>
        </el-col>
        <el-col :span="2" style="min-width: 120px">
          <el-popover
            placement="bottom"
            width="430"
            style="margin-right:10px;"
            trigger="click">
            <div class="demo-input-suffix">
              <el-date-picker
                v-model="datepickervalue"
                :default-time="['00:00:00', '23:59:59']"
                type="datetimerange"
                align="right"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                value-format="yyyy-MM-dd HH:mm:ss"
                @change="pickdateFilter"
              />
            </div>
            <el-button slot="reference" round>选择日期</el-button>
          </el-popover>
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
    <!--列表-->
    <el-table :data="gzzjs" highlight-current-row v-loading="listLoading" style="width: 100%;">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column type="index" width="60"></el-table-column>
      <el-table-column prop="user.user_name" label="录入人" width="120" sortable></el-table-column>
      <el-table-column prop="time" label="时间" width="120" sortable></el-table-column>
      <el-table-column label="工作总结" min-width="180" sortable>
        <template slot-scope="scope">
          <router-link to="/gzzj/gzzjcheck" style="text-decoration: none">{{ scope.row.gzzj }}</router-link>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200">
        <template slot-scope="scope">
          <el-button type="info" size="small" @click="handleCheck(scope.row)">查看详情</el-button>
          <el-button type="danger" size="small" @click="handleDel(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--工具条-->
    <el-col :span="22" class="toolbar">
      <!-- <el-button type="danger" @click="batchRemove" :disabled="this.sels.length===0">批量删除</el-button> -->
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

    <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form :model="addForm" label-width="80px" ref="addForm" :rules="rules">
        <el-form-item label="录入人" prop="user" style="text-align: left">
          <el-select v-model="addForm.user" placeholder="请选择">
            <el-option
              v-for="item in users"
              :key="item.id"
              :label="item.user_name"
              :value="item.id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="工作总结" prop="gzzj" style="line-height: 3">
          <el-input
            type="textarea"
            v-model="addForm.gzzj"
            placeholder="内容不能超过256个字"
            @input="descInput"
            :autosize="{ minRows: 3, maxRows: 6}"
            maxlength="256"
          ></el-input>
          <span
            class="text"
            style="float: right;color: #909399;margin-right: 55px;"
          >已输入{{remnant}}字,剩余{{256-remnant}}字</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <!-- <el-button @click.native="addFormVisible = false">取消</el-button> -->
        <el-button @click="handleCancel">取消</el-button>
        <el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
      </div>
    </el-dialog>

    <!-- 查看详情 -->
    <el-dialog
      title="工作总结详情"
      :visible.sync="checkVisible"
      :close-on-click-modal="true"
      class="dialog_check"
    >
      <table class="checkgzzj">
        <tr>
          <td>
            <i class="el-icon-edit"></i>
          </td>
          <td class="checktitle">录入人：</td>
          <td>{{username}}</td>
        </tr>
        <tr>
          <td>
            <i class="el-icon-date"></i>
          </td>
          <td class="checktitle">录入时间：</td>
          <td>{{checklist.time}}</td>
        </tr>
        <tr>
          <td>
            <i class="el-icon-printer"></i>
          </td>
          <td class="checktitle">内容：</td>
          <td>{{checklist.gzzj}}</td>
        </tr>
      </table>
    </el-dialog>
  </section>
</template>

<script>
import { getgzzjlist, deletegzzj, getuserlist, addgzzj } from "@/api/index";
export default {
  data() {
    return {
      listQuery: {
        user: undefined,
        gzzj: undefined,
        time_after: undefined,
        time_before: undefined,
      },
      filters: {
        user: "",
        gzzj: ""
      },
      gzzjs: [],
      users: [],
      rules: {
        user: [
          { required: true, message: '请选择录入人', trigger: 'change' }
        ],
        gzzj: [
          { required: true, message: '请输入工作总结内容', trigger: 'blur' },
          { min: 1, max: 256, message: '长度在 1 到 256 之间（含）'}
        ]
      },
      remnant: 0, //输入数
      checklist: [],
      username: "",
      total: 0,
      currentPage: 1,
      pagesize: 10,
      sels: [],
      listLoading: false,
      datepickervalue: '',
      addLoading: false,
      addFormVisible: false, //新增界面是否显示
      checkVisible: false, //查看详情界面是否显示
      addForm: {
        gzzj: "",
        user: ""
      }
      // username: this.checklist.user.user_name,
    };
  },
  mounted() {
    this.getgzzj();
  },
  methods: {
    handleSizeChange(val) {
      this.pagesize = val;
      console.log("当前pagesize是" + this.pagesize);
      this.getgzzj({ page_size: this.pagesize, ...this.listQuery });
    },
    handleCurrentChange(page) {
      this.currentPage = page;
      console.log(
        "当前页码是" + this.currentPage + ",pagesize是" + this.pagesize
      );
      this.getgzzj({ p: this.currentPage, ...this.listQuery });
    },
    getgzzj(params) {
      this.listLoading = true;
      // params = { page_size: this.pagesize, p: this.currentPage };
      typeof (params) === 'object' ? params.page_size = this.pagesize : params = { page_size: this.pagesize }
      getgzzjlist(params)
        .then(response => {
          console.log(response);
          const d = response.data.results;
          this.gzzjs = d;
          this.total = response.data.count;
          this.listLoading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    handleFilter() {
      this.currentPage = 1
      this.getgzzj(this.listQuery)
    },
    pickdateFilter() {
      this.listQuery.time_after = this.datepickervalue[0]
      this.listQuery.time_before = this.datepickervalue[1]
      this.handleFilter()
    },
    clearAll() {
      this.currentPage = 1
      this.pagesize = undefined
      this.listQuery.time_after = undefined
      this.listQuery.time_before = undefined
      this.listQuery.user = undefined
      this.listQuery.gzzj = undefined
      this.getgzzj(this.listQuery)
    },
    handleDel(row) {
      this.$confirm("确认删除该记录吗?", "提示", {
        type: "warning"
      })
        .then(() => {
          this.listLoading = true;
          let para = row.id;
          deletegzzj(para).then(res => {
            this.listLoading = false;
            this.$message({
              message: "删除成功",
              type: "success"
            });
            this.getgzzj();
          });
        })
        .catch(() => {});
    },

    //显示新增界面
    handleAdd() {
      this.addFormVisible = true;
      this.addForm = {
        user: "",
        gzzj: ""
      };
      getuserlist().then(response => {
        const usr = response.data.results;
        this.users = usr;
      });
    },
    //新增
    addSubmit: function() {
      this.$refs.addForm.validate(valid => {
        if (valid) {
          this.$confirm("确认提交吗？", "提示", {}).then(() => {
            this.addLoading = true;
            let para = this.addForm;
            addgzzj(para).then(res => {
              this.addLoading = false;
              this.$message({
                message: "提交成功",
                type: "success"
              });
              this.addForm = {};
              console.log(this.addForm);
              this.addFormVisible = false;
              this.getgzzj();
            });
          });
        }
      });
    },
    handleCancel() {
      this.addFormVisible = false

    },
    // 显示详情页面
    handleCheck(row) {
      console.log(row);
      this.checkVisible = true;
      this.checklist = row;
      this.username = row.user.user_name;
    },
    // 提示输入字数
    descInput() {
      var txtVal = this.addForm.gzzj.length;
      this.remnant = txtVal;
    }
  },
  filters: {
    ellipsis(value) {
      if (!value) return "";
      if (value.length > 10) {
        return value.slice(0, 8) + "...";
      }
      return value;
    }
  }
};
</script>

<style lang="scss" scoped>
.toolbar {
  margin-top: 2%;
  margin-left: 1%;
  text-align: left;
}
.checkgzzj td {
  text-align: left;
  padding-bottom: 3rem;
  padding-left: 2rem;
  font-size: 1.2rem;
  vertical-align: top;
}
.checktitle {
  width: 25%;
}
</style>
