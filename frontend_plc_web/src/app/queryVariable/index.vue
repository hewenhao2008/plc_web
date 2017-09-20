<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="/">系统信息</Breadcrumb-item>
        <Breadcrumb-item href="history_variable">曲线组变量信息</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="col-xs-10">

          <Select v-model="query_id" style="width:200px" placeholder="选择变量组" filterable>
            <Option v-for="query in queries" :value="query.id" :key="query.id">{{ query.name }}</Option>
          </Select>

          <Button type="primary"  @click="showAdd = true">添加</Button>
          <br/><br/>
          <Table stripe highlight-row border :columns="columns" :data="query_variables"></Table>

          <query-add :query_id='query_id' :showAdd="showAdd" @close="closeAdd"></query-add>
          <query-var-delete :query_id='query_id' :variable_id="data.var_id" :showDelete="showDelete" @close="closeDelete"></query-var-delete>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Query from '@/models/actions/query_group'

  import queryAdd from './components/query_variable_add'
  import queryVarDelete from './components/query_variable_delete'

  export default {
    data () {
      return {
        queries: [],
        query_id: '',
        query_variables: [],
        showAdd: false,
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
            key: 'var_name',
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
      'queryAdd': queryAdd,
      'queryVarDelete': queryVarDelete
    },
    created () {
      this.get_query()
    },
    watch: {
      query_id: function () {
        this.post_variable()
      }
    },
    methods: {
      flush () {
        setInterval(this.get_value(), 5000)
      },
      get_query () {
        new Query()
          .GET()
          .then((res) => {
            this.queries = res.data['data']
          })
      },
      post_variable () {
        new Query()
          .POST({
            data: {
              id: this.query_id
            }
          })
          .then((res) => {
            this.query_variables = res.data['data'][0]['variable']
          })
      },
      change (page) {
        console.log(page)
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      },
      closeAdd () {
        this.showAdd = false
        this.post_variable()
      },
      closeDelete () {
        this.showDelete = false
        this.post_variable()
      }
    }
  }
</script>

