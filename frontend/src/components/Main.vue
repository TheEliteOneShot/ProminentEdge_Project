<script setup lang="ts">
import GridFromServer from '/@src/components/GridFromServer.vue'

import { getTestItems } from '/@src/api/getTestItems';

import { ref } from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)

const gridServerDataSource = async () => {
  return {
    getRows: async function (params: any) {
      return await getTestItems()
        .then(async (data) => {
          params.success({ rowData: data });
        })
        .catch(() => {
          params.fail();
        });
    },
  };
};

const gridServerDataOptions = {
  columnDefs: [
    { field: 'id', mindWidth: 50, flex: 1 },
    { field: 'data', flex: 2, minWidth: 500 },
  ],
  defaultColDef: {
    sortable: true,
    resizable: true,
  },
  rowModelType: 'serverSide',
  serverSideStoreType: 'full',
  animateRows: true,
};

async function test() {
  const result = await getTestItems();
  alert(JSON.stringify(result));
}

</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <p>
      Count: {{ count }}
    </p>
  </div>

  <div>
    <BButton @click="test()" variant="outline-primary">Test</BButton>
    <BButton @click="count++" variant="danger">Increment</BButton>
    <BButton @click="count++" variant="success">Increment</BButton>
    <BButton @click="count++" variant="outline-primary">Increment</BButton>
  </div>

  <BCardGroup deck>
  <BCard
    header="featured"
    header-tag="header"
    footer="Card Footer"
    footer-tag="footer"
    title="Title"
  >
    <BCardText>Header and footers using props.</BCardText>
    <BButton href="#" variant="primary">Go somewhere</BButton>
  </BCard>

  <BCard title="Title" header-tag="header" footer-tag="footer">
    <template #header>
      <h6 class="mb-0">Header Slot</h6>
    </template>
    <BCardText>Header and footers using slots.</BCardText>
    <BButton href="#" variant="primary">Go somewhere</BButton>
    <template #footer>
      <em>Footer Slot</em>
    </template>
  </BCard>
</BCardGroup>


<GridFromServer
      :server-data-source="gridServerDataSource"
      :options="gridServerDataOptions"
    />

</template>

<style scoped>
</style>
