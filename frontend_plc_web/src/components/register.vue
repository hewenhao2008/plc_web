<template>
  <Card class="login">
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
      <FormItem label="用户名" prop="username">
        <Input v-model="formValidate.username" placeholder="请输入用户名"></Input>
      </FormItem>
      <FormItem label="邮箱" prop="email">
        <Input v-model="formValidate.email" placeholder="请输入邮箱"></Input>
      </FormItem>
      <FormItem label="密码" prop="password">
        <Input v-model="formValidate.password" placeholder="请输入密码"></Input>
      </FormItem>
      <FormItem label="密码确认" prop="confirm">
        <Input v-model="formValidate.confirm" placeholder="请再次输入密码"></Input>
      </FormItem>


      <FormItem>
        <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
      </FormItem>
    </Form>
  </Card>
</template>
<script>
//  import auth from '../utils/auth'
  import Model from '../models/actions/register'

  export default {
    data () {
      return {
        formValidate: {
          username: '',
          email: '',
          password: '',
          confirm: ''
        },
        ruleValidate: {
          username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'}
          ],
          email: [
            {required: true, message: '邮箱不能为空', trigger: 'blur'},
            {type: 'email', message: '邮箱格式不正确', trigger: 'blur'}
          ],
          password: [
            {required: true, type: 'string', min: 6, message: '密码最少6个字符', trigger: 'blur'},
            {type: 'string', max: 32, message: '密码最多32个字符', trigger: 'blur'}
          ],
          confirm: [
            {required: true, type: 'string', min: 6, message: '密码最少6个字符', trigger: 'blur'},
            {type: 'string', max: 32, message: '密码最多32个字符', trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            new Model()
              .PUT({
                data: this.formValidate
              })
              .then((res) => {
                this.$Message.success(res.data['msg'])
//                this.$Message.success('注册成功!')
//                auth.login(res.data.data)
                this.$route.push('/')
              })
          } else {
            this.$Message.error('表单验证失败!')
          }
        })
      }
    }
  }
</script>
