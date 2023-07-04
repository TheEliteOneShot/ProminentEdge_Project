<script lang="ts">

//@ts-ignore
import { GoogleMap, Marker } from "vue3-google-map";

import { defineComponent } from "vue";
import GridFromServer from '/@src/components/GridFromServer.vue'
import config from '/@src/config';
//@ts-ignore
import { convertDate, convertDateToYear } from '/@src/utility/convert_date';

import { getUploadedCadFiles } from '/@src/api/getUploadedCadFiles';
import { uploadCadFiles } from '/@src/api/uploadCadFiles';
import { getApparatusInformationByCadFileID } from '/@src/api/getApparatusInformationByCadFileID';
import { getWeatherPointData } from '/@src/api/getWeatherPointData';

import { ref } from 'vue';

export default defineComponent({
  components: { GoogleMap, Marker, GridFromServer },
  setup() {

    const googleMapsApiKey = ref<string>(config.GOOGLE_MAPS_API_KEY);
    var defaultGoogleMapLocation = ref({ lat: 40.689247, lng: -74.044502 });
    var locations = ref([{}]);

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

      if (currentlySelectedCadFileId == undefined || null) return;

      let result = await getApparatusInformationByCadFileID(currentlySelectedCadFileId);
      if (result.length > 0) {
        selectedCadFile.value = `Currently Selected CAD -> FILE_NAME: [${result[0].FILE_NAME}] FILE_ID: [${result[0].FILE_ID}]`;
      }


      locations.value = [];

      result.forEach((item: any, index: any) => {
        if (index == 0) {
          defaultGoogleMapLocation.value = { lat: Number(item.latitude), lng: Number(item.longitude) };
        }
        var operative_word = "";
        switch (item.type) {
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
            timestamp: item.timestamp,
            geoHash: item.geohash,
            eventDuration: item.event_duration,
            responseDuration: item.response_duration,
            turnoutDuration: item.turnout_duration,
            travelDuration: item.travel_duration,
            unitId: item.unit_id,
            carId: item.car_id,
            unitType: item.unit_type,
            eventType: item.type,
          }
        )
      })
    };

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
        {
          field: 'SELECTED_FILE_ID',
          mindWidth: 50,
          flex: 1,
          cellRenderer: ((params: any) => {
            return `<input onclick="onCadFileSelectedFromAgGrid(this)" type='checkbox' ${params.value ? ' unchecked' : ''} value='${params.value}' /> ${params.value}`;
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
        .then(() => location.reload());

    }

    const latitude = ref();
    const longitude = ref();
    const label = ref();
    const timestamp = ref();
    const geoHash = ref();
    const eventDuration = ref();
    const responseDuration = ref();
    const travelDuration = ref();
    const turnoutDuration = ref();
    const unitId = ref();
    const carId = ref();
    const unitType = ref();
    const eventType = ref();

    const prcp = ref();
    const pres = ref();
    const snow = ref();
    const tavg = ref();
    const tmax = ref();
    const tmin = ref();
    const tsun = ref();
    const wdir = ref();
    const wpgt = ref();
    const wspd= ref();

    const markerClicked = async (
              event_position: any,
              event_label: any,
              event_timestamp: any,
              event_geoHash: any,
              event_eventDuration: any,
              event_responseDuration: any,
              event_turnoutDuration: any,
              event_travelDuration: any,
              event_unitId: any,
              event_carId: any,
              event_unitType: any,
              event_type: any
              ) => {
      let timestampToYear = convertDateToYear(new Date(event_timestamp));
      let result = await getWeatherPointData(event_position.lat, event_position.lng, timestampToYear, timestampToYear)
      .then(response => response?.data[0]);

      prcp.value = result.prcp;
      pres.value = result.pres;
      snow.value = result.snow;
      tavg.value = result.tavg;
      tmax.value = result.tmax;
      tmin.value = result.tmin;
      tsun.value = result.tsun;
      wdir.value = result.wdir;
      wpgt.value = result.wpgt;
      wspd.value = result.wspd;

      latitude.value = event_position.lat;
      longitude.value = event_position.lng;
      label.value = event_label;
      geoHash.value = event_geoHash;
      eventDuration.value = event_eventDuration;
      responseDuration.value = event_responseDuration;
      travelDuration.value = event_travelDuration;
      turnoutDuration.value = event_turnoutDuration;
      unitId.value = event_unitId;
      carId.value = event_carId;
      unitType.value = event_unitType;
      eventType.value = event_type;

      timestamp.value = convertDate(new Date(event_timestamp));
    }

    return { 
      eventType,
      unitId,
      carId,
      unitType,
      eventDuration, 
      responseDuration, 
      travelDuration, 
      turnoutDuration, 
      prcp, 
      pres, 
      snow, 
      tavg, 
      tmax, 
      tmin, 
      tsun,
      wdir, 
      wpgt, 
      wspd, 
      markerClicked, 
      latitude, 
      longitude, 
      label, 
      timestamp,
      geoHash, 
      updateGoogleMaps, 
      locations, 
      defaultGoogleMapLocation, 
      googleMapsApiKey, 
      gridServerDataSource, 
      gridServerDataOptions, 
      selectedCadFile, 
      files,
      onFileUploadChanged,
      fileNames,
      uploadCadFileText, 
      uploadCadFileLoadingHidden, 
      uploadSelectedCadFiles 
    };
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
        <BCard title="Event Locations - Click a Marker for details" style="position:center; width: 50rem;">

          <GoogleMap id="googleMapElement" :api-key="googleMapsApiKey" style="width: 100%; height: 500px"
            :center="defaultGoogleMapLocation" :zoom="15">
            <Marker @click="markerClicked(
              //@ts-ignore
              location.position,
              //@ts-ignore
              location.label,
              //@ts-ignore
              location.timestamp,
              //@ts-ignore
              location.geoHash,
              //@ts-ignore
              location.eventDuration,
              //@ts-ignore
              location.responseDuration,
              //@ts-ignore
              location.turnoutDuration,
              //@ts-ignore
              location.travelDuration,
              //@ts-ignore
              location.unitId,
              //@ts-ignore
              location.carId,
              //@ts-ignore
              location.unitType,
              //@ts-ignore
              location.eventType
              )"
              v-for="(location, i) in locations"
              :options="{
                //@ts-ignore
                position: location.position, 
                //@ts-ignore
                label: location.label, 
                //@ts-ignore
                title: location.title 
                }" :key="i" />
          </GoogleMap>

        </BCard>

        <BTableSimple hover small caption-top stacked>
          <BThead head-variant="dark">
            <BTr>
              <BTh>Description</BTh>
              <BTh>Event Type</BTh>
              <BTh>Title</BTh>
              <BTh>Event Duration</BTh>
              <BTh>Response Duration</BTh>
              <BTh>Travel Duration</BTh>
              <BTh>Turnout Duration</BTh>
              <BTh>Unit ID</BTh>
              <BTh>Car ID</BTh>
              <BTh>Unit Type</BTh>
              <BTh>Latitude</BTh>
              <BTh>Longitude</BTh>
              <BTh>Geohash</BTh>
              <BTh>Timestamp</BTh>
            </BTr>
          </BThead>
          <BTbody>
            <BTr>
              <BTh rowspan="5" class="text-center">Marker Details</BTh>
              <BTd stacked-heading="Description">{{ label }}</BTd>
              <BTd stacked-heading="Event Type">{{ eventType }}</BTd>
              <BTd stacked-heading="Event Duration">{{ eventDuration }}</BTd>
              <BTd stacked-heading="Response Duration">{{ responseDuration }}</BTd>
              <BTd stacked-heading="Travel Duration">{{ travelDuration }}</BTd>
              <BTd stacked-heading="Turnout Duration">{{ turnoutDuration }}</BTd>
              <BTd stacked-heading="Unit ID">{{ unitId }}</BTd>
              <BTd stacked-heading="Car ID">{{ carId }}</BTd>
              <BTd stacked-heading="Unit Type">{{ unitType }}</BTd>
              <BTd stacked-heading="Latitude">{{ latitude }}</BTd>
              <BTd stacked-heading="Longitude">{{ longitude }}</BTd>
              <BTd stacked-heading="Geohash">{{ geoHash }}</BTd>
              <BTd stacked-heading="Timestamp">{{ timestamp }}</BTd>
            </BTr>
          </BTbody>

        </BTableSimple>
        <BTableSimple hover small caption-top stacked>
          <BThead head-variant="dark">
            <BTr>
              <BTh>Average Air Temperature in °C</BTh>
              <BTh>Minimum Air Temperature in °C</BTh>
              <BTh>Maximum Air Temperature in °C</BTh>
              <BTh>Daily Precipitation Total in mm</BTh>
              <BTh>Maximum Snow Depth in mm</BTh>
              <BTh>Average Wind Direction in degrees (°)</BTh>
              <BTh>Average Wind Speed in km/h</BTh>
              <BTh>Peak Wind Gust in km/h</BTh>
              <BTh>Average Sea-level Air Pressure in hPa</BTh>
              <BTh>Daily Sunshine Total in minutes (m)</BTh>
            </BTr>
          </BThead>
          <BTbody>
            <BTr>
              <BTh rowspan="5" class="text-center">Weather  [{{ timestamp }}] [Latitude: {{ latitude }} / Longitude: {{ longitude }}]</BTh>
              <BTd stacked-heading="Average Air Temperature in °C">{{ tavg }}</BTd>
              <BTd stacked-heading="Minimum Air Temperature in °C">{{ tmin }}</BTd>
              <BTd stacked-heading="Maximum Air Temperature in °C">{{ tmax }}</BTd>
              <BTd stacked-heading="Daily Precipitation Total in mm">{{ prcp }}</BTd>
              <BTd stacked-heading="Maximum Snow Depth in mm">{{ snow }}</BTd>
              <BTd stacked-heading="Average Wind Direction in degrees (°)">{{ wdir }}</BTd>
              <BTd stacked-heading="Average Wind Speed in km/h">{{ wspd }}</BTd>
              <BTd stacked-heading="Peak Wind Gust in km/h">{{ wpgt }}</BTd>
              <BTd stacked-heading="Average Sea-level Air Pressure in hPa">{{ pres }}</BTd>
              <BTd stacked-heading="Daily Sunshine Total in minutes (m)">{{ tsun }}</BTd>
              
            </BTr>
          </BTbody>
          
        </BTableSimple>
      </BCardGroup>
    </BAccordionItem>
  </BAccordion>
</template>

<style scoped></style>
