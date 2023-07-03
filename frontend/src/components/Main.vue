<script lang="ts">

//@ts-ignore
import { GoogleMap, Marker } from "vue3-google-map";

import { defineComponent } from "vue";
import GridFromServer from '/@src/components/GridFromServer.vue'
import config from '/@src/config';

import { getUploadedCadFiles } from '/@src/api/getUploadedCadFiles';
import { uploadCadFiles } from '/@src/api/uploadCadFiles';

import { ref } from 'vue';

export default defineComponent({
  components: { GoogleMap, Marker, GridFromServer },
  setup() {
    const googleMapsApiKey = ref<string>(config.GOOGLE_MAPS_API_KEY);

    const isUploadingCADFileFalseText = "Upload Selected CAD Files";
    const isUploadingCADFileTrueText = "Uploading Selected CAD Files...";
    const uploadCadFileText = ref<string>(isUploadingCADFileFalseText);
    const uploadCadFileLoadingHidden = ref<Boolean>(true);

    const center = { lat: 40.689247, lng: -74.044502 };

    const selectedCadFile = ref<string>("No CAD File Selected");

    const files = ref<null | File[]>(null);
    const fileNames = ref<string[]>([]);

    const onFileUploadChanged = async () => {
      fileNames.value = [];
      files?.value?.forEach((file: any) => {
        fileNames.value.push(file.name);
      });
    }

    const gridServerDataSource = async () => {
      return {
        getRows: async function (params: any) {
          return await getUploadedCadFiles()
            .then(async (data: any) => {
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
      { field: 'CADFILE_ID', mindWidth: 50, flex: 1 },
        { field: 'fileName', mindWidth: 50, flex: 1 },
        { field: 'version', mindWidth: 50, flex: 1 },
        { field: 'uploaded_dt', mindWidth: 50, flex: 1 },
      ],
      defaultColDef: {
        sortable: true,
        resizable: true,
      },
      rowModelType: 'serverSide',
      serverSideStoreType: 'full',
      animateRows: true,
    };

    const setIsUploadingCadFile = async (status: Boolean) => {
      if (status) {
        uploadCadFileText.value = isUploadingCADFileTrueText;
      } else {
        uploadCadFileText.value = isUploadingCADFileFalseText;
        alert('File upload completed');
      }
      uploadCadFileLoadingHidden.value = !status;
    }

    const showSelectedFile = async () => {
      alert(googleMapsApiKey.value);
    };

    const uploadSelectedCadFiles = async () => {
      const formData = new FormData();

      files.value?.forEach(file => {
        formData.append('file', file);
      });

      await setIsUploadingCadFile(true)
        .then(() => uploadCadFiles(formData))
        .then(() => setIsUploadingCadFile(false));

    }

    return { center, googleMapsApiKey, gridServerDataSource, gridServerDataOptions, selectedCadFile, files, showSelectedFile, onFileUploadChanged, fileNames, uploadCadFileText, uploadCadFileLoadingHidden, uploadSelectedCadFiles };
  },
});
</script>

<template>
  <h1 style="position:center">Quick Computer Aided Response (CAD) Viewing Tool</h1>
  <!-- <BButton v-on:click="showSelectedFile">Button</BButton> -->
  <BAccordion>
    <BAccordionItem title="Upload CAD File">
      <BFormFile v-on:change="onFileUploadChanged" accept="application/JSON" class="mt-3" size="lg" v-model="files"
        label="Select any CAD .json files that conforms to the example data that was sent with the project requirements."
        multiple />
      <div class="mt-3">
        Selected CAD Files: <strong>{{ fileNames }}</strong>
      </div>
      <br />
      <br />
      <div style="position:relative;">
        <BButton v-on:click="uploadSelectedCadFiles" style="width:20rem" variant="success">
          <BSpinner :hidden="uploadCadFileLoadingHidden" small />
          {{ uploadCadFileText }} &nbsp;&nbsp;
        </BButton>
      </div>
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
          <GoogleMap :api-key="googleMapsApiKey" style="width: 100%; height: 500px" :center="center"
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
