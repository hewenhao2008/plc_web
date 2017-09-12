<template>
  <!-- Modal begin-->
  <div class="modal fade" id="edit" tabindex="-1" role="dialog" aria-labelledby="edit">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
            aria-hidden="true">&times;</span>
          </button>
          <h4 class="modal-title" id="myModalLabel1">工艺参数编辑</h4>
        </div>
        <div class="modal-body">
          <ul>
            <li>
              <label><span>变量ID：</span></label>
              <input type="text" id="variable_id" v-bind:value="vari.variable_id" readonly>
            </li>
            <li>
              <label><span>变量名：</span></label>
              <input type="text" id="variable_name" v-bind:value="vari.variable_name" readonly>
            </li>

            <li>
              <label><span>参数名称：</span></label>
              <input type="text" id="param_name" value="">
            </li>
            <li>
              <label><span>单位：</span></label>
              <input type="text" id="unit" value="">
            </li>

          </ul>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal">取消</button>
          <button type="button" class="btn btn-primary btn-sm" v-on:click="save(message.id)">保存</button>
        </div>
      </div>
    </div>
  </div>
  <!--Modal end-->
</template>
