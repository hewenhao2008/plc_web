<template>
  <Modal v-model="showCreate" title="编辑" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formPLC" :model="formPLC" :label-width="80">

      <FormItem label="PLC名称" prop="plc_name">
        <Input v-model="formPLC.plc_name" placeholder="请输入PLC名称"></Input>
      </FormItem>

      <FormItem label="站点名称" prop="station_id">
        <Select transfer v-model="formPLC.station_id" style="width:100px" placeholder="选择站点"
                filterable>
          <Option v-for="station in stations" :value="station.id" :key="station.id">{{ station.station_name }}</Option>
        </Select>
      </FormItem>

      <FormItem label="IP地址" prop="ip">
        <Input v-model="formPLC.ip" placeholder="请输入IP地址"></Input>
      </FormItem>

      <FormItem label="MPI地址" prop="mpi">
        <Input v-model="formPLC.mpi" placeholder="请输入MPI地址"></Input>
      </FormItem>

      <FormItem label="通讯类型" prop="type">
        <Select transfer v-model="formPLC.type" style="width:100px" placeholder="选择通讯类型" filterable>
          <Option value="1">以太网</Option>
          <Option value="2">MPI</Option>
          <Option value="3">西门子S7ONLIN</Option>
        </Select>
      </FormItem>

      <FormItem label="PLC型号" prop="plc_type">
        <Select transfer v-model="formPLC.plc_type" style="width:100px" placeholder="选择数据类型"
                filterable>
          <Option value="S7-200 Smart">S7-200 Smart</Option>
          <Option value="S7-200">S7-200</Option>
          <Option value="S7-300PN/DP">S7-300PN/DP</Option>
          <Option value="S7-300 DP">S7-300 DP</Option>
        </Select>
      </FormItem>

      <FormItem label="备注" prop="note">
        <Input v-model="formPLC.note" placeholder="请输入备注"></Input>
      </FormItem>

    </Form>
    <div slot="footer">
      <Button type="success" :loading="loading" @click="editSubmit('formPLC')">提交</Button>
      <Button type="ghost" @click="handleReset()" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="handleClean('formPLC')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>
</template>

<script>
  import PLC from '../models/actions/plc'

  export default {
    data () {
      return {
        loading: false,
        formPLC: {
          id: null,
          plc_name: null,
          station_id: null,
          ip: null,
          mpi: null,
          type: null,
          plc_type: null,
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
      'showCreate',
      'stations',
      'data'
    ],
    watch: {
      data: function () {
        this.data2form()
      }
    },
    methods: {
      data2form () {
        this.formVariableEdit.id = this.data.id
        this.formVariableEdit.plc_name = this.data.plc_name
        this.formVariableEdit.station_id = this.data.station_id
        this.formVariableEdit.ip = this.data.ip
        this.formVariableEdit.mpi = this.data.mpi
        this.formVariableEdit.type = this.data.type
        this.formVariableEdit.plc_type = this.data.plc_type
      },
      editSubmit (name) {
        this.loading = true
        this.$refs[name].validate((valid) => {
          if (valid) {
            new PLC()
              .PUT({
                data: this.formVariableEdit
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

