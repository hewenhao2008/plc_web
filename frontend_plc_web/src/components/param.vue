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
          <div class="panel panel-default">
            <div class="panel-heading">
              <h3 class="panel-title">搜索 （选择参数，查询的日期段）</h3>
            </div>
            <div class="panel-body">
              <div class="row">
                <div class="col-lg-10 col-sm-10 col-xs-12" id="sele">

                  <div class="input-group line left">
                  </div>

                  <Select v-model="plc_id" style="width:200px" @on-change="post_group">
                    <Option v-for="plc in plcs" :value="plc.id" :key="plc.id">{{ plc.plc_name }}</Option>
                  </Select>

                  <Select v-model="group_id" style="width:200px" @on-change="post_variable">
                    <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
                  </Select>

                  <br/><br/>
                </div>
              </div>
            </div>
          </div>

          <Table stripe highlight-row border :columns="columns" :data="variables"></Table>

          <param-create :variable_id='data.id' :showCreate="showCreate" @close="closeCreate"></param-create>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import PLC from '../models/actions/plc'
  import Group from '../models/actions/group'
  import Variable from '../models/actions/variable'

  import paramCreate from './param_create'

  export default {
    data () {
      return {
        plc_id: '',
        group_id: '',
        groups: [],
        plcs: [],
        variables: [],
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
            title: '变量组名',
            key: 'group_name',
            align: 'center',
            sortable: true
          }, {
            title: '备注',
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
                      this.showCreate = true
                    }
                  }
                }, '添加参数')
              ])
            }
          }
        ]
      }
    },
    components: {
      'paramCreate': paramCreate
    },
    created () {
      this.get_variable()
      this.get_plc()
      this.get_group()
    },
    methods: {
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
            data: {group_id: this.group_id}
          })
          .then((res) => {
            this.variables = res.data['data']
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
