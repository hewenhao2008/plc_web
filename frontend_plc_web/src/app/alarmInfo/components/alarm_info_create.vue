<template>

  <Modal v-model="showCreate" title="新建" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formAlarmInfo" :model="formAlarmInfo" :label-width="80" inline>


      <FormItem label="选择变量" prop="variable_id">

        <Select v-model="group_id" style="width:100px" placeholder="选择变量组" filterable @on-change="post_variable">
          <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
        </Select>

        <Select transfer v-model="formAlarmInfo.variable_id" style="width:100px" placeholder="选择变量名"
                filterable>
          <Option v-for="variable in variables" :value="variable.id" :key="variable.id">{{ variable.variable_name }}
          </Option>
        </Select>

      </FormItem>

      <FormItem label="报警类型" prop="alarm_type">
        <Select transfer v-model="formAlarmInfo.alarm_type" style="width:100px" placeholder="选择报警类型" filterable>
          <Option value="1">提示</Option>
          <Option value="2">警告</Option>
          <Option value="3">错误</Option>
        </Select>
      </FormItem>

      <FormItem label="报警内容" prop="note">
        <Input v-model="formAlarmInfo.note" placeholder="请输入报警内容"></Input>
      </FormItem>


    </Form>
    <div slot="footer">
      <Button type="success" :loading="loading" @click="createSubmit">提交</Button>
      <Button type="success" :loading="loading" @click="createSubmitContinue">提交并继续</Button>
      <Button type="ghost" @click="handleClean('formAlarmInfo')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>


</template>


<script>
  import AlarmInfo from '@/models/actions/alarm_info'
  import Variable from '@/models/actions/variable'

  export default {
    data () {
      return {
        loading: false,
        group_id: '',
        variables: [],
        formAlarmInfo: {
          variable_id: null,
          alarm_type: null,
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
      'groups'
    ],
    methods: {
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
      createSubmit () {
        this.loading = true
        new AlarmInfo()
          .PUT({
            data: this.formAlarmInfo
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
        new AlarmInfo()
          .PUT({
            data: this.formAlarmInfo
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
      handleClean (name) {
        this.$refs[name].resetFields()
      },
      close () {
        this.$emit('close')
      }
    }
  }
</script>
