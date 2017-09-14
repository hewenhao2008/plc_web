<template>
  <Modal v-model="showCreate" title="新建" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formQuery" :model="formQuery" :label-width="80" inline>

      <FormItem label="组名称" prop="name">
        <Input v-model="formQuery.name" placeholder="请输入组名称"></Input>
      </FormItem>

    </Form>
    <div slot="footer">
      <Button type="success" :loading="loading" @click="createSubmit">提交</Button>
      <Button type="success" :loading="loading" @click="createSubmitContinue">提交并继续</Button>
      <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>
</template>

<script>
  import Query from '../models/actions/query_group'

  export default {
    data () {
      return {
        loading: false,
        formQuery: {
          name: null
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
      'showCreate',
      'groups'
    ],
    methods: {
      createSubmit () {
        this.loading = true
        new Query()
          .PUT({
            data: this.formQuery
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
      },
      createSubmitContinue () {
        this.loading = true
        new Query()
          .PUT({
            data: this.formQuery
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
      close () {
        this.$emit('close')
      }
    }
  }
</script>
