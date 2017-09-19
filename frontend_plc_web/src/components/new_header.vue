<template>
  <Row>
    <Menu mode="horizontal" theme="light" active-name="1">

      <MenuItem name="1">
        <Icon type="ios-paper"></Icon>
        内容管理
      </MenuItem>
      <MenuItem name="2">
        <Icon type="ios-people"></Icon>
        用户管理
      </MenuItem>
      <Submenu name="3">
        <template slot="title">
          <Icon type="stats-bars"></Icon>
          统计分析
        </template>
        <MenuGroup title="使用">
          <MenuItem name="3-1">新增和启动</MenuItem>
          <MenuItem name="3-2">活跃分析</MenuItem>
          <MenuItem name="3-3">时段分析</MenuItem>
        </MenuGroup>
        <MenuGroup title="留存">
          <MenuItem name="3-4">用户留存</MenuItem>
          <MenuItem name="3-5">流失用户</MenuItem>
        </MenuGroup>
      </Submenu>
      <MenuItem name="4">
        <Icon type="settings"></Icon>
        综合设置
      </MenuItem>
      <Row type="flex" justify="end" class="code-row-bg">
        <Col span="8">
        <div v-if="is_login">
          <Submenu name="user">
            <template slot="title">
              <!--<Icon type="stats-bars"></Icon>-->
              <v-gravatar :email="email"></v-gravatar>
              {{ username }}
            </template>
            <MenuItem name="3-1">用户资料</MenuItem>
            <!--<router-link to="/logout">-->
            <MenuItem name="logout"><p @click="handleLogout">退出登录</p></MenuItem>
            <!--</router-link>-->
          </Submenu>
        </div>
        <div v-else>
          <router-link to="/login">
            <MenuItem name="login">
              <Icon type="settings"></Icon>
              登录
            </MenuItem>
          </router-link>
        </div>
        </Col>
      </Row>

    </Menu>
  </Row>

</template>
<script>
  import Gravatar from 'vue-gravatar'
  import auth from '@/utils/auth'
  import storage from '@/utils/helpers/storageLite'

  export default {
    data () {
      return {
        is_login: '',
        username: '',
        email: ''
      }
    },
    components: {
      'v-gravatar': Gravatar
    },
    created () {
      this.confirm_login()
    },
    watch: {
      is_login: function () {
        this.confirm_login()
      }
    },
    methods: {
      confirm_login () {
//        this.$set(this.is_login, !!auth.loggedIn())
        this.is_login = auth.loggedIn()
        if (this.is_login) {
          this.username = storage.get('username')
          this.email = storage.get('email')
        }
      },
      handleLogout () {
//        this.$router.push('/logout')
        if (this.is_login) {
          auth.logout()
        }
        this.$Message.success('退出成功')
        this.confirm_login()
      }
    }
  }
</script>
