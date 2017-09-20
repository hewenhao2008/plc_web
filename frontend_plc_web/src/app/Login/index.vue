<template>
  <Card class="login" dis-hover>
    <p slot="title">后台管理系统</p>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="60" label-position="left">
      <Form-item label="用户" prop="username">
        <Input v-model="formValidate.username" placeholder="请输入用户" @on-enter="handleLogin"/>
      </Form-item>
      <Form-item label="密码" prop="password">
        <!--@on-enter="submit"-->
        <Input type="password" v-model="formValidate.password" placeholder="请输入密码" @on-enter="handleLogin"></Input>
      </Form-item>
      <Form-item>
        <Button type="primary" @click="handleLogin">登录</Button>
      </Form-item>
    </Form>
  </Card>
</template>

<script>
  import auth from '@/utils/auth'
  import Model from '@/models/actions/login'
//  import REST from '@/utils/rest'

  export default {
    name: 'login',
    data () {
      return {
        formValidate: {
          username: 'yakumo17s',
          password: 'touhou'
        },
        ruleValidate: {
          username: [
            {
              required: true,
              message: '用户不能为空'
            }
          ],
          password: [
            {
              required: true,
              message: '密码不能为空'
            }
          ]
        }
      }
    },
    methods: {
      handleLogin () {
        this.$refs.formValidate.validate((valid) => {
          if (valid) {
            new Model()
              .POST({
                data: this.formValidate
              })
              .then((res) => {
//                console.log(res.data.token)
//                this.$store.token = res.data.token
//                console.log(this.$store.token)
//                REST.constructor.addHeaders({'token': res.data.token})
                this.$Message.success('登录成功')
                auth.login(res.data)
                this.$router.push('/')
              })
          }
        })
      }
    }
  }
</script>

<style lang="scss" scoped src="./styles/index.scss">
</style>

