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

          <param_edit :showEdit="showEdit" :data="data" @close="closeEdit"></param_edit>
          <param_delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></param_delete>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Param from '../models/actions/param'
  import Variable from '../models/actions/variable'

  import paramDelete from './param_delete'
  import paramEdit from './param_edit.vue'

  export default {
    data () {
      return {
        plc_id: '',
        group_id: '',
        groups: [],
        plcs: [],
        variables: [],
        params: [],
        value: '',
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
              let self = this
              return h('div', [
                h('Input', {
                  props: {
                    real_time_value: params.row.value
                  },
                  on: {
                    input: function (value) {
                      self.value = value
                    }
                  },
                  value: this.real_time_value
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
            width: 200,
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
                      console.log(this.data.variable_id, this.data.value)
                      this.modify_value()
                    }
                  }
                }, '保存'),
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
      'param_delete': paramDelete,
      'param_edit': paramEdit
    },
    created () {
      this.get_param()
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_param () {
        new Param()
          .GET()
          .then((res) => {
            this.params = res.data['data']
          })
      },
      modify_value () {
        this.loading = true
        new Variable()
          .PUT({
            data: {
              id: this.data.variable_id,
              write_value: this.value
            }
          })
          .then((res) => {
            this.loading = false
            if (res.data['ok'] === 1) {
              this.$Message.success(res.data['msg'])
            } else {
              this.$Message.error(res.data['msg'])
            }
          })
      },
      closeCreate () {
        this.showCreate = false
        this.get_param()
      },
      closeEdit () {
        this.showEdit = false
        this.get_param()
      },
      closeDelete () {
        this.showDelete = false
        this.get_param()
      }
    }
  }
</script>
