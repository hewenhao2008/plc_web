<template>

  <Modal v-model="showEdit" title="编辑" :mask-closable="false" :closable="false">

    <div slot="header">
      <span style="float: left">编辑</span>
      <span style="float: right">
      <Button type="ghost" size="small" @click="close" style="margin-left: 8px">
        <Icon type="close"></Icon>
      </Button>
        </span>
      <br><br>
    </div>

    <Form ref="formStation" :model="formStation" :label-width="80">

      <FormItem label="站名称" prop="station_name">
        <Input v-model="formStation.station_name" placeholder="请输入站名称"></Input>
      </FormItem>

      <FormItem label="MAC地址" prop="mac">
        <Input v-model="formStation.mac" placeholder="请输入MAC地址"></Input>
      </FormItem>

      <FormItem label="IP地址" prop="ip">
        <Input v-model="formStation.ip" placeholder="请输入IP地址"></Input>
      </FormItem>

      <FormItem label="PLC数量" prop="plc_count">
        <Input v-model="formStation.plc_count" placeholder="请输入PLC数量"></Input>
      </FormItem>

      <FormItem label="站标识号" prop="id_num">
        <Input v-model="formStation.id_num" placeholder="请输入站标识号"></Input>
      </FormItem>

      <FormItem label="备注" prop="note">
        <Input v-model="formStation.note" placeholder="请输入备注"></Input>
      </FormItem>

    </Form>

    <div slot="footer">
      <Button type="success" :loading="loading" @click="editSubmit('formStation')">提交</Button>
      <Button type="ghost" @click="handleReset()" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="handleClean('formStation')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>


</template>


<script>
  import Station from '../models/actions/station'

  export default {
    data () {
      return {
        loading: false,
        formStation: {
          id: null,
          station_name: null,
          mac: null,
          ip: null,
          id_num: null,
          plc_count: null,
          note: null
        }
//        ruleVariableCreate: {
//          variable_name: [
//            {required: true, message: '姓名不能为空', trigger: 'blur'}
//          ],
//          mail: [
//            {required: true, message: '邮箱不能为空', trigger: 'blur'},
//            {type: 'email', message: '邮箱格式不正确', trigger: 'blur'}
//          ],
//          city: [
//            {required: true, message: '请选择城市', trigger: 'change'}
//          ],
//          gender: [
//            {required: true, message: '请选择性别', trigger: 'change'}
//          ],
//          interest: [
//            {required: true, type: 'array', min: 1, message: '至少选择一个爱好', trigger: 'change'},
//            {type: 'array', max: 2, message: '最多选择两个爱好', trigger: 'change'}
//          ],
//          date: [
//            {required: true, type: 'date', message: '请选择日期', trigger: 'change'}
//          ],
//          time: [
//            {required: true, type: 'date', message: '请选择时间', trigger: 'change'}
//          ],
//          desc: [
//            {required: true, message: '请输入个人介绍', trigger: 'blur'},
//            {type: 'string', min: 20, message: '介绍不能少于20字', trigger: 'blur'}
//          ]
//        }
      }
    },
    props: [
      'showEdit',
      'data'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    methods: {
      data2form () {
        this.formStation.id = this.data.id
        this.formStation.station_name = this.data.station_name
        this.formStation.mac = this.data.mac
        this.formStation.ip = this.data.ip
        this.formStation.id_num = this.data.id_num
        this.formStation.plc_count = this.data.plc_count
        this.formStation.note = this.data.note
      },
      editSubmit (name) {
        this.loading = true
        this.$refs[name].validate((valid) => {
          if (valid) {
            new Station()
              .PUT({
                data: this.formStation
              })
              .then((res) => {
                this.loading = false
                if (res.data['ok'] === 1) {
                  this.$Message.success(res.data['msg'])
                } else {
                  this.$Message.error(res.data['msg'])
                }
                this.$emit('close')
              })
          } else {
            this.$Message.error('表单验证失败!')
          }
        })
      },
      handleReset () {
        this.data2form()
        this.$Message.warning('已重置')
      },
      handleClean (name) {
        this.$refs[name].resetFields()
      },
      close () {
        this.$emit('close')
      }
    }
  }
</script>
