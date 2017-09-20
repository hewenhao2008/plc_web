<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="query_group">历史曲线组信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">
          <Button type="primary" @click="showCreate = true">新建</Button>

          <br/><br/>

          <Table stripe highlight-row border :columns="columns" :data="queries"></Table>

          <query-create :showCreate="showCreate" @close="closeCreate"></query-create>
          <query-edit :showEdit="showEdit" :data="data" @close="closeEdit"></query-edit>
          <query-delete :showDelete="showDelete" :id="data.id" @close="closeDelete"></query-delete>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Query from '@/models/actions/query_group'

  import queryCreate from './components/query_group_create.vue'
  import queryEdit from './components/query_group_edit.vue'
  import queryDelete from './components/query_group_delete.vue'

  export default {
    data () {
      return {
        queries: [],
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
            title: '曲线组名',
            key: 'name',
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
      'queryCreate': queryCreate,
      'queryEdit': queryEdit,
      'queryDelete': queryDelete
    },
    created () {
      this.get_query()
    },
    methods: {
      get_query () {
        new Query()
          .GET()
          .then((res) => {
            this.queries = res.data['data']
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
        this.get_query()
      },
      closeEdit () {
        this.showEdit = false
        this.get_query()
      },
      closeDelete () {
        this.showDelete = false
        this.get_query()
      }
    }
  }
</script>

