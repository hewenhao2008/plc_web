<style>
  #wrapp {
    width: 760px;
    text-align: left;
    font: normal 1em Arial;
    margin: 0 auto;
    padding: 0;
    color: black;
  }

  #wrapp h1 {
    font: bold 1.1em Arial;
    margin: 1.2em 0 0.5em 0;
    padding: 0;
  }

  .gnb h3 {
    font: normal 9px/14px Arial;
    text-align: right;
    margin: 0 10px 0 0;
    padding: 0
  }

  #wrapp p {
    font: normal 0.9em Arial;
    margin: 1em 0;
    padding: 0;
  }

  #wrapp h2 {
    font: bold 1em Arial;
  }

  code {
    width: 93%;
    font: normal 11px 'Courier New', Courier, Fixed;
    color: #000;
    display: block;
    padding: 1em;
    margin: 1em 0;
    background-color: #eee;
    border: 1px solid #d3d3d6;
    border-left-width: 5px;
    white-space: pre;
    overflow-x: auto;
  }

  .tickercontainer .mask { /* that serves as a mask. so you get a sort of padding both left and right */
    position: relative;
    left: 10px;
    top: 8px;
    width: 670px;
    overflow: hidden;
  }

  ul.newsticker { /* that's your list */
    position: relative;
    left: 750px;
    font: bold 10px Verdana;
    list-style-type: none;
    margin: 0;
    padding: 0;

  }

  ul.newsticker li {
    float: left; /* important: display inline gives incorrect results when you check for elem's width */
    margin: 0;
    padding: 0;
    background: #fff;
  }

  ul.newsticker a {
    white-space: nowrap;
    padding: 0;
    color: #ff0000;
    font: bold 10px Verdana;
    margin: 0 50px 0 0;
  }

  ul.newsticker span {
    color: #222222;
    margin: 0 10px 0 0;
  }

  .amount {
    height: 150px;
    width: 210px;
    background: #fff;
    margin-right: 15px;
    float: left;
    margin-top: 15px;
    border-radius: 3px;
    position: relative;
  }

  .amount > div {
    height: 35px;
    background: #dcf8f8;
    line-height: 35px;
    padding-left: 10px;
    position: relative;
  }

  .amount > p {
    margin-top: 10px;
    margin-left: 10px;
    font-size: 16px;
  }
</style>
<style>
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
</style>
<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="data">实时数据</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">
          <div class="input-group line left">

            <Select v-model="plc_id" style="width:100px" placeholder="选择PLC" filterable @on-change="post_group">
              <Option v-for="plc in plcs" :value="plc.id" :key="plc.id">{{ plc.plc_name }}</Option>
            </Select>

            <Select v-model="group_id" style="width:100px" placeholder="选择变量组" filterable @on-change="post_value">
              <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
            </Select>

            <br><br>

            <Input v-model="search" placeholder="输入变量名搜索..." style="width: 170px">
            <Icon type="search" slot="prepend"></Icon>
            </Input>
          </div>



          <!--数据显示模块-->
          <div style="height:auto;width:100%;">
            <div class="amount" v-cloak v-for="(v,k) in value">
              <img style="position: absolute;top:40px;left:70px;">
              <img style="position: absolute;top:70px;left:70px;">
              <div>{{v.group_name}}-{{v.variable_name}}
                <!--<img src="<?php echo STATICS_URL; ?>temp/img/圆圈.png" style="position:absolute;right:10px;top:-6px;">-->
              </div>

              <p>{{v.value}}</p>

              <p>{{change_time(v.time)}}</p>

            </div>


            <div style="clear:both;"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Value from '@/models/actions/value.js'
  import Alarm from '@/models/actions/alarm.js'
  import PLC from '@/models/actions/plc.js'
  import Group from '@/models/actions/group.js'

  export default {
    data () {
      return {
        alarm: 'text',
        plcs: '',
        plc_id: '',
        groups: '',
        group_id: '',
        value: '',
        search: ''
      }
    },
    created () {
//      todo 现在数据会逐个获取，改成异步方式
      this.get_value()
      this.get_alarm()
      this.get_group()
      this.get_plc()
    },
    mounted () {
      this.flush()
    },
    beforeDestroy () {
      clearInterval(this.get_value_timer)
    },
//    watch: {
//      plc_id: function () {
//        this.post_group()
//      },
//      group_id: function () {
//        this.post_value()
//      }
//    },
    methods: {
      flush () {
        this.get_value_timer = setInterval(this.get_value, 60000)
      },
      test () {
        console.log('a')
      },
      get_value () {
        new Value()
          .POST({
            data: {
              all_variable_id: true,
              limit: 1
            }
          })
          .then((res) => {
            this.value = res.data['data']
          })
      },
      get_alarm () {
        new Alarm()
          .GET()
          .then((res) => {
            this.alarm = res.data['data']
          })
      },
      get_plc () {
        new PLC()
          .GET()
          .then((res) => {
            this.plcs = res.data['data']
          })
      },
      get_group () {
        new Group()
          .GET()
          .then((res) => {
            this.groups = res.data['data']
          })
      },
      post_group () {
        new Group()
          .POST({
            data: {
              plc_id: this.plc_id
            }
          })
          .then((res) => {
            this.groups = res.data['data']
          })
      },
      post_value () {
        new Value()
          .POST({
            data: {
              group_id: this.group_id,
              limit: 1
            }
          })
          .then((res) => {
            this.value = res.data['data']
          })
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      }
    }
  }
</script>
