<template>

  <Modal v-model="showCreate" title="新建" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formStation" :model="formStation" :label-width="80" inline>

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
      <Button type="success" :loading="loading" @click="createSubmit">提交</Button>
      <Button type="success" :loading="loading" @click="createSubmitContinue">提交并继续</Button>
      <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>

</template>

<script>
  import Station from '@/models/actions/station'

  export default {
    data () {
      return {
        loading: false,
        formStation: {
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
      'showCreate'
    ],
    methods: {
      createSubmit () {
        this.loading = true
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
      },
      createSubmitContinue () {
        this.loading = true
        new Station()
          .PUT({
            data: {}
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
      close () {
        this.$emit('close')
      }
    }
  }
</script>
