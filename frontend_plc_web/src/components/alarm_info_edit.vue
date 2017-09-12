<template>
  <Modal v-model="showCreate" title="新建" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formAlarmInfo" :model="formAlarmInfo" :label-width="80">


      <FormItem label="选择变量" prop="variable_id">

        <Select v-model="group_id" style="width:100px" placeholder="选择变量组" filterable @on-change="post_variable">
          <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
        </Select>

        <Select transfer v-model="formAlarmInfo.variable_id" style="width:100px" placeholder="选择变量名"
                filterable>
          <Option v-for="variable in variables" :value="variable.id" :key="variable.id">{{ variable.variable_name }}
          </Option>
        </Select>

      </FormItem>

      <FormItem label="报警类型" prop="alarm_type">
        <Select transfer v-model="formAlarmInfo.alarm_type" style="width:100px" placeholder="选择报警类型" filterable>
          <Option value="1">提示</Option>
          <Option value="2">警告</Option>
          <Option value="3">错误</Option>
        </Select>
      </FormItem>

      <FormItem label="报警内容" prop="note">
        <Input v-model="formAlarmInfo.note" placeholder="请输入报警内容"></Input>
      </FormItem>


    </Form>

    <div slot="footer">
      <Button type="success" :loading="loading" @click="editSubmit('formVariableEdit')">提交</Button>
      <Button type="ghost" @click="handleReset()" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="handleClean('formAlarmInfo')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>

  </Modal>
</template>

<script>
  import Group from '../models/actions/group'
  import AlarmInfo from '../models/actions/alarm_info'
  import Variable from '../models/actions/variable'

  export default {
    data () {
      return {
        loading: false,
        formVariableEdit: {
          id: null,
          variable_name: null,
          group_id: null,
          address: null,
          acquisition_cycle: null,
          data_type: null,
          area: null,
          db_num: null,
          note: null,
          rw_type: null,
          server_record_cycle: null,
          ten_id: null,
          upload: null,
          write_value: null
        }
//        ruleVariableCreate: {
//          variable_name: [
//            {required: true, message: '姓名不能为空', trigger: 'blur'}
//          ],
//          mail: [
//            {required: true, message: '邮箱不能为空', trigger: 'blur'},
//            {type: 'email', message: '邮箱格式不正确', trigger: 'blur'}
//          ],
//          city: [
//            {required: true, message: '请选择城市', trigger: 'change'}
//          ],
//          gender: [
//            {required: true, message: '请选择性别', trigger: 'change'}
//          ],
//          interest: [
//            {required: true, type: 'array', min: 1, message: '至少选择一个爱好', trigger: 'change'},
//            {type: 'array', max: 2, message: '最多选择两个爱好', trigger: 'change'}
//          ],
//          date: [
//            {required: true, type: 'date', message: '请选择日期', trigger: 'change'}
//          ],
//          time: [
//            {required: true, type: 'date', message: '请选择时间', trigger: 'change'}
//          ],
//          desc: [
//            {required: true, message: '请输入个人介绍', trigger: 'blur'},
//            {type: 'string', min: 20, message: '介绍不能少于20字', trigger: 'blur'}
//          ]
//        }
      }
    },
    props: [
      'showEdit',
      'groups',
      'data'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    methods: {
      data2form () {
        this.formVariableEdit.id = this.data.id
        this.formVariableEdit.variable_name = this.data.variable_name
        this.formVariableEdit.group_id = this.data.group_id
        this.formVariableEdit.address = this.data.address
        if (this.data.acquisition_cycle) {
          this.formVariableEdit.acquisition_cycle = this.data.acquisition_cycle.toString()
        }
        this.formVariableEdit.data_type = this.data.data_type
        if (this.data.area) {
          this.formVariableEdit.area = this.data.area.toString()
        }
        this.formVariableEdit.db_num = this.data.db_num
        this.formVariableEdit.note = this.data.note
        this.formVariableEdit.rw_type = this.data.rw_type
        if (this.data.server_record_cycle) {
          this.formVariableEdit.server_record_cycle = this.data.server_record_cycle.toString()
        }
        this.formVariableEdit.ten_id = this.data.ten_id
        this.formVariableEdit.upload = this.data.upload
        this.formVariableEdit.write_value = this.data.write_value
      },
      get_group () {
        new Group()
          .GET()
          .then((res) => {
            this.groups = res.data['data']
          })
      },
      post_variable () {
        new Variable()
          .POST({
            data: {
              group_id: this.group_id
            }
          })
          .then((res) => {
            this.variables = res.data['data']
          })
      },
      editSubmit (name) {
        this.loading = true
        this.$refs[name].validate((valid) => {
          if (valid) {
            new Variable()
              .PUT({
                data: this.formVariableEdit
              })
              .then((res) => {
                this.loading = false
                if (res.data['ok'] === 1) {
                  this.$Message.success(res.data['msg'])
                } else {
                  this.$Message.error(res.data['msg'])
                }
                this.$emit('close')
              })
          } else {
            this.$Message.error('表单验证失败!')
          }
        })
      },
      handleReset () {
        this.data2form()
        this.$Message.warning('已重置')
      },
      handleClean (name) {
        this.$refs[name].resetFields()
      },
      close () {
        this.$emit('close')
      }
    }
  }
</script>
