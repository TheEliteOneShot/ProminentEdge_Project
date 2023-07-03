<script lang="ts">
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";
import GridFromServer from '/@src/components/GridFromServer.vue'

import { getTestItems } from '/@src/api/getTestItems';

import { ref } from 'vue';

export default defineComponent({
  components: { GoogleMap, Marker, GridFromServer },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };

    const selectedCadFile = ref("No CAD File Selected");

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

    return { center, gridServerDataSource, gridServerDataOptions, selectedCadFile };
  },
});
</script>

<template>
  <h1 style="position:center">Quick Computer Aided Response (CAD) Viewing Tool</h1>
  <BAccordion>
  <BAccordionItem title="Upload CAD File">
    Upload Here
  </BAccordionItem>
  <BAccordionItem title="Select CAD File">
    <BCard title="CAD File" style="position:center; mwidth: 100rem;">
    <GridFromServer :server-data-source="gridServerDataSource" :options="gridServerDataOptions" />
  </BCard>
  </BAccordionItem>
  <BAccordionItem title="View Selected CAD File Location Details">
    <h2>{{ selectedCadFile }}</h2>
    <BCardGroup deck>
    <BCard title="Google Map Location" style="position:center; width: 50rem;">
    <GoogleMap api-key="AIzaSyAx649U3JEg5Z_Xy2WXfmLF9wYH0ofm4rk" style="width: 100%; height: 500px" :center="center"
      :zoom="15">
      <Marker :options="{ position: center }" />
    </GoogleMap>
  </BCard>
  <BCard title="Historical weather at time and place" style="position:center; width: 50rem;">
    Weather here
  </BCard>
  </BCardGroup>
  </BAccordionItem>
</BAccordion>


</template>

<style scoped></style>
