<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="station">站点信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">
          <div class="input-group line left">
          </div>
          <Button type="primary" @click="showCreate = true">新建</Button>
          <Button type="primary" @click="showUpload = true">修改生效</Button>
          <br/><br/>

          <Table stripe highlight-row border :columns="columns" :data="stations"></Table>

          <station-create :showCreate="showCreate" @close="closeCreate"></station-create>
          <station-edit :showEdit="showEdit" :data="data" @close="closeEdit"></station-edit>
          <station-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></station-delete>
          <upload :stations="stations" :showUpload="showUpload" @close="closeUpload"></upload>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Station from '../models/actions/station'

  import stationCreate from './station_create.vue'
  import stationEdit from './station_edit.vue'
  import stationDelete from './station_delete.vue'
  import upload from './upload.vue'

  export default {
    data () {
      return {
        station_id: '',
        stations: [],
        showCreate: false,
        showEdit: false,
        showDelete: false,
        showUpload: false,
        data: {},
        columns: [
          {
            title: '序号',
            type: 'index',
            width: 60,
            align: 'center',
            fixed: 'left'
          }, {
            title: '名称',
            key: 'station_name',
            sortable: true
          }, {
            title: 'MAC地址',
            key: 'mac',
            sortable: true
          }, {
            title: 'IP地址',
            key: 'ip',
            sortable: true
          }, {
            title: '备注',
            key: 'note',
            sortable: true
          }, {
            title: 'PLC数量',
            key: 'plc_count',
            sortable: true
          }, {
            title: '站点标识',
            key: 'id_num',
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
      'stationCreate': stationCreate,
      'stationEdit': stationEdit,
      'stationDelete': stationDelete,
      'upload': upload
    },
    created () {
      this.get_station()
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_station () {
        new Station()
          .GET()
          .then((res) => {
            this.stations = res.data['data']
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
        this.get_station()
      },
      closeEdit () {
        this.showEdit = false
        this.get_station()
      },
      closeDelete () {
        this.showDelete = false
        this.get_station()
      },
      closeUpload () {
        this.showUpload = false
      }
    }
  }
</script>
