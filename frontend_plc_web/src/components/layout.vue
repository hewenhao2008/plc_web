<style>
  .layout {
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }

  .layout-breadcrumb {
    padding: 10px 15px 0;
  }

  .layout-content {
    min-height: 200px;
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
  }

  .layout-content-main {
    padding: 10px;
  }

  .layout-copy {
    text-align: center;
    padding: 10px 0 20px;
    color: #9ea7b4;
  }

  .layout-menu-left {
    /*background: #464c5b;*/
    background: #fff;
  }

  .layout-header {
    height: 60px;
    background: #fff;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .1);
  }

  .layout-logo-left {
    width: 90%;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    margin: 15px auto;
  }

  .layout-ceiling-main a {
    color: #9ba7b5;
  }

  .layout-hide-text .layout-text {
    display: none;
  }

  .ivu-col {
    transition: width .2s ease-in-out;
  }
</style>
<template>
  <div>
  <header-view></header-view>
  <div class="layout" :class="{'layout-hide-text': spanLeft < 5}">

    <Row type="flex">
      <i-col :span="spanLeft" class="layout-menu-left">
        <!--<Affix :offset-top="50">-->

        <Menu active-name="1" theme="light" width="auto">
          <!--<div class="layout-logo-left"></div>-->


          <router-link to="/data">
            <Menu-item name="1">
              <Icon type="ios-navigate" :size="iconSize"></Icon>
              <span class="layout-text">实时数据</span>
            </Menu-item>
          </router-link>


          <router-link to="/history">
            <Menu-item name="2">
              <Icon type="ios-keypad" :size="iconSize"></Icon>
              <span class="layout-text">历史数据</span>
              <!--<comp1></comp1>-->
            </Menu-item>
          </router-link>


          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>
              报警数据
            </template>

            <router-link to="/alarm_now">
              <MenuItem name="3-1">最新报警</MenuItem>
            </router-link>

            <router-link to="/alarm_history">
              <MenuItem name="3-2">历史报警</MenuItem>
            </router-link>

          </Submenu>


          <Submenu name="4">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>
              系统信息
            </template>

            <router-link to="/station">
              <MenuItem name="4-1">站点信息</MenuItem>
            </router-link>

            <router-link to="/plc">
              <MenuItem name="4-2">PLC信息</MenuItem>
            </router-link>

            <router-link to="/group">
              <MenuItem name="4-3">变量组信息</MenuItem>
            </router-link>

            <router-link to="/variable">
              <MenuItem name="4-4">变量信息</MenuItem>
            </router-link>

            <router-link to="/query_group">
              <MenuItem name="4-5">历史曲线组信息</MenuItem>
            </router-link>

            <router-link to="/query_variable">
              <MenuItem name="4-6">曲线组变量信息</MenuItem>
            </router-link>

            <router-link to="/alarm_info">
              <MenuItem name="4-7">报警参数信息</MenuItem>
            </router-link>

          </Submenu>


          <Submenu name="5">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>
              参数管理
            </template>

            <router-link to="/param">
              <MenuItem name="5-1">工艺参数</MenuItem>
            </router-link>

            <router-link to="/param_val">
              <MenuItem name="5-2">参数修改</MenuItem>
            </router-link>

          </Submenu>
        </Menu>
        <!--</Affix>-->
      </i-col>

      <i-col :span="spanRight">
        <div class="layout-header">
          <i-button type="text" @click="toggleClick">
            <Icon type="navicon" size="32"></Icon>
          </i-button>
        </div>
          <router-view></router-view>
      </i-col>
    </Row>
    <!--<div class="layout-copy">-->
    <!--版权所有&copy;内蒙古博悦信息技术有限公司-->
    <!--</div>-->
  </div>
    </div>
</template>

<script>
  import bread from './breadcrumb-view.vue'
  import header from './new_header.vue'
  import Transfer from '../../node_modules/iview/src/components/transfer/transfer'

  export default {
    data () {
      return {
        spanLeft: 5,
        spanRight: 19
      }
    },
    components: {
      Transfer,
      'bread-view': bread,
      'header-view': header
    },
    computed: {
      iconSize () {
        return this.spanLeft === 5 ? 14 : 24
      }
    },
    methods: {
      toggleClick () {
        if (this.spanLeft === 5) {
          this.spanLeft = 2
          this.spanRight = 22
        } else {
          this.spanLeft = 5
          this.spanRight = 19
        }
      }
    }
  }
</script>
