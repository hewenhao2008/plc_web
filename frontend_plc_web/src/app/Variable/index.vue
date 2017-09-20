<style>
  .ivu-select-dropdown {
    position: absolute !important;
  }
</style>

<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="alarm_info">变量信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">

          <Select v-model="group_id" style="width:100px" placeholder="选择变量组" filterable>
            <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
          </Select>

          <Button type="primary" @click="showCreate = true">新建</Button>
          <br><br>

          <Table stripe highlight-row border :columns="columns" :data="variables"></Table>


          <variableCreate :groups="groups" :showCreate="showCreate" @close="closeCreate"></variableCreate>
          <variable-edit :groups="groups" :showEdit="showEdit" :data="data" @close="closeEdit"></variable-edit>
          <variable-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></variable-delete>

        </div>
      </div>
    </div>
  </div>
</template>


<script>
  import PLC from '@/models/actions/plc'
  import Group from '@/models/actions/group'
  import Variable from '@/models/actions/variable'

  import variableCreate from './components/variable_create.vue'
  import variableEdit from './components/variable_edit.vue'
  import variableDelete from './components/variable_delete.vue'

  export default {
    data () {
      return {
        group_id: '',
        groups: [],
        variables: [],
        variable_id: '',
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
            title: '变量组名',
            key: 'group_name',
            align: 'center',
            sortable: true
          }, {
            title: '变量名',
            key: 'variable_name',
            align: 'center',
            sortable: true
          }, {
            title: '地址',
            key: 'address',
            align: 'center',
            sortable: true
          }, {
            title: '上传周期',
            key: 'server_record_cycle',
            align: 'center',
            sortable: true
          }, {
            title: '备注',
            key: 'note',
            align: 'center'
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
                    size: 'small',
                    value: params.row
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
      'variableCreate': variableCreate,
      'variableEdit': variableEdit,
      'variableDelete': variableDelete
    },
    created () {
      this.get_variable()
      this.get_group()
    },
    watch: {
      group_id: function () {
        this.post_variable()
      }
    },
    methods: {
      get_group () {
        new Group()
          .GET()
          .then((res) => {
            this.groups = res.data['data']
          })
      },
      get_plc () {
        new PLC()
          .GET()
          .then((res) => {
            this.plcs = res.data['data']
          })
      },
      get_variable () {
        new Variable()
          .GET()
          .then((res) => {
            this.variables = res.data['data']
          })
      },
      post_variable () {
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
      closeCreate () {
        this.showCreate = false
        this.get_variable()
      },
      closeEdit () {
        this.showEdit = false
        this.get_variable()
      },
      closeDelete () {
        this.showDelete = false
        this.get_variable()
      }
    }
  }
</script>

