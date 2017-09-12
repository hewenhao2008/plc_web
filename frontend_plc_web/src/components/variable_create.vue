<template>
  <Modal v-model="showCreate" title="新建" :mask-closable="false" :closable="false">

    <!--<p slot="close"><Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button></p>-->
    <Form ref="formVariable" :model="formVariable" :label-width="80">

      <FormItem label="变量名" prop="variable_name">
        <Input v-model="formVariable.variable_name" placeholder="请输入变量名"></Input>
      </FormItem>

      <FormItem label="变量组名" prop="group_id">
        <Select transfer v-model="formVariable.group_id" style="width:100px" placeholder="选择变量组"
                filterable>
          <Option v-for="group in groups" :value="group.id" :key="group.id">{{ group.group_name }}</Option>
        </Select>
      </FormItem>

      <FormItem label="存储区域" prop="area">
        <Select transfer v-model="formVariable.area" style="width:100px" placeholder="选择存储区域" filterable>
          <Option value="1">DB</Option>
          <Option value="2">Input</Option>
          <Option value="3">Output</Option>
          <Option value="4">Merkers</Option>
        </Select>
      </FormItem>

      <FormItem label="DB块号码" prop="db_num">
        <Input v-model="formVariable.db_num" placeholder="请输入DB块号码"></Input>
      </FormItem>

      <FormItem label="地址" prop="address">
        <Input v-model="formVariable.address" placeholder="请输入地址"></Input>
      </FormItem>

      <FormItem label="数据类型" prop="data_type">
        <Select transfer v-model="formVariable.data_type" style="width:100px" placeholder="选择数据类型"
                filterable>
          <Option value="FLOAT">FLOAT</Option>
          <Option value="INT">INT</Option>
          <Option value="DINT">DINT</Option>
          <Option value="WORD">WORD</Option>
          <Option value="BYTE">BYTE</Option>
          <Option value="BOOL">BOOL</Option>
        </Select>
      </FormItem>

      <FormItem label="读写类型" prop="rw_type">
        <RadioGroup v-model="formVariable.rw_type">
          <Radio label="1">只读</Radio>
          <Radio label="2">只写</Radio>
          <Radio label="3">读写</Radio>
        </RadioGroup>
      </FormItem>

      <FormItem label="是否上传">
        <RadioGroup v-model="formVariable.upload">
          <Radio label="1">是</Radio>
          <Radio label="0">否</Radio>
        </RadioGroup>
      </FormItem>

      <FormItem label="采集周期" prop="acquisition_cycle">
        <Select transfer v-model="formVariable.acquisition_cycle" style="width:100px" placeholder="选择采集周期"
                filterable>
          <Option value="1">1s</Option>
          <Option value="10">10s</Option>
          <Option value="30">30s</Option>
          <Option value="60">60s</Option>
          <Option value="600">600s</Option>
        </Select>
      </FormItem>

      <FormItem label="上传周期" prop="server_record_cycle">
        <Select transfer v-model="formVariable.server_record_cycle" style="width:100px"
                placeholder="选择上传周期"
                filterable>
          <Option value="10">10s</Option>
          <Option value="30">30s</Option>
          <Option value="60">60s</Option>
          <Option value="600">600s</Option>
        </Select>
      </FormItem>

      <FormItem label="写入值" prop="write_value">
        <Input v-model="formVariable.write_value" placeholder="请输入写入值"></Input>
      </FormItem>

      <FormItem label="备注" prop="note">
        <Input v-model="formVariable.note" placeholder="请输入备注"></Input>
      </FormItem>

    </Form>
    <div slot="footer">
      <Button type="success" :loading="loading" @click="createSubmit">提交</Button>
      <Button type="success" :loading="loading" @click="createSubmitContinue">提交并继续</Button>
      <Button type="ghost" @click="handleClean('formVariable')" style="margin-left: 8px">清空</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>

</template>

<script>
  import Group from '../models/actions/group'
  import Variable from '../models/actions/variable'

  export default {
    data () {
      return {
        loading: false,
        formVariable: {
          variable_name: null,
          group_id: null,
          address: null,
          acquisition_cycle: null,
          data_type: null,
          db_num: null,
          note: null,
          rw_type: null,
          server_record_cycle: null,
          ten_id: null,
          upload: null,
          write_value: null
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
      get_group () {
        new Group()
          .GET()
          .then((res) => {
            this.groups = res.data['data']
          })
      },
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
        new Variable()
          .PUT({
            data: this.formVariable
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
        new Variable()
          .PUT({
            data: this.formVariable
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
