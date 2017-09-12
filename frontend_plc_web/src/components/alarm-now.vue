<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="alarm_now">最新报警</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">
          <Table stripe highlight-row border :columns="columns" :data="alarms"></Table>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Alarm from '../models/actions/alarm.js'

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
            key: 'time',
            sortable: true,
            render: (h, params) => {
              return h('div', this.change_time(params.row.time))
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
        new Alarm()
          .GET()
          .then((res) => {
            this.alarms = res.data['data']
          })
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      }
    }
  }
</script>
