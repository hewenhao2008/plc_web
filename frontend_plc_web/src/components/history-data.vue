<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
        <Breadcrumb-item href="history">历史数据</Breadcrumb-item>
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

                  <Select v-model="search" style="width:200px">
                  <Option v-for="que in querys" :value="que.id" :key="que.id">{{ que.name }}</Option>
                  </Select>
                  <br>

                  <CheckboxGroup v-model="variable">
                    <Checkbox v-for="vari in variables" v-bind:label="vari.var_id" :key="vari.id">{{vari.var_name}}
                    </Checkbox>
                  </CheckboxGroup>
                  <br>

                  <DatePicker type="datetimerange" placeholder="选择日期和时间" style="width: 300px"
                              v-model="time"></DatePicker>
                  <br><br>


                  <Button type="primary" shape="circle" icon="ios-search" v-on:click="get_value">搜索</Button>
                </div>
              </div>
            </div>
          </div>

          <div id="container" style="min-width:400px;height:400px"></div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import HistoryGroup from '../models/actions/query_group'
  import Value from '../models/actions/value.js'

  export default {
    data () {
      return {
        querys: '',
        query: '',
        search: '',
        variables: '',
        variable: [],
        time: '',
        value: ''
      }
    },
    created () {
      this.get_query()
    },
    watch: {
      search: function () {
        this.get_query_variable()
//        this.variable = this.querys['data'][this.query]
      }
    },
    methods: {
      get_query () {
        new HistoryGroup()
          .GET()
          .then((res) => {
            this.querys = res.data['data']
//            this.variables = res.data['data'][0]['variable']
          })
      },
      get_query_variable () {
        new HistoryGroup()
          .POST({
            data: {id: this.search}
          })
          .then((res) => {
            this.variables = res.data['data'][0]['variable']
          })
      },
      get_value () {
        new Value()
          .POST({
            data: {
              variable_id: this.variable,
              min_time: Date.parse(this.time[0]) / 1000,
              max_time: Date.parse(this.time[1]) / 1000
            }
          })
          .then((res) => {
            this.value = res.data['data']
          })
      }
    }
  }
</script>
