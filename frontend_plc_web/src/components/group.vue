<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="group">变量组信息</Breadcrumb-item>
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

          <Table stripe highlight-row border :columns="columns" :data="groups"></Table>

          <group-create :plcs="plcs" :showCreate="showCreate" @close="closeCreate"></group-create>
          <group-edit :plcs="plcs" :showEdit="showEdit" :data="data" @close="closeEdit"></group-edit>
          <group-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></group-delete>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Group from '../models/actions/group'
  import PLC from '../models/actions/plc'

  import groupCreate from './group_create.vue'
  import groupEdit from './group_edit.vue'
  import groupDelete from './group_delete.vue'

  export default {
    data () {
      return {
        plc_id: '',
        group_id: '',
        groups: [],
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
            title: '变量组名称',
            key: 'group_name',
            sortable: true
          }, {
            title: 'PLC名称',
            key: 'plc_name',
            sortable: true
          }, {
            title: '备注',
            key: 'note',
            sortable: true
          }, {
            title: '上传周期',
            key: 'upload_cycle',
            width: 120,
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
      'groupCreate': groupCreate,
      'groupEdit': groupEdit,
      'groupDelete': groupDelete
    },
    created () {
      this.get_group()
      this.get_plc()
    },
    watch: {
      plc_id: function () {
        this.post_group()
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
        this.get_group()
      },
      closeEdit () {
        this.showEdit = false
        this.get_group()
      },
      closeDelete () {
        this.showDelete = false
        this.get_group()
      }
    }
  }
</script>
