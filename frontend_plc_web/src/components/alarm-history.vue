<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">报警数据</Breadcrumb-item>
        <Breadcrumb-item href="alarm_now">历史报警</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">
          <a href="#" class=" btn btn-primary "><span class="glyphicon glyphicon-search" v-on:click="test()"></span></a>
          <a href="#" class=" btn btn-primary "><span class="glyphicon glyphicon-download"></span></a>
          <br/><br/>

          <Table stripe highlight-row border :columns="columns" :data="alarms"></Table>

          <Page :total="100" show-sizer show-elevator show-total @on-change="change"></Page>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import AlarmLog from '../models/actions/alarm_history'

  export default {
    data () {
      return {
        alarms: [],
        columns: [
          {
            title: '序号',
            type: 'index',
            width: 60,
            align: 'center'
          }, {
            title: '区域',
            key: 'station_name',
            sortable: true
          }, {
            title: '类型',
            key: 'alarm_type',
            sortable: true,
            render: (h, params) => {
              let data
              switch (params.row.alarm_type) {
                case 1:
                  data = '提示'
                  break
                case 2:
                  data = '警告'
                  break
                case 3:
                  data = '错误'
                  break
              }
              return h('div', data)
            }
          }, {
            title: '原因',
            key: 'note',
            sortable: true
          }, {
            title: '时间',
            width: 200,
            key: 'time',
            sortable: true,
            render: (h, params) => {
              return h('div', this.change_time(params.row.time))
            }
          }, {
            title: '状态',
            key: 'status',
            sortable: true,
            render: (h, params) => {
              let data
              switch (params.row.status) {
                case 0:
                  data = '正常'
                  break
                case 1:
                  data = '报错'
                  break
              }
              return h('div', data)
            }
          }
        ]
      }
    },
    created () {
      this.get_alarm()
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_alarm () {
        new AlarmLog()
          .GET()
          .then((res) => {
            this.alarms = res.data['data']
          })
      },
      change (page) {
        console.log(page)
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      }
    }
  }
</script>

