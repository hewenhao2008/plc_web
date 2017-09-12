<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="plc">PLC信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">

          <Select v-model="station_id" style="width:100px" placeholder="选择站点" filterable>
            <Option v-for="station in stations" :value="station.id" :key="station.id">{{ station.station_name }}
            </Option>
          </Select>

          <Button type="primary" @click="showCreate = true">新建</Button>
          <br/><br/>

          <Table stripe highlight-row border :columns="columns" :data="plcs"></Table>

          <plcCreate :stations="stations" :showCreate="showCreate" @close="closeCreate"></plcCreate>
          <plc-edit :stations="stations" :showEdit="showEdit" :data="data" @close="closeEdit"></plc-edit>
          <plc-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></plc-delete>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Station from '../models/actions/station'
  import PLC from '../models/actions/plc'

  import plcCreate from './plc_create.vue'
  import plcEdit from './plc_edit.vue'
  import plcDelete from './plc_delete.vue'

  export default {
    data () {
      return {
        stations: [],
        station_id: '',
        plc_id: '',
        plcs: [],
        showCreate: false,
        showEdit: false,
        showDelete: false,
        data: {},
        columns: [
          {
            title: '序号',
            type: 'index',
            width: 50,
            align: 'center',
            fixed: 'left'
          }, {
            title: 'PLC名称',
            key: 'plc_name',
            sortable: true
          }, {
            title: '站点名称',
            key: 'station_name',
            sortable: true
          }, {
            title: '备注',
            key: 'note',
            sortable: true
          }, {
            title: 'IP地址',
            key: 'ip',
            width: 120,
            sortable: true
          }, {
            title: 'MPI',
            key: 'mpi',
            sortable: true
          }, {
            title: '通讯类型',
            key: 'type',
            sortable: true,
            render: (h, params) => {
              let data
              switch (params.row.type) {
                case 1:
                  data = '以太网'
                  break
                case 2:
                  data = 'MPI'
                  break
                case 3:
                  data = 'S7ONLINE'
                  break
              }
              return h('div', data)
            }
          }, {
            title: 'PLC型号',
            key: 'plc_type',
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
      'plcCreate': plcCreate,
      'plcEdit': plcEdit,
      'plcDelete': plcDelete
    },
    created () {
      this.get_plc()
      this.get_station()
    },
    watch: {
      station_id: function () {
        this.post_plc()
      }
    },
    methods: {
      get_station () {
        new Station()
          .GET()
          .then((res) => {
            this.stations = res.data['data']
          })
      },
      get_plc () {
        new PLC()
          .GET()
          .then((res) => {
            this.plcs = res.data['data']
          })
      },
      post_plc () {
        new PLC()
          .POST({
            data: {station_id: this.station_id}
          })
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
        this.get_plc()
      },
      closeEdit () {
        this.showEdit = false
        this.get_plc()
      },
      closeDelete () {
        this.showDelete = false
        this.get_plc()
      }
    }
  }
</script>
