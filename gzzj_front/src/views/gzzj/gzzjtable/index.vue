<template>
  <section>
    <el-col :span="22" class="toolbar" style="padding-bottom: 0px;">
      <el-row :gutter="20">
        <el-col :span="4" style="min-width: 200px">
          <el-input
            suffix-icon="el-icon-edit"
            placeholder="录入人查询"
            v-model="listQuery.user"
            @keyup.enter.native="handleFilter"
          ></el-input>
        </el-col>
        <el-col :span="4" style="min-width: 200px">
          <el-input
            suffix-icon="el-icon-edit"
            placeholder="内容查询"
            v-model="listQuery.gzzj"
            @keyup.enter.native="handleFilter"
          ></el-input>
        </el-col>
        <el-col :span="2" style="min-width: 120px">
          <el-popover placement="bottom" width="430" style="margin-right:10px;" trigger="click">
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
      <el-table-column type="expand" class="detail">
        <template slot="header" slot-scope="scope">
          <el-tooltip class="item" effect="dark" content="点击下面按钮查看详情" placement="right">
            <i class="el-icon-question"></i>
          </el-tooltip>
        </template>
        <template slot-scope="props">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item label="录入人">
              <span>{{ props.row.user.user_name }}</span>
            </el-form-item>
            <el-form-item label="时间">
              <span>{{ props.row.time }}</span>
            </el-form-item>
            <el-form-item label="工作总结内容">
              <span>{{ props.row.gzzj }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column type="index" width="60"></el-table-column>
      <el-table-column prop="user.user_name" label="录入人" width="120" sortable></el-table-column>
      <el-table-column prop="time" label="时间" width="120" sortable></el-table-column>
      <el-table-column label="工作总结" min-width="180" sortable>
        <template slot-scope="scope">
          <span>{{ scope.row.gzzj }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="200" align="center">
        <template slot-scope="scope">
          <el-button
            type="warning"
            size="small"
            :disabled="scope.row.user.user_name !== logininfo.user_name"
            @click="handleEdit(scope.row)">编辑</el-button>
          <el-button
            type="danger"
            size="small"
            :disabled="scope.row.user.user_name !== logininfo.user_name"
            @click="handleDel(scope.row)"
          >删除</el-button>
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
      <el-button
        type="primary"
        size="small"
        style="margin-left: 20px"
        :disabled="!logininfo.is_manager"
        @click="export2Excel"
      >导出 EXCEL</el-button>
      <el-button
        type="primary"
        size="small"
        style="margin-left: 20px"
        :disabled="!logininfo.is_manager"
        @click="export2Word"
      >导出 WORD</el-button>
    </el-col>

    <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false">
      <el-form :model="addForm" label-width="80px" ref="addForm" :rules="rules">
        <el-form-item label="录入人" prop="user" style="text-align: left">
          <span>{{ logininfo.user_name }}</span>
        </el-form-item>
        <el-form-item label="日期" prop="time">
          <el-date-picker
            v-model="addForm.time"
            type="date"
            value-format="yyyy-MM-dd"
            placeholder="选择日期"
            :picker-options="pickerOptions"
          ></el-date-picker>
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

    <!-- 修改 -->
    <el-dialog :visible.sync="editFormVisible" title="内容修改">
      <el-form ref="editForm" :model="editForm" :rules="rules" label-width="100px">
        <el-form-item label="录入人" prop="user" style="text-align: left">
          <span>{{ logininfo.user_name }}</span>
        </el-form-item>
        <el-form-item label="日期" prop="time">
          <el-date-picker
            v-model="editForm.time"
            type="date"
            value-format="yyyy-MM-dd"
            placeholder="选择日期"
            :picker-options="pickerOptions"
          ></el-date-picker>
        </el-form-item>
        <el-form-item label="工作总结" prop="gzzj" style="line-height: 3">
          <el-input
            type="textarea"
            v-model="editForm.gzzj"
            placeholder="内容不能超过256个字"
            @input="descInput2"
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
        <el-button @click="handleCancel2">取消</el-button>
        <el-button type="primary" @click.native="editSubmit('editForm')" :loading="addLoading">提交</el-button>
      </div>
    </el-dialog>

    <!-- 查看详情 -->
    <!-- <el-dialog
      title="工作总结详情"
      :visible.sync="checkVisible"
      :close-on-click-modal="true"
      class="dialog_check"
    >
      <table class="checkgzzj" style="width: inherit">
        <tr>
          <td>
            <i class="el-icon-edit"></i>
          </td>
          <td class="checktitle">录入人：</td>
          <td class="checkcontent">{{username}}</td>
        </tr>
        <tr>
          <td>
            <i class="el-icon-date"></i>
          </td>
          <td class="checktitle">录入时间：</td>
          <td class="checkcontent">{{checklist.time}}</td>
        </tr>
        <tr>
          <td>
            <i class="el-icon-printer"></i>
          </td>
          <td class="checktitle">内容：</td>
          <td class="checkcontent">{{checklist.gzzj}}</td>
        </tr>
      </table>
    </el-dialog>-->
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import {
  getgzzjlist,
  deletegzzj,
  getuserlist,
  addgzzj,
  editgzzj
} from "@/api/index";
import axios from "axios";
export default {
  data() {
    return {
      editid: "",
      exportlist: [],
      listQuery: {
        user: undefined,
        gzzj: undefined,
        time_after: undefined,
        time_before: undefined
      },
      filters: {
        user: "",
        gzzj: ""
      },
      gzzjs: [],
      users: [],
      disabled: true,
      department: "",
      rules: {
        time: [{ required: true, message: "请选择日期", trigger: "blur" }],
        gzzj: [
          { required: true, message: "请输入工作总结内容", trigger: "blur" },
          { min: 1, max: 256, message: "长度在 1 到 256 之间（含）" }
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
      datepickervalue: "",
      addLoading: false,
      addFormVisible: false, //新增界面是否显示
      editFormVisible: false, //新增界面是否显示
      checkVisible: false, //查看详情界面是否显示
      addForm: {
        time: "",
        gzzj: "",
        user: ""
      },
      editForm: {
        id: "",
        user: "",
        time: "",
        gzzj: ""
      },
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [
          {
            text: "今天",
            onClick(picker) {
              picker.$emit("pick", new Date());
            }
          },
          {
            text: "昨天",
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit("pick", date);
            }
          },
          {
            text: "一周前",
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", date);
            }
          }
        ]
      }
      // username: this.checklist.user.user_name,
    };
  },
  mounted() {
    this.getgzzj();
  },
  computed: {
    ...mapGetters(["logininfo"])
  },
  methods: {
    handleSizeChange(val) {
      this.pagesize = val;
      this.getgzzj({
        p: this.currentPage,
        page_size: this.pagesize,
        ...this.listQuery
      });
    },
    handleCurrentChange(page) {
      this.currentPage = page;
      this.getgzzj({ p: this.currentPage, ...this.listQuery });
    },
    getgzzj(params) {
      this.listLoading = true;
      let dept = this.$store.getters.dept.dept;
      // params = { page_size: this.pagesize, p: this.currentPage };
      // typeof params === "object"
      //   ? (params.page_size = this.pagesize)
      //   : (params = { page_size: this.pagesize });
      getgzzjlist({
        p: this.currentPage,
        page_size: this.pagesize,
        dept,
        ...this.listQuery
      })
        .then(response => {
          const d = response.results;
          this.gzzjs = d;
          this.total = response.count;
          this.listLoading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    handleFilter() {
      this.currentPage = 1;
      this.getgzzj(this.listQuery);
    },
    pickdateFilter() {
      this.listQuery.time_after = this.datepickervalue[0];
      this.listQuery.time_before = this.datepickervalue[1];
      this.handleFilter();
    },
    clearAll() {
      this.currentPage = 1;
      this.pagesize = undefined;
      this.listQuery.time_after = undefined;
      this.listQuery.time_before = undefined;
      this.listQuery.user = undefined;
      this.listQuery.gzzj = undefined;
      this.getgzzj(this.listQuery);
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
        user: this.logininfo.user_id,
        gzzj: ""
      };
      getuserlist().then(response => {
        const usr = response.results;
        this.users = usr;
      });
    },
    //显示编辑界面
    handleEdit(row) {
      this.editFormVisible = true;
      this.editForm = {
        id: row.id,
        user: this.logininfo.user_id,
        gzzj: row.gzzj,
        time: row.time
      };
      getuserlist().then(response => {
        const usr = response.results;
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
              this.addFormVisible = false;
              this.getgzzj();
            });
          });
        }
      });
    },
    //编辑
    editSubmit(editForm) {
      this.$refs.editForm.validate(valid => {
        if (valid) {
          this.$confirm("确认提交吗？", "提示", {}).then(() => {
            this.addLoading = true;
            editgzzj(this.editForm.id, {
              time: this.editForm.time,
              gzzj: this.editForm.gzzj
            }).then(res => {
              this.addLoading = false;
              this.$message({
                message: "提交成功",
                type: "success"
              });
              this.editForm = {};
              this.editFormVisible = false;
              this.getgzzj();
            });
          });
        }
      });
    },

    handleCancel() {
      this.addFormVisible = false;
    },
    handleCancel2() {
      this.editFormVisible = false;
    },
    // 提示输入字数
    descInput() {
      var txtVal = this.addForm.gzzj.length;
      this.remnant = txtVal;
    },
    descInput2() {
      var txtVal = this.editForm.gzzj.length;
      this.remnant = txtVal;
    },
    export2Excel() {
      let dept = this.$store.getters.dept.dept;
      getgzzjlist({ ...this.listQuery, dept, page_size: 1000 }).then(res => {
        import("@/vendor/Export2Excel")
          .then(excel => {
            const tHeader = ["序号", "录入人", "录入时间", "工作总结"];
            const filterVal = ["id", "user", "time", "gzzj"];
            const list = res.results;
            const data = this.formatJson(filterVal, list);
            excel.export_json_to_excel({
              header: tHeader,
              data,
              filename: "querygzzj",
              autowidth: false,
              bookType: "xlsx"
            });
          })
          .catch(() => {
            this.$message({
              message: "导出失败，请联系管理员",
              type: "error"
            });
          });
      });
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map((v, k) =>
        filterVal.map(j => {
          if (j === "user") {
            return v["user"].user_name;
          } else if (j === "id") {
            return k + 1;
          } else {
            return v[j];
          }
        })
      );
    },
    export2Word() {
      let dept = this.$store.getters.dept.dept;
      getgzzjlist({ ...this.listQuery, dept, page_size: 1000 })
        // axios.get(`http://192.168.31.25:8000/gzzjlist/`, { //url: 接口地址
        //   responseType: `arraybuffer` //一定要写
        // })
        .then(res => {
          let shuzu = [];
          for (let index = 0; index < res.results.length; index++) {
            let element = res.results[index];
            shuzu.push(element.gzzj);
          }
          if (res.conut != 0) {
            let blob = new Blob([shuzu], {
              type: `application/msword` //word文档为msword,pdf文档为pdf
            });
            let objectUrl = URL.createObjectURL(blob);
            let link = document.createElement("a");
            let fname = `我的文档`; //下载文件的名字
            link.href = objectUrl;
            link.setAttribute("download", fname);
            document.body.appendChild(link);
            link.click();
          } else {
            this.$message({
              type: "error",
              message: "导出失败"
            });
          }
        });
      // axios({
      //   method: "get",
      //   url: "http://192.168.31.25:8000/gzzjlist/",
      //   responseType: "blob"
      // }).then(res => {
      //   //这里res.data是返回的blob对象
      //   var blob = new Blob([res.data], {
      //     type: "application/msword"
      //       // "application/vnd.openxmlformats-officedocument.wordprocessingml.document;charset=utf-8"
      //   }); //application/vnd.openxmlformats-officedocument.wordprocessingml.document这里表示doc类型
      //   var downloadElement = document.createElement("a");
      //   var href = window.URL.createObjectURL(blob); //创建下载的链接
      //   downloadElement.href = href;
      //   downloadElement.download = "xxx.docx"; //下载后文件名
      //   document.body.appendChild(downloadElement);
      //   downloadElement.click(); //点击下载
      //   document.body.removeChild(downloadElement); //下载完成移除元素
      //   window.URL.revokeObjectURL(href); //释放掉blob对象
      // });
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
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 70%;
}
</style>
