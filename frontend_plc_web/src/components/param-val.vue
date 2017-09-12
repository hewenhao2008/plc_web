<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">参数管理</Breadcrumb-item>
        <Breadcrumb-item href="param">工艺参数</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">

          <Table stripe highlight-row border :columns="columns" :data="params"></Table>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import PLC from '../models/actions/plc'
  import Group from '../models/actions/group'
  import Variable from '../models/actions/variable'
  import Param from '../models/actions/param'

  export default {
    data () {
      return {
        plc_id: '',
        group_id: '',
        groups: [],
        plcs: [],
        variables: [],
        params: [],
        columns: [
          {
            title: '序号',
            type: 'index',
            width: 60,
            align: 'center',
            fixed: 'left'
          }, {
            title: '参数名',
            key: 'param_name',
            align: 'center',
            sortable: true
          }, {
            title: '实时值',
            key: 'value',
            align: 'center',
            sortable: true,
            render: (h, params) => {
              return h('div', [
                h('Input', {
                  props: {
                    value: params.row.value
                  },
                  value: this.value
                })
              ])
            }
          }, {
            title: '单位',
            key: 'unit',
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
                      this.showCreate = true
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
                      this.model_delete(params.row.id)
                    }
                  }
                }, '删除')
              ])
            }
          }
        ]
      }
    },
    created () {
      this.get_param()
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_plc () {
        new PLC()
          .GET()
          .then((res) => {
            this.plcs = res.data['data']
          })
      },
      get_param () {
        new Param()
          .GET()
          .then((res) => {
            this.params = res.data['data']
          })
      },
      get_group () {
        new Group()
          .GET()
          .then((res) => {
            this.groups = res.data['data']
          })
      },
      post_variable () {
        new Variable()
          .POST({
            data: {group_id: this.group_id}
          })
          .then((res) => {
            this.variables = res.data['data']
          })
      },
      get_group_from_plc () {
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
      get_variable_from_group () {
        new Variable()
          .POST({
            data: {
              group_id: this.group_id
            }
          })
          .then((res) => {
            this.variables = res.data['data']
          })
      },
      change (page) {
        console.log(page)
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      },
      model_edit (stationId) {
        console.log('edit' + stationId)
      },
      model_delete (stationId) {
        console.log('delete' + stationId)
      },
      model_create () {
        console.log('create')
      },
      modify () {
        console.log('modify')
      }
    }
  }
</script>
