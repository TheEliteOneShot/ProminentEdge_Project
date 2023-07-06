<script lang="ts">
import { defineComponent, onMounted, onActivated, ref } from 'vue';

import agGrid from '/@src/ag-grid';

export default defineComponent({
  name: 'GridUserItems',
  props: ['serverDataSource', 'options'],
  setup(props) {

    onActivated(async () => {
      if (props.options?.api?.refreshServerSideStore !== undefined)
        props.options.api.refreshServerSideStore();
    });

    const onGridReady = async (params: any) => {
      params.api.showLoadingOverlay();
    };

    const onFirstDataRendered = async (params: any) => {
      params.api.sizeColumnsToFit();
      await new Promise((resolve) => setTimeout(resolve, 100));
      showGrid.value = true;
      params.api.hideOverlay();
    };

    onMounted(async () => {
      const element = document.querySelector('#gridTarget');
      props.options.onFirstDataRendered = onFirstDataRendered;
      props.options.onGridReady = onGridReady;
      await agGrid.Grid(element, props.options);
      props.options.api.setServerSideDatasource(await props.serverDataSource());
    });

    const showGrid = ref(false);

    return { showGrid };
  },
});
</script>

<template>
  <div class="container">
    <div
      id="gridTarget"
      :class="{
        visible: showGrid,
        'ag-theme-alpine-dark': true,
      }"
      style="height: 600px; width: 100"
      class=""
    ></div>
  </div>
</template>

<style>
.ag-overlay-panel {
  background-color: darkgrey !important;
}
</style>
