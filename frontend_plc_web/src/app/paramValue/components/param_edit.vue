<template>
  <Modal v-model="showEdit" title="编辑" :mask-closable="false" :closable="false">

    <div slot="header">
      <span style="float: left">编辑</span>
      <span style="float: right">
      <Button type="ghost" size="small" @click="close" style="margin-left: 8px">
        <Icon type="close"></Icon>
      </Button>
        </span>
      <br><br>
    </div>

    <Form ref="formParam" :model="formParam" :label-width="80" inline>

      <FormItem label="参数名称" prop="param_name">
        <Input v-model="formParam.param_name" placeholder="请输入参数名"></Input>
      </FormItem>

      <FormItem label="单位名称" prop="unit">
        <Input v-model="formParam.unit" placeholder="请输入单位名称"></Input>
      </FormItem>

      <

    </Form>

    <div slot="footer">
      <Button type="success" :loading="loading" @click="editSubmit('formParam')">提交</Button>
      <Button type="ghost" @click="handleReset()" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="handleClean('formParam')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>

</template>

<script>
  import Group from '@/models/actions/group'
  import Variable from '@/models/actions/variable'
  import Param from '@/models/actions/param'

  export default {
    data () {
      return {
        loading: false,
        formParam: {
          id: null,
          param_name: null,
          unit: null,
          variable_id: null
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
      'data'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    methods: {
      data2form () {
        this.formParam.id = this.data.id
        this.formParam.param_name = this.data.param_name
        this.formParam.unit = this.data.unit
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
            new Param()
              .PUT({
                data: this.formParam
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
