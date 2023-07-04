const env = {
    GOOGLE_MAPS_API_KEY: import.meta.env.VITE_GOOGLE_MAPS_API_KEY,
    API_BASE_PROTOCOL: import.meta.env.VITE_API_BASE_PROTOCOL,
    API_BASE_HOST: import.meta.env.VITE_API_BASE_HOST,
    API_BASE_PORT: import.meta.env.VITE_API_BASE_PORT,
    API_BASE_PREFIX: import.meta.env.VITE_API_BASE_PREFIX,
};

const routes = {
    baseUrl: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}`,
    baseApi: {
      uploadCadFiles: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}/upload_cad_files`,
      getUploadedCadFiles: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}/get_uploaded_cad_files`,
      getApparatusInformationByCadFileID: `${env.API_BASE_PROTOCOL}://${env.API_BASE_HOST}:${env.API_BASE_PORT}${env.API_BASE_PREFIX}/get_apparatus_information_by_cadfile_id`,
    },
  };
  
const config = { ...env, routes };

export default config;
