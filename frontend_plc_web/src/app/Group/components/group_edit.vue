<template>
  <Modal v-model="showEdit" title="编辑" :mask-closable="false" :closable="false">

    <div slot="header">
      <span style="float: left">编辑</span>
      <span style="float: right">
      <Button type="ghost" size="small" @click="close" style="margin-left: 8px" inline>
        <Icon type="close"></Icon>
      </Button>
        </span>
      <br><br>
    </div>

    <Form ref="formGroup" :model="formGroup" :label-width="80">

      <FormItem label="变量组名" prop="group_name">
        <Input v-model="formGroup.group_name" placeholder="请输入变量组名"></Input>
      </FormItem>

      <FormItem label="PLC名" prop="plc_id">
        <Select transfer v-model="formGroup.plc_id" style="width:100px" placeholder="选择PLC"
                filterable>
          <Option v-for="plc in plcs" :value="plc.id" :key="plc.id">{{ plc.plc_name }}</Option>
        </Select>
      </FormItem>


      <FormItem label="上传周期" prop="upload_cycle">
        <Select transfer v-model="formGroup.upload_cycle" style="width:100px" placeholder="选择上传周期"
                filterable>
          <Option value="60">一分钟</Option>
          <Option value="300">五分钟</Option>
          <Option value="600">十分钟</Option>
          <Option value="900">十五分钟</Option>
          <Option value="1800">三十分钟</Option>
          <Option value="3600">一小时</Option>
        </Select>
      </FormItem>

      <FormItem label="备注" prop="note">
        <Input v-model="formGroup.note" placeholder="请输入备注"></Input>
      </FormItem>

    </Form>

    <div slot="footer">
      <Button type="success" :loading="loading" @click="editSubmit('formGroup')">提交</Button>
      <Button type="ghost" @click="handleReset()" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="handleClean('formGroup')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>
</template>

<script>
  import Group from '@/models/actions/group'

  export default {
    data () {
      return {
        loading: false,
        formGroup: {
          id: null,
          group_name: null,
          plc_id: null,
          upload_cycle: null,
          note: null
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
      'plcs',
      'data'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    methods: {
      data2form () {
        this.formGroup.id = this.data.id
        this.formGroup.group_name = this.data.group_name
        this.formGroup.plc_id = this.data.plc_id
        if (this.data.upload_cycle) {
          this.formGroup.upload_cycle = this.data.upload_cycle.toString()
        }
      },
      editSubmit (name) {
        this.loading = true
        this.$refs[name].validate((valid) => {
          if (valid) {
            new Group()
              .PUT({
                data: this.formGroup
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
