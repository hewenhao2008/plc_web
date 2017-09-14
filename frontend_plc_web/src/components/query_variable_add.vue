<template>
  <Modal v-model="showAdd" title="添加" :mask-closable="false" :closable="false">

    <Form :label-width="80" inline>
      <Select transfer v-model="group_id" style="width:100px" placeholder="选择变量组"
              filterable @on-change="post_variable">
        <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
      </Select>

      <Select transfer v-model="variable_id" style="width:100px" placeholder="选择变量"
              filterable>
        <Option v-for="variable in variables" :value="variable.id" :key="variable.id">{{ variable.variable_name }}
        </Option>
      </Select>
    </Form>

    <div slot="footer">
      <Button type="success" :loading="loading" @click="addSubmit">提交</Button>
      <Button type="success" :loading="loading" @click="createSubmitContinue">提交并继续</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>
</template>

<script>
  import Group from '../models/actions/group'
  import Variable from '../models/actions/variable'
  import Query from '../models/actions/query_group'

  export default {
    data () {
      return {
        loading: false,
        variable_id: '',
        group_id: '',
        groups: [],
        variables: []
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
      'showAdd',
      'query_id'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    created () {
      this.get_group()
    },
    methods: {
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
      addSubmit () {
        this.createSubmitContinue()
        this.$emit('close')
      },
      createSubmitContinue () {
        this.loading = true
        new Query()
          .PUT({
            data: {
              id: this.query_id,
              variable_id: this.variable_id
            }
          })
          .then((res) => {
            this.loading = false
            if (res.data['ok'] === 1) {
              this.$Message.success(res.data['msg'])
            } else {
              this.$Message.error(res.data['msg'])
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
