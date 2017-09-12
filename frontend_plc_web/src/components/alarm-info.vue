<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="alarm_info">报警参数信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">

          <Select v-model="plc_id" style="width:200px" placeholder="选择PLC" filterable>
            <Option v-for="plc in plcs" :value="plc.id" :key="plc.id">{{ plc.plc_name }}</Option>
          </Select>

          <Button type="primary" @click="showCreate = true">新建</Button>

          <br/><br/>

          <Table stripe highlight-row border :columns="columns" :data="alarm_info"></Table>

          <alarm-info-create :showCreate="showCreate" @close="closeCreate"></alarm-info-create>
          <alarm-info-edit :showEdit="showEdit" :data="data" @close="closeEdit"></alarm-info-edit>
          <alarm-info-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></alarm-info-delete>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import PLC from '../models/actions/plc'
  import AlarmInfo from '../models/actions/alarm_info'

  import alarmInfoCreate from './alarm_info_create.vue'
  import alarmInfoEdit from './alarm_info_edit.vue'
  import alarmInfoDelete from './alarm_info_delete.vue'

  export default {
    data () {
      return {
        plc_id: '',
        group_id: '',
        groups: [],
        plcs: [],
        alarm_info: [],
        showCreate: false,
        showEdit: false,
        showDelete: false,
        data: {},
        columns: [
          {
            title: '序号',
            type: 'index',
            width: 60,
            align: 'center',
            fixed: 'left'
          }, {
            title: '变量名',
            key: 'variable_name',
            align: 'center',
            sortable: true
          }, {
            title: '报警类型',
            key: 'alarm_type',
            align: 'center',
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
            title: '报警内容',
            key: 'note',
            align: 'center',
            sortable: true
          }, {
            title: '操作',
            key: 'action',
            width: 150,
            align: 'center',
            fixed: 'right',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.data = params.row
                      this.showEdit = true
                    }
                  }
                }, '编辑'),
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.data = params.row
                      this.showDelete = true
                    }
                  }
                }, '删除')
              ])
            }
          }
        ]
      }
    },
    components: {
      'alarmInfoCreate': alarmInfoCreate,
      'alarmInfoEdit': alarmInfoEdit,
      'alarmInfoDelete': alarmInfoDelete
    },
    created () {
      this.get_alarm_info()
      this.get_plc()
    },
    watch: {
      plc_id: function () {
        this.post_alarm_info()
      }
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_alarm_info () {
        new AlarmInfo()
          .GET()
          .then((res) => {
            this.alarm_info = res.data['data']
          })
      },
      post_alarm_info () {
        new AlarmInfo()
          .POST({
            data: {
              plc_id: this.plc_id
            }
          })
          .then((res) => {
            this.alarm_info = res.data['data']
          })
      },
      get_plc () {
        new PLC()
          .GET()
          .then((res) => {
            this.plcs = res.data['data']
          })
      },
      change (page) {
        console.log(page)
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      },
      closeCreate () {
        this.showCreate = false
        this.get_alarm_info()
      },
      closeEdit () {
        this.showEdit = false
        this.get_alarm_info()
      },
      closeDelete () {
        this.showDelete = false
        this.get_alarm_info()
      }
    }
  }
</script>
