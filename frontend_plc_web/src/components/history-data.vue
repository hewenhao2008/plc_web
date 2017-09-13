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

                  <Select v-model="query_id" style="width:200px" @on-change="post_query_variable">
                    <Option v-for="que in querys" :value="que.id" :key="que.id">{{ que.name }}</Option>
                  </Select>
                  <br>

                  <CheckboxGroup v-model="variable_id">
                    <Checkbox v-for="vari in variables" :label="vari.var_id" :key="vari.id">{{vari.var_name}}
                    </Checkbox>
                  </CheckboxGroup>
                  <br>

                  <DatePicker type="datetimerange" placeholder="选择日期和时间" style="width: 300px"
                              v-model="time"></DatePicker>
                  <br><br>


                  <Button type="primary" shape="circle" icon="ios-search" @click="get_value">搜索</Button>
                </div>
              </div>
            </div>
          </div>

          <div id="container" style="min-width:400px;height:400px"></div>
          <div id="test" style="min-width:400px;height:400px"></div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
  import HistoryGroup from '../models/actions/query_group'
  import Value from '../models/actions/value.js'

  let echarts = require('echarts')
  //  let myChart = echarts.init(document.getElementById('main'))

  export default {
    data () {
      return {
        querys: [],
        query_id: '',
        variables: [],
        variable_id: [],
        variable_name: [],
        time: '',
        value: [],
        base: new Date(1968, 9, 3),
        oneDay: 24 * 3600 * 1000,
        date: [],
        data: [],
        chart: null,
        legends: [],
        Series: [],
        arr: [],
        Item: {
          name: '',
          type: 'line',
          data: ''
        },
        options: {
          title: {
            text: '历史曲线'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: []
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
          },
          yAxis: {
            type: 'value'
          },
          dataZoom: [{
            type: 'inside',
            start: 0,
            end: 100
          }, {
            show: true,
            type: 'slider',
            y: '90%',
            start: 50,
            end: 100
          }],
          series: []
        }
      }
    },
    created () {
      this.get_query()
    },
    mounted () {
      this.$nextTick(function () {
        this.drawGraph('container')
      })
    },
    watch: {
      value: function () {
        // todo 优化一下代码结构
        for (var k in this.value) {
//          console.log(k)
          this.data[this.value[k].variable_name] = {name: this.value[k].variable_name, data: [], time: []}
        }
//        console.log(this.data)
        for (var l in this.value) {
          this.data[this.value[l].variable_name].data.push(this.value[l].value)
          this.data[this.value[l].variable_name].time.push(this.value[l].time)
        }
//        console.log(this.data)
        for (var i in this.data) {
          this.arr.push({name: this.data[i]['name'], type: 'line', data: this.data[i]['data']})
          this.legends.push(this.data[i].name)
          for (var j in this.data[i].time) {
            this.date.push(this.change_time(this.data[i].time[j]))
          }
        }

//        console.log(this.arr)
//        console.log('a')
        this.options.xAxis.data = this.date
//        console.log('b')
        this.options.legend.data = this.legends
//        console.log('c')
        this.options.series = this.arr
//        console.log('d')
        this.chart.showLoading()
        setTimeout(() => {
          this.chart.setOption(this.options)
        }, 500)
        this.chart.hideLoading()
//        console.log('e')
        
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
      post_query_variable () {
        new HistoryGroup()
          .POST({
            data: {id: this.query_id}
          })
          .then((res) => {
            this.variables = res.data['data'][0]['variable']
          })
      },
      get_value () {
        new Value()
          .POST({
            data: {
//              variable_name: this.variable_name,
              variable_id: this.variable_id,
              min_time: Date.parse(this.time[0]) / 1000,
              max_time: Date.parse(this.time[1]) / 1000
            }
          })
          .then((res) => {
            this.value = res.data['data']
          })
      },
      drawGraph (id) {
        // 绘图方法
        this.chart = echarts.init(document.getElementById(id))
        // 皮肤添加同一般使用方式
//        this.chart.showLoading()
//        this.chart.setOption(this.options)
//        this.chart.hideLoading()
      },
      change_time (time) {
        return new Date(parseInt(time) * 1000).toLocaleString().replace(/年|月/g, '-').replace(/日/g, ' ')
      }
    }
  }
</script>
