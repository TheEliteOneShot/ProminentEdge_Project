<script lang="ts">

//@ts-ignore
import { GoogleMap, Marker } from "vue3-google-map";

import { defineComponent } from "vue";
import GridFromServer from '/@src/components/GridFromServer.vue'
import config from '/@src/config';
import convertDate from '/@src/utility/convert_date';

import { getUploadedCadFiles } from '/@src/api/getUploadedCadFiles';
import { uploadCadFiles } from '/@src/api/uploadCadFiles';

import { getApparatusInformationByCadFileID } from '/@src/api/getApparatusInformationByCadFileID';

import { ref } from 'vue';
import { DateFilterModelFormatter } from "ag-grid-community/dist/lib/filter/provided/date/dateFilter";

export default defineComponent({
  components: { GoogleMap, Marker, GridFromServer },
  setup() {

    const googleMapsApiKey = ref<string>(config.GOOGLE_MAPS_API_KEY);

    const isUploadingCADFileFalseText = "Upload Selected CAD Files";
    const isUploadingCADFileTrueText = "Uploading Selected CAD Files...";
    const uploadCadFileText = ref<string>(isUploadingCADFileFalseText);
    const uploadCadFileLoadingHidden = ref<Boolean>(true);

    const selectedCadFile = ref<string>("No CAD File Selected");

    const files = ref<null | File[]>(null);
    const fileNames = ref<string[]>([]);

    const onFileUploadChanged = async () => {
      fileNames.value = [];
      files?.value?.forEach((file: any) => {
        fileNames.value.push(file.name);
      });
    };

    const updateGoogleMaps = async () => {

      //@ts-ignore
      // This variable is set in the index.html file
      var currentlySelectedCadFileId = currentCadFileIdSelected;

      let result = await getApparatusInformationByCadFileID(currentlySelectedCadFileId);

      locations.value = [];

      result.forEach( (item: any, index: any) => {
        console.log(index);
        if (index == 0) {
          center.value = { lat: Number(item.latitude), lng: Number(item.longitude) };
        }
        var operative_word = "";
        switch(item.type) {
          case "arrived":
            operative_word = "had";
            break;
          case "available":
          case "cleared":
          case "dispatched":
          case "enroute":
          case "~":
          default:
            operative_word = "was";
            break;
        }
        locations.value.push(
          {
            position: { lat: Number(item.latitude), lng: Number(item.longitude) },
            label: item.unit_id + ` ${operative_word} ` + item.type + ' at ' + convertDate(new Date(item.timestamp)),
            title: item.unit_id + ` ${operative_word} ` + item.type + ' at ' + convertDate(new Date(item.timestamp)),
          }
          )
      })
    };

    const center = ref({ lat: -31.56391, lng: 147.154312  });

    var locations = ref([{}]);


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
        { field: 'SELECTED', 
          mindWidth: 50, 
          flex: 1,
          cellRenderer: ((params:any) => {
          return `<input onclick="onCadFileSelectedFromAgGrid(this)" type='checkbox' ${params.value ? ' unchecked' : ''} value='${params.value}' />`; 
        }),
        },
        { field: 'fileName', mindWidth: 50, flex: 1 },
        { field: 'version', mindWidth: 50, flex: 1 },
        { field: 'uploaded_date', mindWidth: 50, flex: 1 },
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

    const uploadSelectedCadFiles = async () => {
      const formData = new FormData();

      files.value?.forEach(file => {
        formData.append('file', file);
      });

      await setIsUploadingCadFile(true)
        .then(() => uploadCadFiles(formData))
        .then(() => setIsUploadingCadFile(false))
        .then(() => location.reload() );

    }

    return {updateGoogleMaps, locations, center, googleMapsApiKey, gridServerDataSource, gridServerDataOptions, selectedCadFile, files, onFileUploadChanged, fileNames, uploadCadFileText, uploadCadFileLoadingHidden, uploadSelectedCadFiles };
  },
});
</script>

<template>
  <h1 style="position:center">Easy Computer Aided Response (CAD) Viewing Tool</h1>

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
    <BAccordionItem v-on:update:model-value="updateGoogleMaps" title="View Selected CAD File Location Details">
      <h2>{{ selectedCadFile }}</h2>
      <BCardGroup deck>
        <BCard title="Google Map Location" style="position:center; width: 50rem;">

          <GoogleMap id="googleMapElement" :api-key="googleMapsApiKey" style="width: 100%; height: 500px" :center="center"
            :zoom="15">
            <Marker v-for="(location, i) in locations" :options="{ position: location.position, label: location.label, title: location.title }" :key="i" />
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
